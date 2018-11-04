<template>
  <div class="post container">

    <!-- POST: COMPRESSED -->
  <div v-if="data.results" class="row">
    <div v-for="(post, index) in data.results"
         :key="index"
         class="col-sm-4">
      <div class="card">
        <!-- <img class="card-img-top" src="{{post.image}} cap" alt="Card image cap"> -->
        <div class="card-body">
          <h5 class="card-title">{{ post.title }}</h5>
          <p class="card-text">{{ post.content }}</p>
        </div>
        <div class="card-body">
          <tags :tags="post.tags"/>
        </div>
      </div>
    </div>
  </div>

  <!-- POST: EXPANDED -->
  <div v-else class="card">
    <!-- <img class="card-img-top" src=".../100px180/?text=Image cap" alt="Card image cap"> -->
    <div class="card-body">
      <h5 class="card-title">{{ data.title }}</h5>
      <p class="card-text">{{ data.content }}</p>
    </div>
    <div class="card-body">
      <tags :tags="data.tags"/>
    </div>
  </div>

</div>
</template>

<script>
import Tags from '@/components/Tags.vue'
import axios from 'axios'
export default {
  name: 'Post',
  components: {
    Tags
  },
  data () {
    return {
      data: [],
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/blog/posts/').then(response => {
      this.data = response.data
    })
  }
}
</script>

<style lang="scss" scoped>
  // @import '@/assets/style/const.scss';
</style>
