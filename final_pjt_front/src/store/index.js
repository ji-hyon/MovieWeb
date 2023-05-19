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
    movies: [],
    token: null,
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SIGN_UP(state, token) {
      state.token = token
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
      .then(res =>
        // console.log(res, context)
        context.commit('GET_MOVIES', res.data)
      )
      .catch(err =>
        console.log(err)
      )
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SIGN_UP', res.data.key)
          // context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
