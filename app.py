import streamlit as st
import os
import re
import xxhash

# 设置页面为 wide mode
st.set_page_config(layout="wide")

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def list_md_files(directory):
    file_path_list = []
    for file in os.listdir(directory):
        md_file_path = os.path.join(directory, file)
        if file.endswith('.md'):
            file_path_list.append(md_file_path)
    return file_path_list

def extract_titles(markdown_content):
    lines = markdown_content.split('\n')

    titles = []
    current_title = None
    in_code_block = False

    for line in lines:
        if '```' in line:
            in_code_block = not in_code_block

        if not in_code_block:
            if line.startswith('# '):
                current_title = (1, line[2:].strip())
            elif line.startswith('## '):
                current_title = (2, line[3:].strip())
            elif current_title:
                titles.append(current_title)
                current_title = None

    return titles

def create_anchor_from_text(text):
    new_anchor = ""

    # Check if the text is valid ASCII characters
    is_ascii = text and all(ord(char) < 128 for char in text)

    if is_ascii:
        # If the text is valid ASCII characters
        new_anchor = '-'.join(re.findall(r'\w+', text.lower()))
    elif text:
        # If the text is not valid ASCII, use a hash of the text
        new_anchor = format(xxhash.xxh32(text, seed=0xabcd).intdigest(), 'x')

    return new_anchor

def create_sidebar(titles):
    st.sidebar.markdown("**Document Structure**")

    for level, title in titles:
        # 生成锚点
        anchor = create_anchor_from_text(title)
        # 检查是否为当前页面标题，并应用样式
        style = "color: inherit; text-decoration: none;"

        # 使用自定义 CSS 样式
        st.sidebar.markdown(f"""
            <style>
                .sidebar-link:hover {{
                    text-decoration: underline !important;  # 添加下划线
                    color: #4682b4 !important;  # 鼠标悬停颜色
                }}
            </style>
            <div style='margin-left: {20 * (level - 1)}px; {style}'>
                <a href='#{anchor}' style='{style}'>{title}</a>
            </div>
        """, unsafe_allow_html=True)

def render_with_sidebar(md_files):
    selected_file = st.sidebar.radio("Select a file", [os.path.basename(file).split('.')[0] for file in md_files])

    file_path = f"markdown/{selected_file}.md"
    content = read_markdown_file(file_path)

    # 获取标题
    titles = extract_titles(content)

    # 生成侧边栏
    create_sidebar(titles)

    # 渲染 Markdown
    st.markdown(content, unsafe_allow_html=True)


# 读取 Markdown 文件列表
md_files = list_md_files("markdown")

# 显示主界面
render_with_sidebar(md_files)
