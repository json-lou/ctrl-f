<template>
  <q-page padding class="flex flex-center">
    <div class="container fill"
         style="width: 70vh; max-height: 100vh; text-align: center;">
      <h1 class="q-ma-none">Ctrl-F</h1>
      <h5>Want to only watch the important parts of your video? Enter your keywords below!</h5>
      <form-input/>
    </div>
  </q-page>
</template>

<script>
import FormInput from '../components/FormInput'

export default {
  name: 'IndexPage',
  meta: {
    title: 'Ctrl-F'
  },
  components: {
    'form-input': FormInput
  }
}
</script>
