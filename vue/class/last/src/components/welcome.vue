<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 16:23:48
 * @LastEditTime: 2023-12-13 17:04:04
 * @Description: 
-->
<template>
  <div class="w-full h-full flex flex-col justify-center">
    <div class="text-[33px] font-medium text-center text-gray-600">图书借阅</div>
    <div class="mt-[16px]">
      <van-swipe :autoplay="3000" indicator-color="white">
        <van-swipe-item v-for="image in images" :key="image">
          <img :src="image" />
        </van-swipe-item>
      </van-swipe>
    </div>
    <VanButton type="primary" @click="start" block class="!mt-3 !rounded-[12px]"
      >立即体验</VanButton
    >
  </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();
/* 图片信息 */
const images = [
  '/src/assets/swipe/wallhaven-g895pq_1920x1080.png',
  '/src/assets/swipe/wallhaven-q2oxdd_1920x1080.png',
  '/src/assets/swipe/wallhaven-r2k3y1_1920x1080.png',
  '/src/assets/swipe/wallhaven-vqmdq5_1920x1080.png'
];
const start = () => {
  router.push('/login');
};
</script>
<style lang="less">
.van-swipe {
  border-radius: 14px;
}
</style>
