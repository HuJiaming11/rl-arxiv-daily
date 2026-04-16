with open('daily_arxiv.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 在table样式之前添加body样式
old_pattern = 'f.write("  table {'
new_text = '''f.write("  /* 控制整个页面的最大宽度，提升大屏幕阅读体验 */\\n")
f.write("  body {\\n")
f.write("    max-width: 1400px;\\n")
f.write("    margin: 0 auto;\\n")
f.write("    padding: 20px;\\n")
f.write("  }\\n")
f.write("  table {'''

content = content.replace(old_pattern, new_text)

with open('daily_arxiv.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("成功添加body样式控制页面宽度")