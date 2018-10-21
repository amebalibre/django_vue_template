<template>
  <div class="tag">
    <span class="badge badge-pill"
        v-if="id in tags && tags[id].name"
        :style="{ background: tags[id].color }">
      {{ tags[id].name }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'tag',
  props: {
    id: Number
  },
  data () {
    return {
      tags: [
        {},
        {name: 'healthy', color: 'red'},
        {name: 'realfood', color: 'hotpink'},
        {name: 'hacking', color: 'gray'},
        {name: 'pythonic'},  // load: default color
        {color: 'yellow'},  // not showed
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/const.scss';
.tag {
  span {
    // Default color
    background: darken($background-color, 15%);
  }
}
</style>
