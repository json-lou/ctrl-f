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
          @click="drawerL = !drawerL"
          color="primary"
          flat round dense
          icon="bookmark_border"
        />
      </a>
      <q-toolbar-title style="text-align: center;">
        <a href="/" class="text-primary" style="text-decoration: none;">
          CtrlF<a class="text-secondary">.mp4</a>
        </a>
      </q-toolbar-title>
      <q-btn
        @click="drawerR = !drawerR"
        color="primary"
        flat round dense
        icon="description"
      />
    </q-toolbar>
    <q-layout-drawer v-model="drawerL" side="left">
      <q-scroll-area class="fit">
        <q-list-header>Capture</q-list-header>
        <q-item v-for="pic in screenshots" :key="pic">
          <img :src="pic"/> <!-- fix later ================================== -->
        </q-item>
      </q-scroll-area>
    </q-layout-drawer>
    <q-layout-drawer v-model="drawerR" side="right">
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
  props: [ 'transcript', 'screenshots' ],
  data () {
    return {
      drawerL: true,
      drawerR: true
    }
  }
}
</script>
