<template>
  <div>
    <p>랜덤페이지입니다</p>
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