<template>
  <div class="blog">
    <h1>{{ title }}</h1>
    <post/>
</div>
</template>

<script>
import Post from '@/components/Post.vue'
export default {
  name: 'Blog',
  components: {
    Post
  },
  data () {
    return {
      results: [],
      title: 'Blog',
      tags: []
    }
  }
}
</script>

<style lang="scss" scoped>
  // @import '@/assets/style/const.scss';
</style>
