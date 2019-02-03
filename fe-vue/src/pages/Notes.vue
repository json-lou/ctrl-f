<template>
  <q-page padding class="column justify-center">
    <notes-layout :transcript="transcript"/>
    <div class="row justify-center">
      <h5 style="margin-bottom: 10px;">results for <a class="text-secondary">{{ keyword }}</a></h5>
    </div>
    <div class="row justify-center">
      <video-player :url="url" :timestamp="timestamps[selected]" class="q-my-lg"/>
    </div>
    <!-- TIMESTAMP NAVI -->
    <div class="row justify-center items-center" style="margin-bottom: 20px;">
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
    <q-item-separator/>
    <div class="row justify-center">
      <q-search
        float-label="Try another topic"
        color="secondary"/>
    </div>
    <div class="row justify-center">
      <q-btn
        label="Ctrl+F Again"
        color="secondary"
        class="no-shadow"
        rounded push
        style="margin-top: 20px;"
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
      keyword: 'kanye',
      url: 'https://www.youtube.com/embed/biFlrzTJets',
      selected: 0,
      timestamps: [ 0, 60, 120, 180, 240, 300, 360 ], // given in seconds
      transcript: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse mollis magna libero. Donec et lobortis neque. Duis a risus ac ante tincidunt malesuada sit amet eu massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla varius lectus dictum, laoreet odio aliquam, auctor mi. Etiam vitae sem at ipsum laoreet ullamcorper. Praesent sollicitudin dui et aliquam ornare. Curabitur sagittis dui quis felis mattis suscipit. Vestibulum massa elit, consequat a posuere eget, consequat sed tellus. Aliquam aliquam augue hendrerit, tincidunt nisl vel, iaculis nulla. Sed malesuada mollis auctor. Aliquam velit ex, porttitor a mattis nec, blandit a est. Nam facilisis eget eros vel ultrices. Integer malesuada malesuada ipsum id porta. Curabitur finibus ut libero id congue. Sed suscipit laoreet dolor quis dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vitae tellus eget velit scelerisque viverra vitae convallis nunc. In ut metus vulputate neque tincidunt egestas. Donec cursus nunc pulvinar quam facilisis euismod. Aenean pharetra lacinia lacinia. Morbi efficitur tellus nec placerat fringilla. In condimentum sapien a facilisis suscipit. Mauris a odio mi. Aenean turpis tortor, mollis in turpis et, tempus ullamcorper nisl. Morbi ut placerat magna. Cras id leo leo. Fusce vulputate velit sit amet massa eleifend, sed maximus sem egestas. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc hendrerit fringilla arcu lacinia lobortis. In tristique libero est, ac ornare sapien pellentesque vitae. Fusce bibendum vehicula mauris, a fermentum leo aliquam vitae. Aliquam eu ipsum pharetra, congue odio sit amet, vulputate ante. Curabitur laoreet lectus vel consequat ullamcorper. Donec mollis metus quis augue vehicula fermentum. Etiam et efficitur nunc. Vestibulum placerat orci quis augue consequat maximus. Nunc molestie velit a accumsan pretium. Donec posuere libero urna, quis sodales diam fringilla ut. Aliquam pulvinar dapibus quam id tristique. Sed tristique faucibus molestie. Nulla aliquam tincidunt eros, ut placerat orci hendrerit et. Maecenas porta ante non pretium blandit. Fusce commodo ullamcorper laoreet. Vestibulum sagittis orci consectetur ante placerat pharetra. Morbi eget enim non ipsum hendrerit imperdiet. Mauris ut sapien nulla. In hac habitasse platea dictumst. Sed id elit a nisi lobortis scelerisque id ac metus. Aliquam accumsan, eros in faucibus maximus, nunc lectus ornare orci, nec dapibus massa lacus sit amet enim. Phasellus fermentum, risus eleifend tempus pellentesque, est tellus dictum mauris, sed hendrerit ex nisi ut urna. Pellentesque et fermentum ipsum, at tincidunt neque. Maecenas viverra, elit eu dapibus suscipit, nisl lacus rutrum magna, sit amet porttitor tortor eros a velit. Quisque non bibendum libero, sit amet scelerisque risus. Maecenas ultricies luctus pellentesque. Etiam consectetur semper lacinia. Quisque dui dui, facilisis sed justo eleifend, euismod pharetra nunc. Integer nec neque vitae eros pharetra suscipit eget a nisi. Etiam mattis at arcu ut gravida. Integer egestas pulvinar pellentesque.'
    }
  },
  methods: {
    getTimestamps () {
      // get request
      console.log('fetch timestamps')
    },
    updateSelected (i) {
      this.$data.selected = i
      console.log(this.$data.selected)
    },
    onSubmitAgain () {
      // get request with keyword, url
    }
  },
  created () { this.getTimestamps() }
}
</script>

<style>
</style>
