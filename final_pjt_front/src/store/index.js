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
    // movies: [],
    genres: {},
  },

  getters: {
  },

  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_GENRES(state, genres){
      state.genres = genres
    }

  },

  actions: {
    getMovies(context) {

      // 장르 데이터 가져옴
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genres/`
      })
      .then(res => {
        const genres = res.data
        context.commit('GET_GENRES', genres)
        console.log(genres);
      })
      

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
      .then(res => {
        // console.log(res, context)
        // context.commit('GET_MOVIES', res.data)
        // 모든 영화 데이터 가져오기
        const movies = res.data
        context.commit('GET_MOVIES', movies)
      })
      .catch(err =>
        console.log(err)
      )
    }
  },

  modules: {
  }
})
