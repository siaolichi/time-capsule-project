import axios from 'axios';
import VueAxios from 'vue-axios';
import jQuery from 'jquery';

import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

global.$ = jQuery;

Vue.use(VueAxios, axios);

Vue.config.productionTip = false;
// axios.defaults.withCredentials = true;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
