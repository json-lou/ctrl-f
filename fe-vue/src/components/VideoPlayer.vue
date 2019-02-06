<template>
  <div class="q-video">
    <iframe
      style="width: 682px; height: 384px;"
      :src="urlState + '?start=' + timestamp + '&autoplay=1'"
      frameborder="0"
      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
    />
  </div>
</template>

<script>
export default {
  name: 'VideoPlayer',
  props: [ 'timestamp' ],
  computed: {
    urlState: {
      get () { return this.$store.state.url.urlState }
    }
  }
}
</script>
