<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 18:59:21
 * @LastEditTime: 2023-12-14 11:23:30
 * @Description: 主页
-->
<template>
  <div class="flex flex-col w-full">
    <el-scrollbar class="w-full flex-1">
      <router-view />
    </el-scrollbar>
    <div class="flex-shrink-0">
      <van-tabbar v-model="active">
        <van-tabbar-item icon="home-o" to="/home/hot">首页</van-tabbar-item>
        <van-tabbar-item icon="search" to="/home/college">我的借阅</van-tabbar-item>
        <van-tabbar-item icon="friends-o" to="/home/history">借阅历史</van-tabbar-item>
        <van-tabbar-item icon="setting-o" to="/home/settings">标签</van-tabbar-item>
      </van-tabbar>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
const active = ref(0);

onMounted(() => {
  const currentUrl = window.location.href;
  const parts = currentUrl.split('/home/');
  if (parts.length > 1) {
    const contentAfterHome = parts[1];
    if (contentAfterHome === 'college') {
      active.value = 1;
    } else if (contentAfterHome === 'history') {
      active.value = 2;
    } else if (contentAfterHome === 'settings') {
      active.value = 3;
    }
  } else {
    console.log('URL不符合预期格式');
  }
});
</script>
<style lang="less">
.van-tabbar--fixed {
  background-color: rgba(170, 171, 187);
  .van-tabbar-item--active {
    background-color: transparent;
  }
}
</style>
