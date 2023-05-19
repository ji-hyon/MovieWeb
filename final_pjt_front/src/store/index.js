import Vue from 'vue'
import Vuex from 'vuex'
//
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [
      {
        id: 1,
        title: '제목',
        content: '내용',
      }
    ]
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`
      })
      .then(res =>
        console.log(res, context)
      )
      .catch(err =>
        console.log(err)
      )
    }
  },
  modules: {
  }
})
