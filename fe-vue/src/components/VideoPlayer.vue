<template>
  <div class="q-video">
    <iframe
      style="width: 853px; height: 480px;"
      :src="url + '?start=' + timestamp + '&autoplay=1'"
      frameborder="0"
      allow="autoplay; accelerometer; encrypted-media; gyroscope; picture-in-picture">
    </iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoPlayer',
  props: [ 'url', 'timestamp' ]
}
</script>
