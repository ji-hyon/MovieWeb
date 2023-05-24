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
  <div>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" @click="goToDetailMovie" />
  </div>
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

<style>
</style>
