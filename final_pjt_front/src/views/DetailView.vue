<template>
  <div>
    <DetailMovie :movie = movies[movieId] />
  </div>
</template>

<script>
import axios from 'axios'
import DetailMovie from '@/components/DetailMovie.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DetailView',
    components: {
      DetailMovie,
    },
    created() {
        this.getMovieDetail()
    },
    data() {
        return {
            movieId : this.$route.params.id - 1
        }
    },
    computed: {
        movies() {
            return this.$store.state.movies
        }
    },
    methods: {
        getMovieDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
            })
            .then((res) => {
                console.log(res);
            })
            .catch(err => console.log(err))
        }
    }
}
</script>

<style>

</style>