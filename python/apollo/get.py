'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-10-03 20:48:19
LastEditTime: 2025-07-04 11:29:17
Description: 
'''
import re
da = 0


def find_score_400(file_path):
  # 存储总分为400的数据
  scores_400 = []

  with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
      global da
      da += 1
      # 去除行尾的换行符
      line = line.strip()
      regex = r'id: (\d+) 总分: ([1234567890.]+), 总时长: (\d+)'

      pattern = r"(xh_2025_狭窄道路通行|xh_2025_施工区域通行|xh_2025_交通标志场景|xh_2025_交通灯场景|xh_2025_动态避障场景|xh_2025_自主泊车场景): 得分: (\d+), 用时: (\d+)"
      matches = re.finditer(pattern, line)

      results = {}

      for match in matches:
        scene = match.group(1)
        score = int(match.group(2))
        duration = int(match.group(3))
        results[scene] = {'score': score, 'duration': duration}

      match = re.search(regex, line)
      if match:
        score = float(match.group(2))
        if score >= 600:
          scores_400.append({
              'id': match.group(1),
              'score': score,
              'time': match.group(3),
              'desc': f'id: {match.group(1)} 总分: {match.group(2)} 总时长: {match.group(3)}',
              'xh_2025_狭窄道路通行': results.get('xh_2025_狭窄道路通行'),
              'xh_2025_施工区域通行': results.get('xh_2025_施工区域通行'),
              'xh_2025_交通标志场景': results.get('xh_2025_交通标志场景'),
              'xh_2025_交通灯场景': results.get('xh_2025_交通灯场景'),
              'xh_2025_动态避障场景': results.get('xh_2025_动态避障场景'),
              'xh_2025_自主泊车场景': results.get('xh_2025_自主泊车场景'),
          })

  scores_400.sort(key=lambda x: (float(x['score']), float(x['time'])))
  return scores_400


# 指定文件路径
file_path = 'data3.txt'  # 替换为你的文件路径

# 执行查找
results = find_score_400(file_path)

# 输出结果
if results:
  print(f"共有数据 {da} 条，找到总分为600及以上的数据 {len(results)} 条。")
  print("按总分和耗时排序后的前20项数据:")
  for i, result in enumerate(results[:30], 1):
    print(
        f"{i}. id: {result['id']}, 总分: {result['score']}, 总时长: {result['time']}")

    print(f"   xh_2025_狭窄道路通行: {result['xh_2025_狭窄道路通行']}")
    print(f"   xh_2025_施工区域通行: {result['xh_2025_施工区域通行']}")
    print(f"   xh_2025_交通标志场景: {result['xh_2025_交通标志场景']}")
    print(f"   xh_2025_交通灯场景: {result['xh_2025_交通灯场景']}")
    print(f"   xh_2025_动态避障场景: {result['xh_2025_动态避障场景']}")
    print(f"   xh_2025_自主泊车场景: {result['xh_2025_自主泊车场景']}")

  # 统计四个场景的最优得分, 结合总分和耗时
  best_scores = {scene: None for scene in [
      'xh_2025_自主泊车场景', 'xh_2025_动态避障场景', 'xh_2025_交通灯场景', 'xh_2025_施工区域通行', 'xh_2025_交通标志场景', 'xh_2025_狭窄道路通行']}

  for scene in best_scores.keys():
    best_scores[scene] = max(
        results,
        key=lambda x: (x[scene]['score'], -x[scene]['duration']
                       ) if x[scene] else (0, float('inf'))
    )

  print("\n四个场景的最优得分（同分数时先比较场景得分，再比较耗时）：")
  for scene, result in best_scores.items():
    print(
        f"{scene}: 最优得分 = {result[scene]['score']}, 总分 = {result['score']}, 耗时 = {result[scene]['duration']} (id: {result['id']})")
else:
  print("没有找到总分为600的数据。")
