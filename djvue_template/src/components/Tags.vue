<template>
  <div class="blog">
    <div class="list-group"
        v-for="id in ids"
        :key="id">
        <Tag :id="id"/>
    </div>
</div>
</template>

<script>
import Tag from '@/components/Tag.vue'
export default {
  name: 'tags',
  props: {
    ids: Array,
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
