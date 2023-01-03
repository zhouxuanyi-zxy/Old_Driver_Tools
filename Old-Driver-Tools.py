# Old-Driver-Tools Python Edition
# Author: zhouxuanyi-zxy
# Licence: MIT Licence
# Version: v0.1b
# Language: Python
# 2023.1.3-v0.1b

import base64
import os
try:
    import pyperclip    # 复制到剪切板
except ModuleNotFoundError:    # 如果没有此包,则使用国内pip源安装
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyperclip")
    os.system("python Old_Driver_Tools.py")    # 自动重启程序
    exit()
# 导入结束,程序开始
base64_decode_encode = "" # base64模式判断
utf_8_decode_encode = "" # UTF-8模式判断
user_input = ""    # 用户输入
def base64_de_en():    # base64编/解码具体实现
    global user_input,base64_decode_encode
    user_input = input("")
    user_input = bytes(user_input,encoding="utf-8")    # 转换为bytes类型
    try:
        if base64_decode_encode == "encode":    # 编码
            base64_out = base64.b64encode(user_input)    # 编码
        elif base64_decode_encode == "decode":    # 解码
            base64_out = base64.b64decode(user_input)    # 解码
        pyperclip.copy(str(base64_out)[2:-1:])
        print(str(base64_out)[2:-1:])
    except:
        print("Error!")

def utf_8_de_en():    # UTF-8编/解码(别用,用了就废)
    global utf_8_decode_encode
    utf_8_user_input = input()
    if utf_8_decode_encode == "encode":
        utf_8_out = utf_8_user_input.encode("utf-8")
    elif utf_8_decode_encode == "decode":
        utf_8_user_input = bytes(input())
        # utf_8_decode_swap = user_input.encode("utf-8")
        # utf_8_decode_swap = bytes(utf_8_decode_swap.decode("utf-8"))
        utf_8_decode_swap = utf_8_user_input.encode().decode("utf-8")
        utf_8_out = utf_8_decode_swap.encode("utf-8").decode()
    print(utf_8_out)
base64_de_en()