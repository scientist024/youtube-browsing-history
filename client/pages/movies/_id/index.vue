<template>
  <div>
    <Toolbar :header="movie.title" :url="url"></Toolbar>

    <v-container class="v-container">
      <div class="movie-wrap" style="margin: 30px">
        <youtube ref="youtube" class="youtube" :video-id="splitVideoId[1]" />
      </div>
      <v-row>
        <v-col cols="12" sm="6" md="4" xl="3">
          <h4>配信者名</h4>
          <p v-for="(list, i) in movie.streamers" :key="i">
            {{ movie.streamers[i]['name'] }}
          </p>
        </v-col>
        <v-col cols="12" sm="6" md="3">
          <h4>感想</h4>
          <p>{{ movie.detail }}</p>
        </v-col>
        <v-col cols="12" sm="6" md="3">
          <h4>面白さ</h4>
          <v-rating v-model="movie.fun" readonly></v-rating>
        </v-col>
        <v-col cols="12" sm="6" md="3">
          <h4>視聴日</h4>
          <p>{{ movie.watched_date }}</p>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios, params }) {
    try {
      const movie = await $axios.$get(`api/movie/${params.id}`)
      return { movie }
    } catch (e) {
      return { movie: [] }
    }
  },

  data() {
    return {
      movie: {
        streamers: [],
        title: '',
        url: '',
        detail: '',
        fun: 5,
        watched_date: '',
      },
      videoId: '',
    }
  },
  head() {
    return {
      title: '詳細ページ',
    }
  },
  computed: {
    splitVideoId() {
      return this.movie.url.split('=')
    },
    criteria() {
      // Compute the search criteria
      return this.search.trim().toLowerCase()
    },
  },
}
</script>
<style scoped>
.movie-wrap {
  display: flex;
  justify-content: center;
}

.movie-wrap iframe {
  max-width: 100%;
}
</style>