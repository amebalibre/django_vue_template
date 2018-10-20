<template>
  <div class="blog">
    <h1>{{ title }}</h1>
  </div>
</template>

<script>
export default {
  name: 'blog',
  data () {
    return {
      title: 'Microblog'
    }
  }
}
</script>

<style lang="scss" scoped>
  // @import './assets/style/const.scss';
</style>
