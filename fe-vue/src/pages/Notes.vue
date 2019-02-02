<template>
  <q-page class="flex flex-center column">
      <q-toolbar
        color="white"
        style="border-bottom: solid;
               border-color: lightgrey;
               border-width: 0.5px;
               position: absolute;
               top: 0;
               left: 0;">
        <q-toolbar-title class="text-primary" style="text-align: center;">
          CtrlF.mp4
      </q-toolbar-title>
    </q-toolbar>
    <video-player :url="url" :timestamp="timestamps[selected]" style="margin-bottom: 50px;"/>

    <!-- TIMESTAMP NAVI -->
    <div>
      <!-- last -->
      <q-btn
        v-if="selected > 0"
        class="no-shadow q-mx-md"
        color="secondary"
        round icon="navigate_before"
        @click="updateSelected(selected - 1)"/>
      <!-- navigate to i -->
      <q-btn
        v-for="i in timestamps.length"
        :key="i"
        class="no-shadow q-mx-sm"
        color="tertiary"
        round
        style="width: 15px; height: 15px;"
        @click="updateSelected(i)"/>
      <!-- next -->
      <q-btn
        v-if="selected < timestamps[timestamps.length - 1]"
        class="no-shadow q-mx-md"
        color="secondary"
        round icon="navigate_next"
        @click="updateSelected(selected + 1)"/>
    </div>
  </q-page>
</template>

<script>
import VideoPlayer from '../components/VideoPlayer'

export default {
  name: 'NotesPage',
  components: {
    'video-player': VideoPlayer
  },
  data () {
    return {
      url: 'https://www.youtube.com/embed/biFlrzTJets',
      selected: 0,
      timestamps: [ 0, 60, 120, 180, 240, 300, 360 ] // given in seconds
    }
  },
  methods: {
    getTimestamps () {
      // fetch request
      console.log('fetch timestamps')
    },
    updateSelected (i) {
      this.$data.selected = i
      console.log(this.$data.selected)
    }
  },
  created () { this.getTimestamps() }
}
</script>

<style>
</style>
