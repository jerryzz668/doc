import regex
import re
import xxhash

def create_anchor_from_text(text):
    new_anchor = ""

    # Check if the text is valid ASCII characters
    is_ascii = text and all(ord(char) < 128 for char in text)

    if is_ascii:
        # If the text is valid ASCII characters
        new_anchor = '-'.join(filter(None, regex.split(r'[^\p{L}\p{N}]+', text.lower())))
    elif text:
        # If the text is not valid ASCII, use a hash of the text
        new_anchor = format(xxhash.xxh32(text, seed=0xabcd).intdigest(), 'x')

    return new_anchor

# 示例用法
titles = ["Linux", "Tmux", "配置Conda源", "创建git公钥", "一、shell常用命令", "基本指令"]

for title in titles:
    anchor = create_anchor_from_text(title)
    print(f"Title: {title}, Generated Anchor: {anchor}")
