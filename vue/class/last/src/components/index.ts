/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2023-12-12 18:05:43
 * @LastEditTime: 2023-12-13 21:32:31
 * @Description: 主ts文件
 */
export interface User {
  username: string;
  password: string;
}

export interface BookInfo {
  id: number;
  name: string;
  author: string;
  price: number;
  img: string;
  num: number; // 书籍总数量
  borrow: number; // 借走
}

export interface BorrowBook {
  username: string;
  bookId: number;
}

export interface History {
  username: string;
  book: BookInfo;
  borrowtime: string;
  returntime: string;
  status: number;
}
