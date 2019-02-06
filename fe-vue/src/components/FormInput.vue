<template>
  <q-field>
    <q-search
      v-model="keywordState"
      type="text"
      float-label="Keyword"
      inverted
      class="no-shadow"
    />
    <q-input
      v-model="urlState"
      type="text"
      float-label="YouTube link"
      color="secondary"
      style="margin: 10px 0;"
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
</script>
