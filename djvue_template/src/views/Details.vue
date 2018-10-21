<template>
  <div class="details">

    <h1>{{ title }}</h1>
    <div class="card" style="width: 18rem; margin: 0 auto;">
      <div class="card-body">
        <h5 class="card-title">{{this.$route.params.name}}</h5>
        <h6 class="card-subtitle mb-2 text-muted">
          The product id is: {{this.$route.params.id}}
        </h6>
        <p class="card-text">
          We should execute a query with this ID for obtains the interested data.
        </p>
      </div>
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

<style lang="scss" scoped>
// @import '@/assets/style/const.scss';
</style>
