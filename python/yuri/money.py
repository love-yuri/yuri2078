import re

with open("E:\\love-yuri\\yuri2078\\python\\yuri\\money.txt", "r") as file:

  count = {}
  for line in file.readlines():
    regex = re.compile(r"消费金额[^\d]*(\d+)食堂消费")
    match = regex.match(line.strip())
    if match:
      money = (int)(match.group(1))
      if (count.get(money)):
        count[money] = count[money] + 1
      else:
        count.setdefault(money, 1)

  print(f"""
    30元消费: {count[30]} 次， 共计 {30 * count[30]}元； 
    20元消费: {count[20]} 次， 共计 {20 * count[20]}元； 
    10元消费: {count[10]} 次， 共计 {10 * count[10]}元;
    共计消费: {count[30] * 30 + count[20] * 20 + count[10] * 10} 元;
    """)
