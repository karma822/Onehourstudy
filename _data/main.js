import Vue from 'vue'
import App from './App'
import axios from 'axios'

Vue.prototype.$http = axios
new Vue({
    el: '#app',
    template: '<App/>',
    components:{ App },
    data: {
        message: 'Hello'
    }
})