<template>
  <div id="app">
    <Toolbar :header="header" :url="url"></Toolbar>
    <v-app id="inspire">
      <v-content class="pa-3">
        <v-row no-gutters>
          <v-col
            v-for="(item, index) in streamers"
            :key="index"
            cols="12"
            xs="12"
            sm="12"
            md="6"
            lg="3"
            xl="3"
          >
            <v-card hover>
              <v-card-title class="name">
                {{ item.name }}
              </v-card-title>
              <v-card-actions>
                <v-btn flat dark @click="deleteStreamer(item.id)">削除</v-btn>
                <v-btn dark :href="item.channel">チャンネルへ</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data() {
    return {
      header: '配信者一覧',
      url: '/streamers/add',
    }
  },
  computed: mapState(['streamers']),
  created() {
    this.getStreamer(this.categories)
  },
  methods: {
    ...mapActions(['getStreamer']),

    async deleteStreamer(id) {
      try {
        await this.$axios.$delete(`/api/streamer/${id}`)
        this.getStreamer(this.categories)
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e)
      }
    },
  },
}
</script>