import argparse
from enum import Enum
import io
import sys
import os
from flask import jsonify

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import numpy as np
from moviepy.editor import VideoFileClip
from pymongo import MongoClient


glob_data = []
notes_screenshots = []
length = 0
prev_time = 0
prev_file = ""
secs = 0
temp = ""


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


# not used
def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return image

def get_document_bounds(videoIO, feature, folderPath, youtube_id):

    client = MongoClient('mongodb+srv://qhacks:<PASSWORD>@cluster0-brdw1.mongodb.net/test?retryWrites=true')
    db = client['qhacks']

    global notes_screenshots
    global glob_data
    global length
    global prev_file
    global prev_time
    global secs
    global temp
    """Returns document bounds given an image."""

    # setting up frame by frame per 5 secs
    myclip = VideoFileClip(videoIO)
    frames = []

    for frame in myclip.iter_frames(fps=0.2):
        frames.append(frame)
        # print("hi")

    for count, single_frame in enumerate(frames, start=1):
        # print("stephen")
        #print(i)
        img = Image.fromarray(single_frame,'RGB')

        dir_path = os.path.dirname(os.path.realpath(__file__))

        #print(dir_path)

        file = "/file%d.png" % count

        #print(file)

        #print(folderPath)

        filename = dir_path + "/" + folderPath + "/" + file

        #print(filename)

        img.save(filename)
        #img.show()

        # if length is 5:
        #     break
        # img_process = img.tobytes()

        #runnin the image processor
        first = True
        build_word = ""
        words = []
        # words.append("a")

        client = vision.ImageAnnotatorClient()

        bounds = []

        temp = filename

        #CHANGED HERE
        # content = img_process

        # content = Image.open(filename)
        with io.open(filename, 'rb') as image_file:
            content = image_file.read()

        # print(content)

        image = types.Image(content=content)

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation

        # Collect specified feature bounds by enumerating all document features
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:

                    for word in paragraph.words:

                        # for symbol in word.symbols:
                            #if (feature == FeatureType.SYMBOL):
                                #bounds.append(symbol.bounding_box)

                            #if (feature == FeatureType.WORD):

                        if first and feature == FeatureType.WORD:
                            bounds.append(word.bounding_box)
                            first = False

                        for i in word.symbols:
                            if hasattr(i, "text"):
                                if i.property.detected_break.type is 0:
                                    build_word += i.text
                                else:
                                    build_word += i.text
                                    # print(build_word)
                                    words.append(build_word)
                                    build_word = ""

                    #if (feature == FeatureType.PARA):
                        #bounds.append(paragraph.bounding_box)

                #if (feature == FeatureType.BLOCK):
                    #bounds.append(block.bounding_box)

            #if (feature == FeatureType.PAGE):
                #bounds.append(block.bounding_box)

        # The list `bounds` contains the coordinates of the bounding boxes.

        # temp = {
        #     "bound": bounds
        # }

        # bound_data = {
        #     "v0x": temp['bound'][0].vertices[0].x,
        #     "v0y": temp['bound'][0].vertices[0].y,
        #     "v1x": temp['bound'][0].vertices[1].x,
        #     "v1y": temp['bound'][0].vertices[1].y,
        #     "v2x": temp['bound'][0].vertices[2].x,
        #     "v2y": temp['bound'][0].vertices[2].y,
        #     "v3x": temp['bound'][0].vertices[3].x,
        #     "v3y": temp['bound'][0].vertices[3].y,
        # }

        collection_texts = db['timestamps']

        for i in words:
            db_data = {
                "secs": secs,
                "keyword": i,
                "youtube_id": "tasty"
            }
            collection_texts.insert_one(db_data)

        # db_data = {
        #     "secs": secs,
        #     "keyword": words,
        #     "youtube_id": "hello"
        # }

        data = {
            secs: words
        }

        if(len(data[secs]) == 0):
            data = {
                secs: "a"
            }

        #print(data)

        # print(data['bound'])

        # print(data['bound'])
        # print(type(data['bound'][0]))
        # print(type(data['bound'][0].vertices))
        # print(type(data['bound'][0].vertices[0].x))

        glob_data.append(data)
        length += 1

        if length > 1:
            if glob_data[length - 1][secs][0] and glob_data[length - 2][prev_time][0]:
                if glob_data[length - 1][secs][0] == glob_data[length - 2][prev_time][0]:
                    prev_file = temp
                    prev_time = secs
                else:
                    screenshot_data = {
                        "secs": secs,
                        "file": prev_file,
                        "youtube_id": "tasty"
                    }
                    notes_screenshots.append(screenshot_data)
                    prev_file = temp
                    prev_time = secs     #HERE BABY
                    # imagerino = Image.open(prev_file)
                    # imagerino.show()
        secs += 5

    # print(glob_data)
    # print("STEPHENNNNNN")
    # print(screenshot_data)

    collection_screenshots = db['screenshots']
    collection_screenshots.insert_many(notes_screenshots)



def render_doc_text(filein, fileout):
    # image = Image.open(filein)
    # print('image', image)

    # rgb_im = image.convert('RGB')

    #bounds = get_document_bounds(filein, FeatureType.PAGE)
    #draw_boxes(rgb_im, bounds, 'blue')
    #bounds = get_document_bounds(filein, FeatureType.PARA)
    #draw_boxes(rgb_im, bounds, 'red')
    bounds = get_document_bounds(filein, FeatureType.WORD)
    #draw_boxes(rgb_im, bounds, 'yellow')

    # outputs words relevant within the frame
    # if fileout is not 0:
    #     rgb_im.save(fileout)
    # else:
    #     image.show()
    return bounds


def start(fileIn, fileOut):
    bound_data = get_document_bounds(fileIn, FeatureType.WORD)
    # bound_data = render_doc_text(fileIn, fileOut)
    #print(jsonify)
    return jsonify(bound_data)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('detect_file', help='The image for text detection.')
    # parser.add_argument('-out_file', help='Optional output file', default=0)
    # args = parser.parse_args()

    # render_doc_text(args.detect_file, args.out_file)

    parser = argparse.ArgumentParser()

    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('folder', help='The image for text detection.')
    parser.add_argument('youtube_id', help='The image for text detection.')

    # parser.add_argument('try2', help='The image for text detection.')
    # parser.add_argument('try3', help='The image for text detection.')
    # parser.add_argument('try4', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    # image = Image.open(args.try1)
    get_document_bounds(args.detect_file, FeatureType.WORD, args.folder, 1)

    # image1 = Image.open(args.try2)
    # get_document_bounds(args.try2, FeatureType.WORD, 5)
    # get_document_bounds(args.try3, FeatureType.WORD, 10)
    # get_document_bounds(args.try4, FeatureType.WORD, 15)

    #print(len(glob_data))

    # render_doc_text(args.detect_file, args.out_file)
