import Vue from 'vue'
import Vuex from 'vuex'

// we first import the module
import info from './info'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    info
  }
})

export default store
