export const state = () => ({
  movies: [],
  streamers: [],
})

export const mutations = {
  setMovie(state, movies) {
    state.movies = movies
  },
  setStreamer(state, streamers) {
    state.streamers = streamers
  },
}

export const actions = {
  async getMovie({ commit }, categories) {
    const response = await this.$axios.$get('/api/movie')
    commit('setMovie', response)
  },
  async getStreamer({ commit }, categories) {
    const response = await this.$axios.$get('/api/streamer')
    commit('setStreamer', response)
  },
}
