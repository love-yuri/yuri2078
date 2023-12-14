/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 16:07:35
 * @LastEditTime: 2023-12-14 18:27:15
 * @Description:
 */
import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  base: './' /* 设置打包根路径 */,
  build: {
    chunkSizeWarningLimit: 10000 // 设置新的警告阈值，单位为字节
  }
});
