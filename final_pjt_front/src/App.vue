<template>
  <div id="app">
    <nav>
      <!-- 수정 테스트 -->
      <router-link v-bind:to="{name: 'MainView'}">Main</router-link> |
      <router-link v-bind:to="{name: 'RecommendationView'}">Recommendation</router-link> |
      <template v-if="isNotLogin">
        <router-link v-bind:to="{name: 'SignInView'}">SignIn</router-link> |
        <router-link v-bind:to="{name: 'SignUpView'}">SignUp</router-link>
      </template>
      <template v-if="isLogin">
        <a v-on:click="signOut" style="text-decoration: underline;">SignOut</a> |
        <router-link v-bind:to="{name: 'ProfileView'}">Profile</router-link>
      </template>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    isNotLogin() {
      return this.$store.getters.isNotLogin
    },
  },

  methods: {
    signOut() {
      this.$store.dispatch('signOut')
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}


body {
  background-image: url(./assets/bg3_.jpg);
  background-repeat: repeat;
  width: 100%;
  height: 100%;
  background-repeat: repeat-y;
  /* background-size: cover; */
}

</style>
