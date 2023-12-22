/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 16:33:50
 * @LastEditTime: 2023-12-17 19:43:25
 * @Description: 路由
 */
import { createRouter, createWebHashHistory } from 'vue-router';
// import { ElNotification } from 'element-plus';

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: () => import('./views/login.vue') }
    // { path: '/login', component: () => import('./components/login.vue') },
  ]
});

// router.beforeEach((to, from, next) => {
//   if (to.fullPath.includes('home') && localStorage.getItem('currentUser') === null) {
//     next('/');
//   } else {
//     next();
//   }
// });

export default router;
