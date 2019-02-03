<template>
  <q-field>
    <q-search
      v-model="keyword"
      type="text"
      float-label="Keyword"
      inverted
      class="no-shadow"/>
    <q-input
      v-model="videoURL"
      type="text"
      float-label="Youtube link"
      color="secondary"
      style="margin: 10px 0;"/>
    <q-btn
      label="Ctrl+F"
      color="secondary"
      class="no-shadow"
      size="lg"
      rounded push
      style="margin-top: 40px;"
      @click="onSubmit"
    />
  </q-field>
</template>

<script>

export default {
  name: 'FormComponent',
  data () {
    return {
      keyword: '',
      videoURL: '' // embeded youtube url for now
    }
  },
  methods: {
    onSubmit () {
      console.log(this.$data)
      // post request
      // let res = getYoutubeId('http://www.youtube.com/watch?v=zbYf5_S7oJo')
      // console.log(res)
      this.$router.push('notes')
    }
  }
}

// function getYouTubeID (url) {
//   var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/
//   var match = url.match(regExp)

//   if (match && match[2].length === 11) {
//     return match[2]
//   } else {
//     return 'error'
//   }
// }
</script>
