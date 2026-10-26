"""
直接运行即可生成图片，只需修改下方 prompt 变量
"""

import base64
from datetime import datetime
from pathlib import Path
from openai import OpenAI

# ============ 只改这里 ============
prompt = "一只戴着礼帽的耄耋，坐在窗台上看雨，油画风格"
model = "gpt-image-2"  # 如有新版可改为 "gpt-image-2"
size = "1024x1024"  # 1024x1024, 1536x1024, 1024x1536, auto
quality = "high"  # low, medium, high, auto
output_format = "png"  # png, jpeg, webp
output_dir = "outputs"
# ==================================

client = OpenAI(
  api_key='sk-Kq4pj6sdthNEMdgW0YT9lQAcSol6JpZAgnTZh2hjlQji7EXt',
  base_url='https://ai.yidon.top/v1/'
)  # 自动读取环境变量 OPENAI_API_KEY

print(f"提示词: {prompt}")
print("正在生成图片，请稍候...")

result = client.images.generate(
  model=model,
  prompt=prompt,
  size=size,
  quality=quality,
  output_format=output_format,
  n=1,
)

# 保存图片
out_path = Path(output_dir)
out_path.mkdir(parents=True, exist_ok=True)

image_data = result.data[0] # type: ignore

if image_data.b64_json:
  img_bytes = base64.b64decode(image_data.b64_json)
elif image_data.url:
  import httpx

  resp = httpx.get(image_data.url, timeout=120)
  resp.raise_for_status()
  img_bytes = resp.content
else:
  raise RuntimeError("API 未返回图片数据")

file_path = out_path / f"image_{datetime.now():%Y%m%d_%H%M%S}.{output_format}"
file_path.write_bytes(img_bytes)

print(f"图片已保存: {file_path}")

if image_data.revised_prompt:
  print(f"优化后的提示词: {image_data.revised_prompt}")
