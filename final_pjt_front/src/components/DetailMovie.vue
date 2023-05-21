<template>
  <div>
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
     <h1>{{ movie.title }}</h1>
     <p>{{ movie.overview }}</p>
     <p>{{ movie.vote_average }}</p>
  </div>
</template>

<script>
export default {
    name : 'DetailMovie',
    props: {
      movie : Object
        // movie: {
            // type: Object,
            // required: true,
    // },
  },
}
</script>

<style>

</style>