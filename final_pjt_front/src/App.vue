<template>
  <div id="app">
    <nav>
      <!-- 수정 테스트 -->
      <router-link v-bind:to="{name: 'MainView'}" class="nav-link">Main</router-link> 
      <router-link v-bind:to="{name: 'RecommendationView'}" class="nav-link">Recommendation</router-link> 
      <template v-if="isNotLogin">
        <router-link v-bind:to="{name: 'SignInView'}" class="nav-link">SignIn</router-link> 
        <router-link v-bind:to="{name: 'SignUpView'}" class="nav-link">SignUp</router-link>
      </template>
      <template v-if="isLogin">
        <a v-on:click="signOut" style="text-decoration: underline;" class="nav-link">SignOut</a> 
        <router-link v-bind:to="{name: 'ProfileView'}" class="nav-link">Profile</router-link>
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
  background-image: url(./assets/pastel.png); 
  background-repeat: no-repeat;
  background-size: cover;
  text-align: right;
}

.nav-link {
  display: inline-block;
  margin-right: 50px;
  font-weight: bold;
  color: #f2f4f5;
  text-decoration: none;
  font-size: 18px
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
