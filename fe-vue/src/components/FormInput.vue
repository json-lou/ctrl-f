<template>
  <q-field>
    <q-input
      v-model="keyword"
      type="text"
      float-label="Keyword"
      color="secondary"/>
    <q-uploader
      v-model="videoURL"
      stack-label="Upload your lecture"
      extensions=".mp4"/>
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
      videoURL: ''
    }
  },
  methods: {
    onSubmit () {
      console.log(this.$data)
      this.$router.push('notes')
    }
  }
}
</script>

<style>
.q-input {
  margin: 10px 0;
}
</style>
