import wordcloud # 导入词云库
import jieba # 导入jieba库

text = '牢牢把握高质量发展这个首要任务和构建新发展格局这个战略任务，发挥自身优势' # 设置字体

wc = wordcloud.WordCloud() # 创建词云
wc = wordcloud.WordCloud(font_path='/usr/share/fonts/wps-office/FZSSK.TTF') # 设置中文路径防止乱码
wc.generate(' '.join(jieba.lcut(text))) # 使用jieba 分割中文
wc.to_file('test.png') # 输出图片
