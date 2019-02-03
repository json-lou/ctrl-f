<template>
  <div class="q-video">
    <iframe
      style="width: 682px; height: 384px;"
      :src="url + '?start=' + timestamp + '&autoplay=1'"
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
