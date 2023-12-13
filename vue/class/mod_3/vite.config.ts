/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-13 08:02:06
 * @LastEditTime: 2023-12-13 09:42:41
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
  build: {
    chunkSizeWarningLimit: 10000 // 设置新的警告阈值，单位为字节
  }
});
