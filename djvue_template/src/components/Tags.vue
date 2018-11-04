<template>
  <div class="tags">
    <div class="list-group"
         v-for="(value, index) in tags"
         :key="index">
      <tag :api="value"/>
    </div>
</div>
</template>

<script>
import Tag from '@/components/Tag.vue'
// import axios from 'axios'
export default {
  name: 'tags',
  props: {
    tags: Array,
  },
  components: {
    Tag
  }
}
</script>

<style lang="scss" scoped>
div {
  display: inline;
  margin-left: 1px;
}
</style>
