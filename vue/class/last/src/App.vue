<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-30 09:22:10
 * @LastEditTime: 2023-12-13 21:52:46
 * @Description: 初始化
-->
<template>
  <div class="main-container">
    <div class="sm:w-1/2 w-full flex justify-center">
      <router-view @login-success="loginSuccess" />
    </div>
  </div>
</template>
<script setup lang="ts">
import { reactive, onMounted, onBeforeUnmount, provide, ref } from 'vue';
import { type BookInfo } from '@/components/index';
import { useRouter } from 'vue-router';
import { type User } from '@/components/index';

const currentUser = ref<User>();
provide('currentUser', currentUser);
const router = useRouter();
const loginSuccess = (user: User) => {
  localStorage.setItem('currentUser', JSON.stringify(user));
  currentUser.value = user;
  router.push('/home');
};

onBeforeUnmount(() => {
  localStorage.removeItem('currentUser');
});

const books = reactive<BookInfo[]>([
  {
    id: 1,
    name: '呐喊',
    author: '鲁迅',
    price: 30,
    img: '/src/assets/books/呐喊.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 2,
    name: '活着',
    author: '余华',
    price: 23,
    img: '/src/assets/books/活着.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 3,
    name: '啊Q正传',
    author: '鲁迅',
    price: 33,
    img: '/src/assets/books/啊Q正传.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 4,
    name: '四世同堂',
    author: '鲁迅',
    price: 44,
    img: '/src/assets/books/四世同堂.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 5,
    name: '朝花夕拾',
    author: '鲁迅',
    price: 45,
    img: '/src/assets/books/朝花夕拾.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 6,
    name: '狂人日记',
    author: '鲁迅',
    price: 59,
    img: '/src/assets/books/狂人日记.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 7,
    name: '毛泽东选集',
    author: '毛泽东',
    price: 32,
    img: '/src/assets/books/毛泽东选集.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 8,
    name: '茶馆',
    author: '老舍',
    price: 44,
    img: '/src/assets/books/茶馆.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 9,
    name: '骆驼祥子',
    author: '老舍',
    price: 25,
    img: '/src/assets/books/骆驼祥子.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 10,
    name: '第七天',
    author: '余华',
    price: 33,
    img: '/src/assets/books/第七天.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 11,
    name: '文城',
    author: '余华',
    price: 23,
    img: '/src/assets/books/文城.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 12,
    name: '在细雨中呐喊',
    author: '余华',
    price: 233,
    img: '/src/assets/books/在细雨中呐喊.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 12,
    name: '许三观卖血记',
    author: '余华',
    price: 34,
    img: '/src/assets/books/许三观卖血记.jpg',
    num: 5,
    borrow: 0
  },
  {
    id: 13,
    name: '第七天',
    author: '余华',
    price: 33,
    img: '/src/assets/books/第七天.jpg',
    num: 5,
    borrow: 0
  }
]);

onMounted(() => {
  if (!localStorage.getItem('bookInfos')) {
    localStorage.setItem('bookInfos', JSON.stringify(books));
  }
});
</script>
<style lang="less" scoped>
.main-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  padding: 5px 6px;
  background-color: rgba(130, 140, 250, 0.2);
}
</style>
