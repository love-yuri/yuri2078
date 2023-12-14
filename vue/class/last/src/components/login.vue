<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 17:16:32
 * @LastEditTime: 2023-12-14 11:02:29
 * @Description: 
-->
<template>
  <div class="w-full bg-[#0089BA] rounded-[16px] p-2 flex flex-col justify-center">
    <div class="text-white text-[20px] font-medium text-center">欢迎登陆</div>
    <van-form @submit="login">
      <van-field
        required
        v-model="user.username"
        placeholder="请输入用户名"
        class="rounded-[8px] mt-3"
        :rules="[{ required: true, message: '请填写用户名' }]"
      />
      <van-field
        required
        type="password"
        v-model="user.password"
        placeholder="请输入密码"
        class="rounded-[8px] mt-3 mb-3"
        :rules="[{ required: true, message: '请输入密码' }]"
      />
      <VanButton type="primary" native-type="submit" block class="mt-4 !rounded-[8px]"
        >登录</VanButton
      >
    </van-form>
    <div class="flex items-center justify-between mt-3">
      <div class="text-white flex justify-center">
        <div>没有账号？</div>
        <div class="text-gray-600">
          <router-link to="/register">注册</router-link>
        </div>
      </div>
      <div class="text-white text-right font-semibold cursor-pointer" @click="frogetPassword">
        忘记密码?
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { type User } from './index';
import { reactive, ref, onMounted } from 'vue';

const emit = defineEmits(['loginSuccess']);

const userMap = ref<Map<string, string>>(new Map());
const user = reactive<User>({
  username: '',
  password: ''
});

const login = () => {
  if (userMap.value.get(user.username) === user.password) {
    ElMessage.success('登录成功');
    emit('loginSuccess', user);
  } else if (userMap.value.get(user.username)) {
    ElMessage.error('密码错误!');
  } else {
    ElMessage.warning('该用户不存在!');
  }
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

const frogetPassword = () => {
  if (userMap.value.get(user.username)) {
    ElMessage.success('密码 : ' + userMap.value.get(user.username));
  } else {
    ElMessage.warning('该用户不存在!');
  }
};
</script>
