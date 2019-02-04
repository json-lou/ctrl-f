<template>
  <q-field>
    <q-search
      v-model="keywordState"
      type="text"
      float-label="Keyword"
      inverted
      class="no-shadow"/>
    <q-input
      v-model="urlState"
      type="text"
      float-label="YouTube link"
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
  methods: {
    onSubmit () {
      this.$router.push('results')
    }
  },
  computed: {
    keywordState: {
      get () { return this.$store.state.keyword.keywordState },
      set (val) { this.$store.commit('keyword/updateKeywordState', val) }
    },
    urlState: {
      get () { return this.$store.state.url.urlState },
      set (val) { this.$store.commit('url/updateUrlState', val) }
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
