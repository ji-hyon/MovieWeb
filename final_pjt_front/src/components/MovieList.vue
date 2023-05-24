<template>
  <!-- <div class="movie-card-container">
    <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
    </router-link>
    <div class="movie-title-container">
      <p class="movie-title">{{ movie.title }}</p>
    </div>
    <div>
      <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
    </div>
  </div> -->
  

   
      <div class="swiper-slide">
        <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
            <div class="slide-image" :style="imgUrl"></div>
        </router-link>
        <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
      </div>
  

</template>


<script>
  export default {
    name: 'MovieList',
    data(){
      return {
        imgUrl: `background-image: url(https://image.tmdb.org/t/p/w500${this.movie.poster_path})`
      }
    },
    props: {
      movie: {
        type: Object,
        required: true,
      },
    },
  }
</script>


<style scoped>
*, ::after, ::before {
  box-sizing: unset;
}

.movie-card-container {
  width: 200px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative; /* 부모 요소에 position: relative;를 추가합니다 */
}

.movie-card-container img {
  width: 100%;
}

.movie-title-container {
  display: none; /* 기본적으로 컨테이너를 숨깁니다 */
  position: absolute; /* 절대 위치로 설정하여 부모 요소에 대해 상대적인 위치를 조정합니다 */
  bottom: 0; /* 하단에 위치하도록 설정합니다 */
  left: 0; /* 좌측에 위치하도록 설정합니다 */
  width: 100%; /* 부모 요소의 너비를 가득 채우도록 설정합니다 */
  background-color: rgba(0, 0, 0, 0.7); /* 배경색을 지정합니다 */
  color: white; /* 텍스트 색상을 지정합니다 */
  padding: 5px; /* 내부 여백을 추가합니다 */
  text-align: center; /* 텍스트를 가운데 정렬합니다 */
  font-weight: bold; /* 텍스트를 두껍게 표시합니다 */
}

.movie-card-container:hover .movie-title-container {
  display: block; /* 마우스 호버 시 컨테이너를 나타나게 합니다 */
}


.movie-rating {
  font-weight: bold;
  margin-top: 10px;
  color: rgb(153, 78, 153);
}

.bi {
  color: orange;
}


</style>



<!-- <template>
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
  color: rgb(153, 78, 153);
}

.bi {
  color: orange;
}

.movie-card-container:hover{
  opacity: 1;
}
</style> -->