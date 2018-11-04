<template>
  <div class="tag">
    <span class="badge badge-pill"
          :style="{ background: color }">
      {{name}}
    </span>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'tag',
  props: {
    api: String
  },
  data () {
    return {
      name: null,
      color: null
    }
  },
  created() {
    axios.get(this.api).then(response => {
      this.name = response.data.name
      this.color = response.data.color
    })
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
