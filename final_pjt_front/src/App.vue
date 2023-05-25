<template>
<!-- 활성화되지 않았을 때도 색칠해지는 문제 해결 -->
  <!-- <div id="app">
    <nav>
      <router-link v-bind:to="{name: 'MainView'}" class="nav-link" active-class="active-link">Main</router-link> 
      <router-link v-bind:to="{name: 'RecommendationView'}" class="nav-link" active-class="active-link">Recommendation</router-link> 
      <template v-if="isNotLogin">
        <router-link v-bind:to="{name: 'SignInView'}" class="nav-link" active-class="active-link">SignIn</router-link> 
      </template>
      <template v-if="isLogin">
        <a v-on:click="signOut" class="nav-link">SignOut</a> 
        <router-link v-bind:to="{name: 'ProfileView', params:{username: this.$store.state.username}}" class="nav-link">Profile</router-link>
      </template>
      <router-link v-bind:to="{name: 'SearchView'}" class="nav-link" active-class="active-link">Search</router-link> 
    </nav>
      <router-view/>
  </div> -->

  <div id="app">
    <nav>
    <div class="d-flex justify-content-between">
      <div class="nav-left">
        <!-- <img class="icon" src= "./assets/icon.png" alt=""> -->
        <!-- <img class="icon" src= "./assets/char.webp" alt=""> -->
        <div>
          <p class="letter mb-0">Purple Cinema</p>
        <img class="icon" src= "./assets/penguin.png" alt="">
      </div>
      </div>

      <div class="nav-right">
        <router-link v-bind:to="{name: 'MainView'}" class="nav-link" :class="{ 'active-link': $route.name === 'MainView' }">Main</router-link> 
        <router-link v-bind:to="{name: 'RecommendationView'}" class="nav-link" :class="{ 'active-link': $route.name === 'RecommendationView' }">Recommendation</router-link> 
        <template v-if="isNotLogin">
          <router-link v-bind:to="{name: 'SignInView'}" class="nav-link" :class="{ 'active-link': $route.name === 'SignInView' }">SignIn</router-link> 
        </template>
        <template v-if="isLogin">
          <a v-on:click="signOut" class="nav-link">SignOut</a> 
          <router-link v-bind:to="{name: 'ProfileView', params:{username: this.$store.state.username}}" class="nav-link" :class="{ 'active-link': $route.name === 'ProfileView' }">Profile</router-link>
        </template>
        <router-link v-bind:to="{name: 'SearchView'}" class="nav-link" :class="{ 'active-link': $route.name === 'SearchView' }">Search</router-link> 
      </div>
    </div>
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
.letter {
  font-family: 'IBM Plex Sans KR', sans-serif;
  color: purple;
  margin-left: 10px;
  font-weight: bold;
}

.nav-left {
  padding-top: 30px;
  /* margin: 0 auto; */
}


.nav-right {
  margin-top: 40px;
}

.icon {
  width: 50px
}

.router-view {
  width: 100%;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-family: 'IBM Plex Sans KR', sans-serif;
  width: 80%;
}

nav {
  display: block;
  width: 100%;
  /* padding: 30px; */
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
