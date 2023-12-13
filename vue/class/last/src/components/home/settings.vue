<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-13 21:58:26
 * @LastEditTime: 2023-12-13 22:12:00
 * @Description: 
-->
<template>
  <div class="text-[24px] text-center font-semibold mb-3">修改用户资料</div>
  <van-form @submit="change">
    <van-cell-group inset>
      <van-field
        v-model="user.username"
        name="用户名"
        label="用户名"
        placeholder="用户名"
        :rules="[{ required: true, message: '请输入正确的用户名', pattern: /^[a-zA-Z0-9]+$/ }]"
      />
      <van-field
        v-model="user.password"
        name="密码"
        label="密码"
        placeholder="密码"
        :rules="[{ required: true, message: '请输入正确的密码', pattern: /^[a-zA-Z0-9]+$/ }]"
      />
    </van-cell-group>
    <div style="margin: 16px">
      <van-button round block type="primary" native-type="submit"> 提交 </van-button>
    </div>
  </van-form>
</template>
<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { type User, type History, type BorrowBook } from '@/components/index';
import { reactive, ref, onMounted } from 'vue';
const userMap = ref<Map<string, string>>(new Map());
const user = reactive<User>({
  username: '',
  password: ''
});

const change = () => {
  let oldUser: User = JSON.parse(localStorage.getItem('currentUser') as string);
  if (userMap.value.get(user.username) && user.username !== oldUser.username) {
    ElMessage.error('当前用户已存在!');
    return;
  }
  let histroys: History[] = JSON.parse(localStorage.getItem('borrowHistroy') as string);
  histroys.forEach((item) => {
    if (item.username === oldUser.username) {
      item.username = user.username;
    }
  });
  let borrows = JSON.parse(localStorage.getItem('borrowBook') as string) as BorrowBook[];
  borrows.forEach((item) => {
    if (item.username === oldUser.username) {
      item.username = user.username;
    }
  });
  localStorage.setItem('borrowBook', JSON.stringify(borrows));
  localStorage.setItem('borrowHistroy', JSON.stringify(histroys));
  localStorage.setItem('currentUser', JSON.stringify(user));
  ElMessage.success('更新成功');
  userMap.value.set(user.username, user.password);
  // new Map(Object.entries(JSON.parse(res)));
  localStorage.setItem('users', JSON.stringify(Object.fromEntries(userMap.value)));
};

onMounted(() => {
  let oldUser: User = JSON.parse(localStorage.getItem('currentUser') as string);
  user.username = oldUser.username;
  user.password = oldUser.password;
  const res = localStorage.getItem('users');
  if (res === null) {
    userMap.value = new Map();
  } else {
    userMap.value = new Map(Object.entries(JSON.parse(res)));
  }
});
</script>
