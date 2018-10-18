<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-link class="nav-link" to="/">Products</router-link>
    <router-link class="nav-link" to="/blog">Blog</router-link>
    <router-link class="nav-link" to="/contact">Contact</router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}
</style>
