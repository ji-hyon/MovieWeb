<!-- <template>
  <div>
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
  </div>
</template>

<script>
export default {
    name : 'RecommendedMovie',
    props: {
      movie: {
          type: Object,
          required: true,
      },
    },
}
</script>

<style>

</style>

 -->

 <template>
    <img class="img" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" @click="goToDetailMovie" />
</template>

<script>
export default {
  name: 'RecommendedMovie',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goToDetailMovie() {
      this.$router.push({ name: 'DetailView', params: { id : this.movie.id } });
    },
  },
};
</script>

<style scoped>
.img {
  margin-top: 20px;
  margin-bottom:70px;
  margin-left: 10px;
  height: 600px;

  background-color:skyblue;
  left:300px;
  animation:ani 1s infinite alternate;  
}

@keyframes ani{
   0%{transform:translate(0,0);}
   100%{transform:translate(0,50px);}
}  
</style>
