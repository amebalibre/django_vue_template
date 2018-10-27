<template>
  <div class="tag">
    <span class="badge badge-pill"
        :style="{ background: color }">
      {{ name }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'tag',
  props: {
    name: String,
    color: String
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
