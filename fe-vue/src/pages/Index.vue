<template>
  <q-page padding class="flex flex-center">
    <div class="container fill" style="width: 70vh; max-height: 100vh; text-align: center;">
      <h1 class="q-ma-none">
        CtrlF<a class="text-secondary">.mp4</a></h1>
      <h5>Want to only watch the key points of your lecture? Ctrl+F through your lecture video!</h5>
      <form-input/>
    </div>
  </q-page>
</template>

<script>
import FormInput from '../components/FormInput'

export default {
  name: 'IndexPage',
  components: {
    'form-input': FormInput
  }
}
</script>
