<template>
<div id="app">
  <nav class="navbar navbar-expand-lg navbar-light">
    <strong><router-link class="navbar-brand" to="/">Home</router-link></strong>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <!-- <li class="nav-item active">
          <a class="nav-link" href="#">HomeX <span class="sr-only">(current)</span></a>
        </li> -->
        <li class="nav-item">
          <router-link class="nav-link" to="/blog">Blog</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/contact">Contact</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link disabled" to="/help">Help</router-link>
        </li>
      </ul>
    </div>
  </nav>
  <router-view/>
</div>
</template>

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

  .navbar {
    background-color: $navbar-color;
    .navbar-brand, .nav-link {
      color: $font-color;
    }
  }

</style>

<style lang="scss" scoped>
  .navbar {
    margin-bottom: 1.4em;
  }
</style>
