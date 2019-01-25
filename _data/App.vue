<template>
  <div id="app">
  <p>{{message}}</p>
    <button v-on:click="searchTerm">Load</button>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
Vue.prototype.$http = axios

export default {
  name: 'app',
  methods: {
    searchTerm: function () {
      // using JSONPlaceholder
      const baseURI = 'https://jsonplaceholder.typicode.com';
      axios.get(`${baseURI}/posts`)
      .then((result) => {
        console.log(result)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 560px;
}
</style>
