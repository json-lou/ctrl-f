<template>
  <q-page padding class="column justify-center">

    <results-layout :transcript="transcript"/>

    <div v-if="timestamps.length > 0">
      <div class="row justify-center">
        <h5 style="margin-bottom: 10px;">
          Results for
          <a class="text-secondary">
            <strong>{{ this.$store.state.keyword.keywordState }}</strong>
          </a>
        </h5>
      </div>

      <!-- video player -->
      <div v-if="timestamps.length > 0" class="row justify-center">
        <video-player :timestamp="timestamps[selected]" class="q-my-lg"/>
      </div>
    </div>

    <!-- timestamp navigation -->
    <div class="row justify-center items-center">
      <!-- hide previous button if on index 0 -->
      <q-btn
        v-if="selected == 0"
        style="cursor: default;"
        class="no-shadow q-mx-md"
        color="white"
        round
      />
      <!-- show previous button -->
      <q-btn
        v-if="selected > 0"
        class="no-shadow q-mx-md"
        color="secondary"
        round push icon="navigate_before"
        @click="updateSelected(selected - 1)"
      />
      <!-- navigation buttons -->
      <q-btn
        v-for="i in timestamps.length"
        :key="i"
        class="no-shadow q-mx-sm"
        color="tertiary"
        round
        style="width: 15px; height: 15px;"
        @click="updateSelected(i - 1)"
      />
      <!-- show next button -->
      <q-btn
        v-if="selected < timestamps.length - 1"
        class="no-shadow q-mx-md"
        color="secondary"
        round push icon="navigate_next"
        @click="updateSelected(selected + 1)"
      />
      <!-- hide next button if on last index -->
      <q-btn
        v-if="timestamps.length == 1 || selected == timestamps.length - 1"
        style="cursor: default;"
        class="no-shadow q-mx-md"
        color="white"
        round
      />
    </div>

    <div class="row justify-center">
      <p v-if="timestamps.length > 0" class="text-grey">{{ selected + 1 }} of {{ timestamps.length }}</p>
      <p v-else>No keyword matches found!</p>
    </div>
  </q-page>
</template>

<script>
import VideoPlayer from '../components/VideoPlayer'
import ResultsLayout from '../components/ResultsLayout'

export default {
  name: 'NotesPage',
  components: {
    'video-player': VideoPlayer,
    'results-layout': ResultsLayout
  },
  data () {
    return {
      selected: 0,
      timestamps: [], // in seconds
      transcript: ''
    }
  },
  methods: {
    youtubeID () {
      const embed = this.$store.state.url.urlState
      if (embed === 'https://www.youtube.com/embed/84YfHc19-Jw') {
        return 'hello'
      } else if (embed === 'https://www.youtube.com/embed/3v9w79NhsfI') {
        return 'khan'
      } else if (embed === 'https://www.youtube.com/embed/Naz3lZXpNqo') {
        return 'tasty'
      }
    },
    async getTimestamps () {
      let response = await fetch('http://localhost:3001/timestamps/' + this.youtubeID() + '/' + this.$store.state.keyword.keywordState)
      let jsonData = await response.json()
      this.$data.timestamps = jsonData
      console.log('Timestamps', this.$data.timestamps)
    },
    async getTranscript () {
      let response = await fetch('http://localhost:3001/transcripts/' + this.youtubeID() + '/')
      let jsonData = await response.json()
      this.$data.transcript = jsonData
      console.log('Transcript', this.$data.transcript)
    },
    updateSelected (i) {
      this.$data.selected = i
    }
  },
  created () {
    this.getTimestamps()
    this.getTranscript()
  },
  computed: {
    keywordState: {
      get () { return this.$store.state.keyword.keywordState }
    }
  }
}
</script>
