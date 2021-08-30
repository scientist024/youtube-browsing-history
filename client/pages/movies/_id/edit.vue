<template>
  <div>
    <Toolbar :header="movie.title" :url="url"></Toolbar>

    <div class="container">
      <main class="container my-5">
        <div class="movie-wrap">
          <youtube ref="youtube" class="youtube" :video-id="splitVideoId[1]" />
        </div>

        <form @submit.prevent="submitMovie">
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="3">
                <v-text-field
                  v-model="movie.title"
                  label="タイトル"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-text-field v-model="movie.detail" label="感想" />
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-text-field v-model="movie.url" label="URL"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <b-form-group>
                  <b-form-tags
                    id="tags-with-dropdown"
                    v-model="value"
                    no-outer-focus
                    class="mb-2"
                    style="background-color: #f0f0f0; box-shadow: 0 0 1px gray"
                  >
                    <template #default="{ tags, disabled, addTag, removeTag }">
                      <ul
                        v-if="tags.length > 0"
                        class="list-inline d-inline-block mb-2"
                      >
                        <li
                          v-for="tag in tags"
                          :key="tag"
                          class="list-inline-item"
                        >
                          <b-form-tag
                            :title="tag"
                            :disabled="disabled"
                            variant="secondary"
                            @remove="removeTag(tag)"
                            >{{ tag }}</b-form-tag
                          >
                        </li>
                      </ul>

                      <b-dropdown
                        size="sm"
                        variant="outline-secondary"
                        block
                        menu-class="w-100"
                      >
                        <template #button-content>
                          <b-icon icon="tag-fill"></b-icon> 配信者名
                        </template>
                        <b-dropdown-form @submit.stop.prevent="() => {}">
                          <b-form-group
                            label="Search tags"
                            label-for="tag-search-input"
                            label-cols-md="auto"
                            class="mb-0"
                            label-size="sm"
                            :description="searchDesc"
                            :disabled="disabled"
                          >
                            <b-form-input
                              id="tag-search-input"
                              v-model="search"
                              type="search"
                              size="sm"
                              autocomplete="off"
                            ></b-form-input>
                          </b-form-group>
                        </b-dropdown-form>
                        <b-dropdown-divider></b-dropdown-divider>
                        <b-dropdown-item-button
                          v-for="option in availableOptions"
                          :key="option"
                          @click="onOptionClick({ option, addTag })"
                        >
                          {{ option }}
                        </b-dropdown-item-button>
                        <b-dropdown-text v-if="availableOptions.length === 0">
                          There are no tags available to select
                        </b-dropdown-text>
                      </b-dropdown>
                    </template>
                  </b-form-tags>
                </b-form-group>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <label>おもしろさ</label>
                <v-rating
                  v-model="movie.fun"
                  background-color="orange lighten-3"
                  color="orange"
                ></v-rating>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <label for="example-datepicker">視聴日</label>
                <b-form-datepicker
                  id="example-datepicker"
                  v-model="movie.watched_date"
                  class="mb-2"
                  style="background-color: #f0f0f0; box-shadow: 0 0 1px gray"
                ></b-form-datepicker>
              </v-col>
              <v-col cols="12">
                <v-btn type="submit" dark>編集</v-btn>
              </v-col>
            </v-row>
          </v-container>
        </form>
      </main>
    </div>
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex'
export default {
  async asyncData({ $axios, params }) {
    try {
      const movie = await $axios.$get(`/api/movie/${params.id}`)
      return { movie }
    } catch (e) {
      return { waterplant: [] }
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
      search: '',
      value: [],
      videoId: '',


      url: '/movies/add',
    }
  },
  head() {
    return {
      title: '編集画面',
    }
  },

  computed: {
    ...mapState(['streamers']),

    options() {
      const newArry = []
      for (const key in this.streamers) {
        newArry.push(this.streamers[key].name)
      }
      return newArry
    },

    valueJson() {
      const newArry = []
      for (let i = 0, len = this.value.length; i < len; i++) {
        const targetvalue = this.streamers.find((v) => v.name === this.value[i])
        newArry.push({ name: targetvalue.name, channel: targetvalue.channel })
      }
      return newArry
    },
    splitVideoId() {
      return this.movie.url.split('=')
    },
    criteria() {
      // Compute the search criteria
      return this.search.trim().toLowerCase()
    },
    availableOptions() {
      const criteria = this.criteria
      // Filter out already selected options
      const options = this.options.filter(
        (opt) => this.value.includes(opt) === false
      )
      if (criteria) {
        // Show only options that match criteria
        return options.filter(
          (opt) => opt.toLowerCase().includes(criteria) === true
        )
      }
      // Show all options available
      return options
    },
    searchDesc() {
      if (this.criteria && this.availableOptions.length === 0) {
        return 'There are no tags matching your search criteria'
      }
      return ''
    },
  },
  created() {
    this.getStreamer(this.categories)
  },
  methods: {
    async submitMovie() {
      const config = {
        header: { 'Content-Type': 'application/x-www-form-urlencoded' },
      }
      try {
        const response = await this.$axios.$patch(
          `/api/movie/${this.movie.id}/`,
          {
            streamers: this.valueJson,
            title: this.movie.title,
            url: this.movie.url,
            detail: this.movie.detail,
            fun: this.movie.fun,
            watched_date: this.movie.watched_date,
          },
          config
        )
        this.$router.push('/movies/')
        // eslint-disable-next-line no-console
        console.log(response)
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e.response)
      }
    },
    onOptionClick({ option, addTag }) {
      addTag(option)
      this.search = ''
    },
    ...mapActions(['getStreamer']),
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