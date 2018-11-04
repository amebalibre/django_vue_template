<template>
  <div class="tags">
    <div class="list-group"
         v-for="(value, index) in tags"
         :key="index">
      <tag :name="value.name" :color="value.color"/>
    </div>
</div>
</template>

<script>
import Tag from '@/components/Tag.vue'
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
