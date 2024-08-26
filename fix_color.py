import re

# 打开原始SVG文件
with open('assets/images/church-logo.svg', 'r') as file:
    svg_content = file.read()

# 将所有黑色填充改为白色
svg_content_updated = re.sub(r'fill="#212225"|fill="black"', 'fill="#FFFFFF"', svg_content)

# 将更新后的内容写入新文件或覆盖原文件
with open('assets/images/church-logo.svg', 'w') as file:
    file.write(svg_content_updated)

print('Color fixed successfully!')
