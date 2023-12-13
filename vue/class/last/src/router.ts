/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 16:33:50
 * @LastEditTime: 2023-12-13 22:21:14
 * @Description: 路由
 */
import { createRouter, createWebHashHistory } from 'vue-router';
// import { ElNotification } from 'element-plus';

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: () => import('./components/welcome.vue') },
    { path: '/login', component: () => import('./components/login.vue') },
    { path: '/register', component: () => import('./components/register.vue') },
    {
      path: '/home',
      component: () => import('./components/home/index.vue'),
      children: [
        { path: '', component: () => import('./components/home/hot.vue') },
        { path: 'hot', component: () => import('./components/home/hot.vue') },
        { path: 'college', component: () => import('./components/home/college.vue') },
        { path: 'history', component: () => import('./components/home/history.vue') },
        { path: 'settings', component: () => import('./components/home/settings.vue') }
      ]
    }
  ]
});

// const root_user = ['yuri', 'root'];

router.beforeEach((to, from, next) => {
  if (to.fullPath.includes('home') && localStorage.getItem('currentUser') === null) {
    next('/');
  } else {
    next();
  }
});

export default router;
