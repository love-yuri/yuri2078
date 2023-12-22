<template>
  <div class="main-container">
    <div class="sm:w-1/2 w-full flex justify-center items-center">
      <router-view />
    </div>
  </div>
</template>
<script setup lang="ts">
//
</script>
<style lang="less" scoped>
.main-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 6px;
  background-color: rgba(130, 140, 250, 0.2);
}
</style>
