# 读取文件
with open('daily_arxiv.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到要插入的位置
insert_index = None
for i, line in enumerate(lines):
    if 'f.write("  table {" in line:
        insert_index = i
        break

if insert_index:
    # 在table样式之前插入body样式
    body_styles = [
        '            f.write("  /* 控制整个页面的最大宽度，提升大屏幕阅读体验 */\\n")\n',
        '            f.write("  body {\\n")\n',
        '            f.write("    max-width: 1400px;\\n")\n',
        '            f.write("    margin: 0 auto;\\n")\n',
        '            f.write("    padding: 20px;\\n")\n',
        '            f.write("  }\\n")\n',
        '\n'
    ]
    lines[insert_index:insert_index] = body_styles

# 写回文件
with open('daily_arxiv.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("成功添加body样式控制页面宽度")