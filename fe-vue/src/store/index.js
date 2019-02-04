import Vue from 'vue'
import Vuex from 'vuex'

import keyword from './keyword'
import url from './url'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: { keyword, url }
})

export default store
