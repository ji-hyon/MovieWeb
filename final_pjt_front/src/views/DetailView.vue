<template>
  <div>
     <p>디테일 페이지</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DetailView',
    created() {
        this.getMovieDetail()
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