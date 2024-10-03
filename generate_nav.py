import os
import re

# 定义当前目录
current_dir = os.getcwd()

# 定义匹配文件名的正则表达式
pattern = re.compile(r'^(\d+)-(.+)\.html$')

# 收集符合条件的文件
files = []
for filename in os.listdir(current_dir):
    match = pattern.match(filename)
    if match:
        id_num = match.group(1)
        title = match.group(2)
        files.append((int(id_num), title, filename))

# 按照id排序
files.sort(key=lambda x: x[0])

# 生成HTML内容
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>FastAdmin 文档</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { text-align: center; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: #337ab7; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>FastAdmin 文档</h1>
    <ul>
'''

for id_num, title, filename in files:
    # 处理标题中的URL编码问题，如果有需要
    display_title = title.replace('-', '－')  # 替换可能的短横线
    html_content += f'        <li><a href="{filename}">{id_num} - {display_title}</a></li>\n'

html_content += '''    </ul>
</body>
</html>
'''

# 写入到 index.html 文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("导航页 'index.html' 已生成。")
