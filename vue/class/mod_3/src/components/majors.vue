<template>
  <div class="w-full h-full flex">
    <div>
      <van-sidebar v-model="active">
        <van-sidebar-item title="计算机科学与技术" to="/majors/computer-science" />
        <van-sidebar-item title="物联网工程" to="/majors/iot-engineering" />
        <van-sidebar-item title="软件工程" to="/majors/software" />
        <van-sidebar-item title="数字媒体技术" to="/majors/digital-media" />
        <van-sidebar-item title="数据科学与大数据技术" to="/majors/data-science" />
      </van-sidebar>
    </div>
    <div class="flex-1 overflow-y-auto">
      <RouterView />
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
const active = ref(0);
</script>
