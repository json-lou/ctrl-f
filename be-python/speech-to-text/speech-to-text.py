from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
from pymongo import MongoClient

from freq_words import addKeywordsToDatabase

import json
import requests
import sys


# Command line arguments

my_file = str(sys.argv)[0]
youtube_id = str(sys.argv)[1]


# Watson speech-to-text

speech_to_text = SpeechToTextV1(
    iam_apikey='1kUdZGkJF8-KIFqDKWJ17k377RpaG5RZhWtbyRGo22TN'
)
speech_to_text.disable_SSL_verification()


# MongoDB instance

client = MongoClient('mongodb+srv://qhacks:qhacks@cluster0-brdw1.mongodb.net/test?retryWrites=true')
db = client['qhacks']
collection_timestamps = db['timestamps']
collection_transcripts = db['transcripts']



class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)
        self.my_data = None
        self.my_transcript = None

    def on_data(self, data):
        self.my_data = data
        self.my_transcript = data['results'][1]['alternatives'][0]['transcript']

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


myRecognizeCallback = MyRecognizeCallback()


def addToDatabase(file, youtube_id):
    with open(join(dirname(__file__), './.', file), 'rb') as audio_file:
        audio_source = AudioSource(audio_file)
        speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type='audio/flac',
            recognize_callback=myRecognizeCallback,
            smart_formatting=True,
            timestamps=True,
            model='en-US_BroadbandModel',
            max_alternatives=0)

    try:
        print('This is the data object:')
        myRecognizeCallback.my_data['youtube_id'] = youtube_id
        print(myRecognizeCallback.my_data)
        collection_timestamps.insert_one(myRecognizeCallback.my_data)

        formattedText = requests.post('http://bark.phon.ioc.ee/punctuator', data={'text': myRecognizeCallback.my_transcript, 'youtube_id': youtube_id})
        print('This is the formatted transcript:')
        my_transcript = {'transcript': formattedText.text}
        print(formattedText.text)
        collection_transcripts.insert_one(my_transcript)

        addKeywordsToDatabase(formattedText.text, youtube_id)
    except:
        print("Can't connect to database")


addToDatabase(my_file, youtube_id)
