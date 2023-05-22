<template>
  <div class="movie-card-container">
      <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
      </router-link>
      <div>
        <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
      </div>
  </div>
</template>

<script>
export default {

  name: 'MovieList',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style>
.movie-card-container {
  width: 200px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.movie-card-container img {
  width: 100%; /* 이미지의 너비를 100%로 설정하여 부모 요소와 동일한 너비를 가지게 합니다 */
}

.movie-rating {
  font-weight: bold;
  margin-top: 10px;
}

.bi {
  color: orange;
}
</style>
