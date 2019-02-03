<template>
  <div>
    <q-toolbar
      color="white"
      style="border-bottom: solid;
             border-color: lightgrey;
             border-width: 0.5px;
             position: absolute;
             top: 0; left: 0;">

      <a href="https://github.com/json-lou/qhacks-2019" target="_blank">
        <q-btn
          color="primary"
          flat round dense
          icon="description"
        />
      </a>
      <q-toolbar-title style="text-align: center;">
        <a href="/" class="text-primary" style="text-decoration: none;">
          CtrlF<a class="text-secondary">.mp4</a>
        </a>
      </q-toolbar-title>
      <q-btn
        @click="drawer = !drawer"
        color="primary"
        flat round dense
        icon="menu"
      />
    </q-toolbar>
    <q-layout-drawer v-model="drawer" side="right">
      <q-scroll-area class="fit">
        <q-list-header>Transcript</q-list-header>
        <q-item>
          <p>{{ transcript }}</p>
        </q-item>
      </q-scroll-area>
    </q-layout-drawer>
  </div>
</template>

<script>
export default {
  name: 'NotesLayout',
  props: [ 'transcript' ],
  data () {
    return {
      drawer: true
    }
  }
}
</script>
