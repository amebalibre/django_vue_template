<template>
  <div class="home">
    <div class="container">
      <h1>{{ title }}</h1>

      <ul class="list-group"
          v-for="(data, index) in products"
          :key="index">
        <li class="list-group-item" @click="goTodetail(data.id, data.title)">{{ data.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      title: 'Home',
      products: [
        {
          id: '1',
          title: 'Cocoa'
        },
        {
          id: '2',
          title: 'Banana'
        },
        {
          id: '3',
          title: 'Onion'
        },
        {
          id: '4',
          title: 'Pineaple'
        }
      ]
    }
  },
  methods: {
    goTodetail (id, title) {
      this.$router.push({
        name: 'details',
        params: {id: id, name: title}
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  // @import './assets/style/const.scss';
</style>
