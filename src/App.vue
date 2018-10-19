<template>
<div id="app">
  <ul class="nav header-nav">
    <li class="nav-item"><router-link class="nav-link" to="/">Products</router-link></li>
    <li class="nav-item"><router-link class="nav-link" to="/blog">Blog</router-link></li>
    <li class="nav-item"><router-link class="nav-link" to="/contact">Contact</router-link></li>
  </ul>
  <router-view/>
</div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
  @import './assets/style/const.scss';

  body {
    background-color: $background-color !important;
    color: $font-color !important;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: ·$font-color;
  }
  .container {
    color: $font-color;
  }

  .nav {
    background-color: $navbar-color;
    .nav-link {
      color: $font-color;
    }
  }

</style>

<style lang="scss" scoped>
  .nav {
    margin-bottom: 1.4em;
  }
</style>
