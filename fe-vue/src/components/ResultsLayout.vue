<template>
  <div>
    <q-toolbar
      color="white"
      style="border-bottom: solid;
             border-color: lightgrey;
             border-width: 0.5px;
             position: absolute;
             top: 0; left: 0;"
    >
      <q-btn
        @click="drawerL = !drawerL"
        color="primary"
        flat round dense
        icon="bookmark_border"
      />
      <q-toolbar-title style="text-align: center;">
        <a href="/" class="text-primary" style="text-decoration: none;">
          Ctrl-F
        </a>
      </q-toolbar-title>
      <q-btn
        @click="drawerR = !drawerR"
        color="primary"
        flat round dense
        icon="description"
      />
    </q-toolbar>

    <!-- left drawer (screenshots) -->
    <q-layout-drawer v-model="drawerL" side="left">
      <q-scroll-area class="fit">
        <q-list-header>Capture</q-list-header>
        <q-item v-for="pic in screenshots" :key="pic">
          <img class="container fit" :src="'../assets' + pic"/>
        </q-item>
      </q-scroll-area>
    </q-layout-drawer>

    <!-- right drawer (transcript) -->
    <q-layout-drawer v-model="drawerR" side="right">
      <q-scroll-area class="fit">
        <q-list-header>Transcript</q-list-header>
        <q-item>
          <p>{{ transcript }}</p>
        </q-item>
      </q-scroll-area>
    </q-layout-drawer>
  </div>
</template>

<script>
export default {
  name: 'NotesLayout',
  props: [ 'transcript' ],
  data () {
    return {
      drawerL: true,
      drawerR: true,
      screenshots: []
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
    async getScreenshots () {
      let response = await fetch('http://localhost:3001/screenshots/' + this.youtubeID())
      let jsonData = await response.json()
      this.$data.screenshots = jsonData
    }
  },
  created () {
    this.getScreenshots()
  }
}
</script>
