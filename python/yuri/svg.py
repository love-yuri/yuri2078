import cairosvg
from PIL import Image

cairosvg.svg2png(
  url="icon.svg", write_to="icon.png", output_width=256, output_height=256
)

img = Image.open("icon.png").convert("RGBA")
img.save(
  "icon.ico",
  format="ICO",
  sizes=[
    (16, 16),
    (24, 24),
    (32, 32),
    (48, 48),
    (64, 64),
    (128, 128),
    (256, 256),
  ],
)
