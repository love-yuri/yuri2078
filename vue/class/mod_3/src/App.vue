<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-30 09:22:10
 * @LastEditTime: 2023-12-13 10:04:14
 * @Description: 初始化
-->
<template>
  <div class="main-container">
    <div class="sm:w-1/2 w-full flex justify-center h-full flex-col">
      <VanImage src="/src/assets/swipe/bg.jpg" class="h-[110px]" />
      <div class="flex-1 min-h-0 flex flex-col">
        <div class="flex-shrink-0">
          <van-tabs v-model:active="active" title-active-color="#6F9B94" @change="change">
            <van-tab title="学院介绍" name="introduction" />
            <van-tab title="校园风光" name="scenery" />
            <van-tab title="专业介绍" name="majors" />
            <van-tab title="通知公告" name="announcements" />
            <van-tab title="学生工作" name="student-affairs" />
          </van-tabs>
        </div>
        <div class="overflow-y-auto">
          <RouterView />
        </div>
      </div>
      <div class="text-[26px] flex items-center justify-center p-3 bg-[#3A5E5E]">
        <span>计算机科学与工程学员</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const active = ref(0);
const router = useRouter();

const change = (tab: string) => {
  router.push('/' + tab);
};
</script>

<style lang="less" scoped>
.main-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 6px;
}
</style>
