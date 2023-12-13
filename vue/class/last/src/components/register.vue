<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 17:37:28
 * @LastEditTime: 2023-12-12 18:58:13
 * @Description: 注册界面
-->
<template>
  <div class="w-[90%] bg-[#0089BA] rounded-[16px] p-2 flex flex-col justify-center">
    <div class="text-white text-[20px] font-medium text-center">欢迎注册</div>
    <van-form @submit="login">
      <van-field
        required
        v-model="user.username"
        placeholder="请输入用户名"
        class="rounded-[8px] mt-3"
        :rules="[{ required: true, message: '请输入正确的用户名', pattern: /^[a-zA-Z0-9]+$/ }]"
      />
      <van-field
        required
        type="password"
        v-model="user.password"
        placeholder="请输入密码"
        class="rounded-[8px] mt-3 mb-3"
        :rules="[{ required: true, message: '请输入正确的密码', pattern: /^[a-zA-Z0-9]+$/ }]"
      />
      <VanButton type="primary" native-type="submit" block class="mt-4 !rounded-[8px]"
        >注册</VanButton
      >
    </van-form>
    <div class="text-white flex justify-center mt-3">
      <div>已有账号？</div>
      <div class="text-gray-600">
        <router-link to="/login">登录</router-link>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { type User } from './index';
import { reactive, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
const userMap = ref<Map<string, string>>(new Map());
const user = reactive<User>({
  username: '',
  password: ''
});

const login = () => {
  if (userMap.value.get(user.username)) {
    ElMessage.error('当前用户已存在!');
    return;
  }
  ElMessage.success('注册成功');
  userMap.value.set(user.username, user.password);
  // new Map(Object.entries(JSON.parse(res)));
  localStorage.setItem('users', JSON.stringify(Object.fromEntries(userMap.value)));
  user.username = '';
  user.password = '';
  router.push('/login');
};

onMounted(() => {
  // localStorage.removeItem('users');
  const res = localStorage.getItem('users');
  if (res === null) {
    userMap.value = new Map();
  } else {
    userMap.value = new Map(Object.entries(JSON.parse(res)));
  }
});
</script>
