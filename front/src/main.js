import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
import VueMoment from 'vue-moment'

Vue.use(VueMoment);
Vue.use(VueCookies)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')
