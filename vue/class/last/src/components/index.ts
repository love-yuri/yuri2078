/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 18:05:43
 * @LastEditTime: 2023-12-14 11:48:18
 * @Description: 主ts文件
 */
/* 用户 */
export interface User {
  username: string;
  password: string;
}

/* 书本信息 */
export interface BookInfo {
  id: number;
  name: string;
  author: string;
  price: number;
  img: string;
  num: number; // 书籍总数量
  borrow: number; // 借走
}

/* 借阅信息 */
export interface BorrowBook {
  username: string;
  bookId: number;
}

/* 历史信息 */
export interface History {
  username: string;
  book: BookInfo;
  borrowtime: string;
  returntime: string;
  status: number;
}

import p1 from '/src/assets/books/呐喊.jpg';
import p2 from '/src/assets/books/活着.jpg';
import p3 from '/src/assets/books/啊Q正传.jpg';
import p4 from '/src/assets/books/四世同堂.jpg';
import p5 from '/src/assets/books/朝花夕拾.jpg';
import p6 from '/src/assets/books/狂人日记.jpg';
import p7 from '/src/assets/books/毛泽东选集.jpg';
import p8 from '/src/assets/books/茶馆.jpg';
import p9 from '/src/assets/books/骆驼祥子.jpg';
import p10 from '/src/assets/books/第七天.jpg';
import p11 from '/src/assets/books/文城.jpg';
import p12 from '/src/assets/books/在细雨中呐喊.jpg';
import p13 from '/src/assets/books/许三观卖血记.jpg';
import p14 from '/src/assets/books/第七天.jpg';

export const books = [
  {
    id: 1,
    name: '呐喊',
    author: '鲁迅',
    price: 30,
    img: p1,
    num: 5,
    borrow: 0
  },
  {
    id: 2,
    name: '活着',
    author: '余华',
    price: 23,
    img: p2,
    num: 5,
    borrow: 0
  },
  {
    id: 3,
    name: '啊Q正传',
    author: '鲁迅',
    price: 33,
    img: p3,
    num: 5,
    borrow: 0
  },
  {
    id: 4,
    name: '四世同堂',
    author: '鲁迅',
    price: 44,
    img: p4,
    num: 5,
    borrow: 0
  },
  {
    id: 5,
    name: '朝花夕拾',
    author: '鲁迅',
    price: 45,
    img: p5,
    num: 5,
    borrow: 0
  },
  {
    id: 6,
    name: '狂人日记',
    author: '鲁迅',
    price: 59,
    img: p6,
    num: 5,
    borrow: 0
  },
  {
    id: 7,
    name: '毛泽东选集',
    author: '毛泽东',
    price: 32,
    img: p7,
    num: 5,
    borrow: 0
  },
  {
    id: 8,
    name: '茶馆',
    author: '老舍',
    price: 44,
    img: p8,
    num: 5,
    borrow: 0
  },
  {
    id: 9,
    name: '骆驼祥子',
    author: '老舍',
    price: 25,
    img: p9,
    num: 5,
    borrow: 0
  },
  {
    id: 10,
    name: '第七天',
    author: '余华',
    price: 33,
    img: p10,
    num: 5,
    borrow: 0
  },
  {
    id: 11,
    name: '文城',
    author: '余华',
    price: 23,
    img: p11,
    num: 5,
    borrow: 0
  },
  {
    id: 12,
    name: '在细雨中呐喊',
    author: '余华',
    price: 233,
    img: p12,
    num: 5,
    borrow: 0
  },
  {
    id: 13,
    name: '许三观卖血记',
    author: '余华',
    price: 34,
    img: p13,
    num: 5,
    borrow: 0
  },
  {
    id: 14,
    name: '第七天',
    author: '余华',
    price: 33,
    img: p14,
    num: 5,
    borrow: 0
  }
];
