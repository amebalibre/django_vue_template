<template>
  <div class="contact">
    <h1>{{ contact }}</h1>
    <div class="card" style="width: 30rem; margin: 0 auto;">
      <div class="container">
        <img class="card-img-top col-sm-6"
            src="https://avatars2.githubusercontent.com/u/4262423?s=400&v=4"
            alt="Card image cap"
            style="margin-top: 20px">
      </div>
  <div class="card-body">
    <h5 class="card-title">Amebalibre</h5>
    <p class="card-text">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
      ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
      ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
      reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
      sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
      est laborum.
    </p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">
      <div class="card-body">
        <a href="https://github.com/amebalibre" class="card-link">Profile</a>
        <a href="https://github.com/amebalibre/django_vue_template/issues" class="card-link">Issues</a>
      </div>
    </li>
  </ul>
</div>
  </div>
</template>

<script>
export default {
  name: 'contact',
  data () {
    return {
      contact: 'Developer info'
    }
  }
}
</script>

<style lang="scss" scoped>
  // @import './assets/style/const.scss';
</style>
