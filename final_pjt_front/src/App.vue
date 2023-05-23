<template>
  <div id="app">
    <nav>
      <router-link v-bind:to="{name: 'MainView'}" class="nav-link" active-class="active-link">Main</router-link> 
      <router-link v-bind:to="{name: 'RecommendationView'}" class="nav-link" active-class="active-link">Recommendation</router-link> 
      <template v-if="isNotLogin">
        <router-link v-bind:to="{name: 'SignInView'}" class="nav-link" active-class="active-link">SignIn</router-link> 
        <router-link v-bind:to="{name: 'SignUpView'}" class="nav-link" active-class="active-link">SignUp</router-link>
      </template>
      <template v-if="isLogin">
        <a v-on:click="signOut" class="nav-link">SignOut</a> 
        <router-link v-bind:to="{name: 'ProfileView', params:{username: this.$store.state.username}}" class="nav-link">Profile</router-link>
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

.nav-link:hover, .nav-link.active-link {
  color: purple;
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
