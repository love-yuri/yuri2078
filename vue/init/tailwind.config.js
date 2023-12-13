/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-11-05 20:42:03
 * @LastEditTime: 2023-11-05 20:55:39
 * @Description: tailwindcss配置文件
 */
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {
      zIndex: {
        '-1': '-1'
      }
    }
  }
}
