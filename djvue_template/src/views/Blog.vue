<template>
  <div class="blog">
    <h1>{{ title }}</h1>
    <Tags :ids="[1, 2, 3, 4, 5]"/>
</div>
</template>

<script>
import Tags from '@/components/Tags.vue'
export default {
  name: 'blog',
  components: {
    Tags
  },
  data () {
    return {
      title: 'Microblog'
    }
  }
}
</script>

<style lang="scss" scoped>
  // @import '@/assets/style/const.scss';
</style>
