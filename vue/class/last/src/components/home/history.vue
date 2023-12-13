<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-13 13:47:40
 * @LastEditTime: 2023-12-13 21:45:15
 * @Description: 
-->
<template>
  <div class="w-full bg-slate-400">
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="book.name" label="书名" width="100" />
      <el-table-column prop="username" label="借阅者" width="80" />
      <el-table-column prop="borrowtime" label="借阅时间" width="100" />
      <el-table-column prop="returntime" label="归还时间" width="100" />
    </el-table>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import type { History } from '@/components/index';
const tableData = ref<History[]>([]);

onMounted(() => {
  let histroys: History[] = JSON.parse(localStorage.getItem('borrowHistroy') as string);
  tableData.value = histroys;
});
</script>
