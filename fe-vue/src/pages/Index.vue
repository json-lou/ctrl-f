<template>
  <q-page class="flex flex-center">
    <div style="width: 500px; height: 100vh; text-align: center;">
      <h1 style="margin-top: 150px; margin-bottom: 0;">
        CtrlF<a class="text-secondary">.</a>mp4</h1>
      <h5>Want to only watch the key points of your lecture? Ctrl+F through your lecture video!</h5>
      <form-input/>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import FormInput from '../components/FormInput'

export default {
  name: 'IndexPage',
  components: {
    'form-input': FormInput
  }
}
</script>
