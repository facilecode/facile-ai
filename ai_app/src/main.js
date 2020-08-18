import Vue from 'vue'
//import App from './App.vue'
import Main from './views/Main.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(Main)
}).$mount('#app')
