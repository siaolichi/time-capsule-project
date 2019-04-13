import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./views/About.vue')
    },
    {
      path: '/capsules',
      name: 'loading-page',
      component: () => import('./views/pages/loading-page.vue'),
      children: [
        {
          path: '',
          name: 'main-menu',
          component: () => import('./views/pages/main-menu.vue')
        },
        {
          path: 'capsule1',
          name: 'capsule1',
          component: () => import('./views/pages/capsule1.vue')
        },
        {
          path: 'capsule2',
          name: 'capsule2',
          component: () => import('./views/pages/capsule2.vue')
        },
        {
          path: 'capsule3',
          name: 'capsule3',
          component: () => import('./views/pages/capsule3.vue')
        }
      ]
    }
  ]
});
