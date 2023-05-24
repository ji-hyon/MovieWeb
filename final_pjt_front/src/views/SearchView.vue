<template>
<div>
  <div class="search">
    <input class="textarea" v-model="searchQuery" placeholder="영화 제목을 입력하세요" />
    <button class="w-btn w-btn-gra1" @click="searchMovies">검색</button>
  </div>

    <div class="no" v-if="searchResults.length === 0">
      검색 결과가 없습니다.
    </div>

    <div v-else  class="image-container">
      <div v-for="movie in searchResults" :key="movie.id" class="movie">
        <div class="title">{{ movie.title }}</div>
        <div class="poster-container">
          <img class="img" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchView",

    data() {
    return {
      searchQuery: '',
      searchResults: [],
    };
  },

  watch: {
    searchQuery(newValue) {
      this.searchMovies(newValue);
    },
  },


  methods: {
    searchMovies() {
      // 영화 검색 API 호출 등의 로직을 수행합니다.
      // 검색 결과를 searchResults에 할당합니다.
      // 이 예시에서는 store에 저장된 movies에서 검색을 수행합니다.
      this.searchResults = this.$store.state.movies.filter((movie) =>
        movie.title.includes(this.searchQuery)
      );
    },
  },

}
</script>

<style scoped>
.title {
  font-size: 25px;
}

.no {
  color: rgb(196, 104, 196);
}

.search {
  
  margin: 40px;
}

.w-btn-gra1 {
    background: linear-gradient(-45deg, #33ccff 0%, #ff99cc 100%);
    color: white;
    border-radius: 10px;
    border-color: rgb(196, 104, 196);
    padding: 15px;
    margin: 5px;
    display: inline;
}

.textarea {
    border-radius: 10px;
    border: 2px solid rgb(196, 104, 196);
    display: inline;
    margin: 7px;
    vertical-align: middle;
    text-align: center;
    padding: 15px;
}

.image-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
}

.movie {
  margin: 20px;
  text-align: center;
  width: 300px;
}

</style>