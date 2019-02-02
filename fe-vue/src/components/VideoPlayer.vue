<template>
  <div class="q-video">
    <iframe
      style="width: 853px; height: 480px;"
      :src="url + '?start=' + timestamp"
      frameborder="0"
      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture">
    </iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoPlayer',
  props: [ 'url', 'timestamp' ]
}
</script>
