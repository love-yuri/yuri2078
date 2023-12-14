<!--
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-13 13:47:40
 * @LastEditTime: 2023-12-14 11:35:25
 * @Description: 
-->
<template>
  <div class="h-full w-full flex flex-col">
    <el-tabs v-model="activeName" class="flex-shrink-0" @tab-click="handleClick">
      <el-tab-pane label="所有" name="first" />
      <el-tab-pane label="鲁迅" name="second" />
      <el-tab-pane label="余华" name="third" />
      <el-tab-pane label="其他" name="fourth" />
    </el-tabs>
    <div class="show-img flex-1">
      <van-image
        fit="contain"
        @click="(showCenter = true), (currentBook = books[index])"
        v-for="(book, index) in books"
        :key="index"
        :src="book.img"
      />
    </div>
  </div>
  <!-- 圆角弹窗（居中） -->
  <van-popup v-model:show="showCenter" round :style="{ padding: '64px' }">
    <div class="font-semibold text-[22px] text-center mb-4">{{ currentBook.name }}</div>
    <van-image fit="contain" :src="currentBook.img" />
    <div class="flex flex-col">
      <el-tag type="success">作者 : {{ currentBook.author }}</el-tag>
      <el-tag type="info">价格 : {{ currentBook.price }}</el-tag>
    </div>
    <div class="flex items-center justify-between pl-3 pr-3 mt-3">
      <el-badge :value="currentBook.borrow" class="item">
        <el-button type="primary">已经借阅</el-button>
      </el-badge>
      <el-badge :value="currentBook.num - currentBook.borrow" class="item">
        <el-button type="success">剩余</el-button>
      </el-badge>
      <el-button type="info" @click="borrow">
        {{ `${hosBorrow ? '已借阅' : '借阅'}` }}
      </el-button>
    </div>
  </van-popup>
</template>
<script lang="ts" setup>
import { reactive, onMounted, ref, computed } from 'vue';
import type { BookInfo, BorrowBook, User, History } from '@/components/index';
import { ElMessage } from 'element-plus';

const borrowBook = ref<BorrowBook[]>([]);
const books = reactive<BookInfo[]>([]);
const allBooks = reactive<BookInfo[]>([]);

const user = ref<User>();
const showCenter = ref(false);
const currentBook = ref<BookInfo>({
  id: 1,
  price: 2,
  img: '',
  name: '',
  author: '',
  num: 0,
  borrow: 0
});

const hosBorrow = computed(() => {
  return borrowBook.value.map((item) => item.bookId).includes(currentBook.value.id);
});

const fromatTime = (time: Date) => {
  return `${time.getFullYear()}-${time.getMonth() + 1}-${time.getDate()}`;
};

const borrow = () => {
  if (
    borrowBook.value.find(
      (item) => item.bookId === currentBook.value.id && item.username === user.value?.username
    ) !== undefined
  ) {
    showCenter.value = false;
    ElMessage.error('您已经借阅过该书');
    return;
  }
  currentBook.value.borrow++;
  borrowBook.value.push({
    bookId: currentBook.value.id,
    username: user.value?.username as string
  });
  localStorage.setItem('borrowBook', JSON.stringify(borrowBook.value));
  showCenter.value = false;
  ElMessage.success('借阅成功');
  localStorage.setItem('bookInfos', JSON.stringify(allBooks));
  let histroys: History[] = JSON.parse(localStorage.getItem('borrowHistroy') as string);
  if (histroys === null) {
    histroys = [];
  }
  histroys.push({
    username: user.value?.username as string,
    book: currentBook.value,
    borrowtime: fromatTime(new Date()),
    returntime: '',
    status: 0
  });
  localStorage.setItem('borrowHistroy', JSON.stringify(histroys));
  console.log(histroys);
};

import type { TabsPaneContext } from 'element-plus';

const activeName = ref('first');

const handleClick = (tab: TabsPaneContext) => {
  books.length = 0;
  if (tab.props.label === '所有') {
    books.push(...allBooks);
  } else if (tab.props.label === '鲁迅' || tab.props.label === '余华') {
    books.push(...allBooks.filter((item) => item.author === tab.props.label));
  } else {
    books.push(...allBooks.filter((item) => !['鲁迅', '余华'].includes(item.author)));
  }
};

onMounted(() => {
  // localStorage.setItem('borrowHistroy', []);
  allBooks.push(...JSON.parse(localStorage.getItem('bookInfos') as string));
  books.push(...allBooks);
  let borrows = JSON.parse(localStorage.getItem('borrowBook') as string) as BorrowBook[];
  if (borrows === null) {
    borrows = [];
  }
  user.value = JSON.parse(localStorage.getItem('currentUser') as string);
  borrowBook.value = borrows.filter((item) => item.username === user.value?.username) || [];
});
</script>
<style lang="less" scoped>
.show-img {
  column-count: 3;
  column-gap: 10px;
}
</style>
