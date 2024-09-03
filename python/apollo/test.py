import re

text = """
id: 88267 总分: 300, 总时长: 676, 减速通行场景: 得分: 100, 用时: 82, taskId: 66bed65b00a9c114ea5ce560
障碍物绕行场景: 得分: 100, 用时: 136, taskId: 66bed65c00a9c12d5a5ce561
车辆靠边启动场景: 得分: 0, 用时: 300, taskId: 66bed65c00a9c17b8e5ce563
动态障碍物场景: 得分: 100, 用时: 158, taskId: 66bed65c00a9c1957e5ce562
"""

pattern = r"(减速通行场景|障碍物绕行场景|车辆靠边启动场景|动态障碍物场景): 得分: (\d+), 用时: (\d+)"
matches = re.finditer(pattern, text)

results = {}

for match in matches:
    scene = match.group(1)
    score = int(match.group(2))
    duration = int(match.group(3))
    results[scene] = {'score': score, 'duration': duration}

for scene, data in results.items():
    print(f"{scene}: 得分 = {data['score']}, 用时 = {data['duration']}")
