const third_head = {
  data() {
    return {
      message: 'Привет, Vue.js!'
    }
  },
  methods: {
    go_wines() {
        window.location.replace("http://127.0.0.1:8000/wines/");
    }
  }
}

Vue.createApp(third_head).mount('#third_head')