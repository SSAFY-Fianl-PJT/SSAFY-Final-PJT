<template>
  <div>
    <div class="Reive-page-title">
      <h3>영화 리뷰</h3>
    </div>
    <hr class="hr-1">
    
    <div v-if="Array.isArray(get_review) && get_review.length > 0">
      <!-- 리뷰가 있을 때에만 표시되는 내용 -->
      <ArticleList :articles="get_review"/>
    </div>
    <div v-else>
      <!-- 리뷰가 없을 때에만 표시되는 내용 -->
      {{ get_review.message }}
    </div>

  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  props:{
    movie_id: {
      type: Number, 
      required: true 
    }
  },
  data() {
    return {
      reviews: [] // 독립적인 리뷰 데이터
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    get_review(){
      // let data = this.$store.state.article.reviews
      return this.reviews
    }
  },
  async created() {
    await this.getReviews()
  },
  methods: {
    async getReviews() {


      if (this.isLogin) {
        const check = await this.$store.dispatch('getReviews', this.movie_id)
        this.reviews = check
        console.log(this.movie_id)
        console.log("이게 진짜 결과입니다",this.reviews)

      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'MainView' })
      }

    }
  },

}
</script>

<style scoped>
.Reive-page-title{
  font-style: bold;
  text-align: left;
  margin: 10px;
}

hr {
  background-color: #fff;
  padding: 0;
  margin: 10px;
}

hr.hr-1 {
  border: 0;
  height: 1px;
  background-image: linear-gradient(to right, rgba(255, 255, 255, 1), rgba(0, 0, 0, 0.75), rgba(255, 255, 255, 1));
}
</style>
