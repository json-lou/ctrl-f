<template>
  <q-page padding class="column justify-center">
    <notes-layout :transcript="transcript"/>
    <div class="row justify-center">
      <h5 style="margin-bottom: 10px;">results for <a class="text-secondary">{{ query }}</a></h5>
    </div>
    <div class="row justify-center">
      <video-player :url="url" :timestamp="timestamps[selected]" class="q-my-lg"/>
    </div>
    <!-- TIMESTAMP NAVI -->
    <div class="row justify-center items-center">
      <q-btn
        v-if="selected == 0"
        style="cursor: default;"
        class="no-shadow q-mx-md"
        color="white"
        round/>
      <q-btn
        v-if="selected > 0"
        class="no-shadow q-mx-md"
        color="secondary"
        round push icon="navigate_before"
        @click="updateSelected(selected - 1)"/>
      <q-btn
        v-for="i in timestamps.length"
        :key="i"
        class="no-shadow q-mx-sm"
        color="tertiary"
        round
        style="width: 15px; height: 15px;"
        @click="updateSelected(i - 1)"/>
      <q-btn
        v-if="selected < timestamps.length - 1"
        class="no-shadow q-mx-md"
        color="secondary"
        round push icon="navigate_next"
        @click="updateSelected(selected + 1)"/>
    </div>
    <div class="row justify-center">
      <p v-if="timestamps.length > 0" class="text-grey">{{ selected }} of {{ timestamps.length }}</p>
      <p v-else>No keyword matches found!</p>
    </div>
    <q-item-separator/>

    <div class="row justify-center">
      <h5>Explore</h5>
    </div>
    <div class="row justify-center" style="margin-bottom: 10px;">
      <q-btn
        v-for="suggestion in suggestions"
        :key="suggestion"
        :label="suggestion"
        color="secondary"
        class="no-shadow q-mx-xs"
        outline rounded/>
    </div>
    <div class="row justify-center">
      <q-search
        float-label="Try another topic"
        class="no-shadow"
        style="width: 500px; height:60px; margin-top: 20px;"
        inverted/>
    </div>
    <div class="row justify-center">
      <q-btn
        label="Ctrl+F"
        color="secondary"
        class="no-shadow"
        rounded push
        style="margin-top: 30px;"
        size="lg"
        @click="onSubmitAgain"
      />
    </div>
  </q-page>
</template>

<script>
import VideoPlayer from '../components/VideoPlayer'
import NotesLayout from '../components/NotesLayout'

export default {
  name: 'NotesPage',
  components: {
    'video-player': VideoPlayer,
    'notes-layout': NotesLayout
  },
  data () {
    return {
      query: 'financial',
      url: 'https://www.youtube.com/embed/biFlrzTJets',
      selected: 0,
      timestamps: [], // given in seconds
      transcript: '',
      suggestions: []
    }
  },
  methods: {
    async getTimestamps () {
      // get request
      let response = await fetch('http://localhost:3001/timestamps/' + 'hello/' + this.$data.query)
      let jsonData = await response.json()
      this.$data.timestamps = jsonData
      console.log('Timestamps', this.$data.timestamps)
    },
    async getTranscript () {
      let response = await fetch('http://localhost:3001/transcripts/' + 'hello/')
      let jsonData = await response.json()
      this.$data.transcript = jsonData
      console.log('Transcript', this.$data.transcript)
      // let jsonData = await response.json()
      // this.$data.transcript = jsonData
      // console.log('Transcript', this.$data.transcript)
    },
    updateSelected (i) {
      this.$data.selected = i
      console.log(this.$data.selected)
    },
    onSubmitAgain () {
      // get request with keyword, url
    }
  },
  created () {
    this.getTimestamps()
    this.getTranscript()
  }
}
</script>

<style>
</style>
