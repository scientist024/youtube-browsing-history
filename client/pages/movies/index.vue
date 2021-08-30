<template>
  <div>
    <Toolbar :header="header" :url="url"></Toolbar>
    <v-container class="grey lighten-5">
      <v-row>
        <v-col
          v-for="movie in movies"
          :key="movie.id"
          class="d-flex"
          cols="12"
          sm="12"
          md="12"
          lg="6"
          xl="4"
        >
          <v-card
            hover
            max-width="100%"
            height="100%"
            class="d-flex flex-column"
            style="width: 200%"
          >
            <v-card-title class="justify-center">{{
              movie.title | omittedText
            }}</v-card-title>
            <v-card-text>watched date: {{ movie.watched_date }}</v-card-text>
            <v-spacer />
            <v-card-actions class="mb-7">
              <div class="btn-crud" style="margin: 10px">
                <v-btn class="btn" dark nuxt :to="`/movies/${movie.id}`">
                  詳細
                </v-btn>
                <v-btn class="btn" dark nuxt :to="`/movies/${movie.id}/edit/`">
                  編集
                </v-btn>

                <v-btn class="btn" dark nuxt @click="deleteMovie(movie.id)">
                  削除
                </v-btn>
              </div>
              <v-row>
                <v-col cols="12">
                  <span v-for="(list, i) in movie.streamers" :key="i"
                    ><v-chip small>{{
                      movie.streamers[i]['name']
                    }}</v-chip></span
                  ></v-col
                >
              </v-row>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
export default {
  filters: {
    omittedText(text) {
      return text.length > 20 ? text.slice(0, 20) + '…' : text
    },
  },
  data() {
    return {
      header: '配信一覧',
      url: '/movies/add',
    }
  },
  head() {
    return {
      title: 'movie list',
    }
  },

  computed: mapState(['movies']),
  created() {
    this.getMovie(this.categories)
  },
  methods: {
    ...mapActions(['getMovie']),

    async deleteMovie(id) {
      try {
        await this.$axios.$delete(`/api/movie/${id}`)
        this.getMovie(this.categories)
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e)
      }
    },
  },
}
</script>
<style>
.btn {
  cursor: pointer;
}
.btn-crud {
  margin: 3px;
}
</style>