<template>
  <div class="blog">
    <h1>{{ title }}</h1>
    <Tags :tags="tags"/>
</div>
</template>

<script>
import Tags from '@/components/Tags.vue'
import axios from 'axios'
export default {
  name: 'Blog',
  components: {
    Tags
  },
  data () {
    return {
      results: [],
      title: 'Blog',
      tags: []
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/blog/tags/').then(response => {
      this.results = response.data
      this.tags = response.data.results
    })
  }
}
</script>

<style lang="scss" scoped>
  // @import '@/assets/style/const.scss';
</style>
