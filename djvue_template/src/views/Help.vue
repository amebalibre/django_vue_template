<template>
  <div class="help">
    <img alt="Vue logo" src="@/assets/img/logo.png">
    <Help msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Help from '@/components/Help.vue'

export default {
  name: 'help',
  components: {
    Help
  }
}
</script>
