<template>
  <div class="details">
    <div class="container">
      <h1 class="text-primary text-center">
        {{ title }}
      </h1>
      <h3>The product id is :{{this.$route.params.id}}</h3>
      <p>We should execute a query with this ID for obtains the interested data</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'details',
  data () {
    return {
      title: 'Details'
    }
  }
}
</script>
