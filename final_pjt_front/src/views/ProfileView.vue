<template>
  <div>
    <h1>hello, {{username}}</h1>
  </div>
</template>

<script>
export default {
    name: 'ProfileView',
    computed: {
      username() {
        return this.$store.state.username;
      }
    }
}
</script>

<style>

</style>