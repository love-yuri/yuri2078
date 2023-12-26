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
import { onMounted, onBeforeUnmount, provide, ref } from 'vue';
import { books } from '@/components/index';
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
