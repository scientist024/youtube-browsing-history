<template>
  <div>
    <v-toolbar dark>
      <v-toolbar-title>{{ header }}</v-toolbar-title>

      <v-spacer></v-spacer>
      <v-tooltip bottom>
        <template #activator="{ on, attrs }">
          <v-btn
            icon
            class="btn"
            rounded
            dark
            nuxt
            :to="url"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-plus-circle</v-icon>
          </v-btn>
        </template>
        <span>追加する</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template #activator="{ on, attrs }">
          <v-btn
            icon
            class="btn"
            rounded
            dark
            nuxt
            to="/movies"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-youtube</v-icon>
          </v-btn>
        </template>
        <span>配信一覧</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template #activator="{ on, attrs }">
          <v-btn
            icon
            class="btn"
            rounded
            dark
            nuxt
            to="/streamers"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <span>配信者一覧</span>
      </v-tooltip>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  props: {
    header: {
      type: String,
      default: 'title',
    },
    url: {
        type: undefined	,
        default: '/movies',
    }
  },
  computed: {
      computedUrl() {
return "/" + this.url
      }
  }
}
</script>