<template>
  <div class="home">
    <h1>{{ title }}</h1>
    <div class="row">
      <div class="col-md4-col-lg4"
        v-for="(data, index) in products"
        :key="index">
          <h3 @click="goTodetail(data.id)">{{ data.title }}</h3>
      </div>
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
    goTodetail (id) {
      this.$router.push({
        name: 'details',
        params: {id: id}
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
