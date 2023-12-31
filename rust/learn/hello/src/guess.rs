use std::io;
use rand::Rng;

pub fn guess() {
  /* 新建字符串对象 */
  let mut str = String::new();
  /* 生成随机数 */ 
  let num = rand::thread_rng().gen_range(2..34);
  println!("num -> {}", num);
  loop {
    io::stdin().read_line(&mut str).expect("发生了错误");
    println!("你猜的是: {}", str);
  }
}