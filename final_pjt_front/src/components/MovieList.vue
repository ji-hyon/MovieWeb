<template>
    <div class="movie-card-container">

      <div class="movie-image">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
      </div>

      <div class="movie-info">
        <!-- <p>{{ movie.genre_ids }}</p> -->
        <h2>{{ movie.title }}</h2>
        <button class="btn btn-primary">
          <router-link
            :to="{
              name: 'DetailView',
              params: { id: movie.id }
            }"
            >
            <p class="btn_letter">Detail</p>
          </router-link>
        </button>
        <!-- <p class="movie-overview">{{ movie.overview }}</p> -->
        <!-- <p class="movie-release-date">{{ movie.release_date }}</p> -->
        <div>
          <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
        </div>
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
  width: 300px;
  margin: 20px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.movie-image {
  width: 100%;
  height: 0;
  padding-top: 150%; /* 이미지의 측면 비율을 2:3으로 유지하기 위한 값을 설정 */
  position: relative;
}

.movie-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.movie-info {
  padding: 20px;
  text-align: center;
}

.movie-info p,
.movie-info h2 {
  margin: 0;
}

.movie-info h2 {
  margin-top: 10px;
}

.movie-info router-link {
  display: inline-block;
  margin-top: 10px;
}

.movie-rating {
  font-weight: bold;
  margin-top: 10px;
}

.bi {
  color: orange;
}

.btn_letter {
  color: aliceblue;
}

/* .btn {
  background-color: rgb(188, 238, 241);
} */
</style>
