/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 16:33:50
 * @LastEditTime: 2023-12-13 09:30:53
 * @Description: 路由
 */
import { createRouter, createWebHashHistory } from 'vue-router';
// import { ElNotification } from 'element-plus';

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      component: () => import('./components/introduction.vue'),
      props: false
    },
    {
      path: '/introduction',
      component: () => import('./components/introduction.vue'),
      props: false
    },
    {
      path: '/scenery',
      component: () => import('./components/scenery.vue'),
      props: false
    },
    {
      path: '/majors',
      component: () => import('./components/majors.vue'),
      props: false,
      children: [
        {
          path: '',
          component: () => import('./components/majors/computer-science.vue'),
          props: false
        },
        {
          path: 'computer-science',
          component: () => import('./components/majors/computer-science.vue'),
          props: false
        },
        {
          path: 'computer-science',
          component: () => import('./components/majors/computer-science.vue'),
          props: false
        },
        {
          path: 'iot-engineering',
          component: () => import('./components/majors/iot-engineering.vue'),
          props: false
        },
        {
          path: 'digital-media',
          component: () => import('./components/majors/digital-media.vue'),
          props: false
        },
        {
          path: 'data-science',
          component: () => import('./components/majors/data-science.vue'),
          props: false
        },
        {
          path: 'software',
          component: () => import('./components/majors/software.vue'),
          props: false
        }
      ]
    },
    {
      path: '/announcements',
      component: () => import('./components/announcements.vue'),
      props: false
    },
    {
      path: '/announcements/1',
      component: () => import('./components/1.vue'),
      props: false
    }
  ]
});

// const root_user = ['yuri', 'root'];

// router.beforeEach((to, from, next) => {
//   let username = localStorage.getItem('username');
//   if (username === null) {
//     username = '';
//   }
//   if (to.fullPath == '/car/3' && !root_user.includes(username)) {
//     next('/car/0');
//     ElNotification.error('普通用户禁止进入管理界面!');
//     return;
//   }
//   next();
// });

export default router;
