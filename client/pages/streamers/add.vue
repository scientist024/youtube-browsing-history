<template>
  <div>
    <Toolbar :header="header" :url="url"></Toolbar>
    <form @submit.prevent="submitStreamer">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="streamers.name"
              label="配信者名"
              :rules="rules"
              hide-details="auto"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="streamers.channel"
              label="チャンネル名"
              :rules="rules"
              hide-details="auto"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn dark type="submit">追加</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      streamers: {
        name: '',
        channel: '',
      },
      header: '配信者追加',
      url: '#',

      rules: [
        (value) => !!value || 'Required.',
        (value) => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }
  },
  methods: {
    async submitStreamer() {
      const config = {
        header: { 'Content-Type': 'application/x-www-form-urlencoded' },
      }
      try {
        await this.$axios.$post(
          '/api/streamer/',
          {
            name: this.streamers.name,
            channel: this.streamers.channel,
          },
          config
        )
        this.$router.push('/streamers/')
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e.response)
      }
    },
  },
}
</script>