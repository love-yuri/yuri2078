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
