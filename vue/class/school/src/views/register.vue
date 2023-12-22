<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-07 16:15:20
 * @LastEditTime: 2023-12-17 19:54:33
 * @Description: 登陆界面
-->
<template>
  <div class="bg-gray-200 p-12 rounded-md">
    <div class="text-gray-500 text-[20px] font-medium">欢迎注册</div>
    <el-form :label-position="labelPosition" label-width="60px" class="mt-4">
      <el-form-item label="用户名">
        <el-input v-model="user.username" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="user.password" placeholder="请输入密码" />
      </el-form-item>
    </el-form>
    <div
      @click="login"
      class="p-1 text-center text-[20px] rounded-[12px] cursor-pointer text-white bg-[rgba(23,23,23,0.2)]"
    >
      登陆
    </div>
    <div class="flex items-center justify-between mt-3">
      <div class="flex justify-center">
        <div>已有账号？</div>
        <div class="text-gray-600">
          <router-link to="/login">登陆</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import axios from 'axios';
defineEmits(['login']);
const user = reactive({
  username: '',
  password: ''
});

const login = () => {
  axios
    .post('/api/user/register', user)
    .then((res) => {
      ElMessage.success(res.data);
      console.log('登陆成功');
    })
    .catch((err) => {
      ElMessage.error(err.response.data.message);
    });
};
</script>
