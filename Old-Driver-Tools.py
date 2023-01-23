# Old-Driver-Tools Python Edition
# Author: zhouxuanyi-zxy
# Licence: MIT Licence
# Version: v0.2b
# Language: Python
# 2023.1.3-v0.1b
# 2023.1.23-v0.2b

import base64
import os
import codecs
try:
    import pyperclip    # 复制到剪切板
except ModuleNotFoundError:    # 如果没有此包,则使用国内pip源安装
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyperclip")
    os.system("python Old_Driver_Tools.py")    # 自动重启程序
    exit()
# 导入结束,程序开始
base64_decode_encode = "encode" # base64模式判断
utf_8_decode_encode = "decode" # UTF-8模式判断
user_input = ""    # 用户输入
mode_select = ""
def start():
    global mode_select
    print("")
    mode_select = input()
    if mode_select == "1":
        base64_de_en()
    elif mode_select == "2":
        utf_8_de_en()

def base64_de_en():    # base64编/解码具体实现
    global user_input,base64_decode_encode
    user_input = input("")
    if user_input == "exit":
        start()
    else:
        user_input = bytes(user_input,encoding="utf-8")    # 转换为bytes类型
    try:
        if base64_decode_encode == "encode":    # 编码
            base64_out = base64.b64encode(user_input)    # 编码
        elif base64_decode_encode == "decode":               # 解码
            base64_out = base64.b64decode(user_input)    # 解码
        # pyperclip.copy(str(base64_out)[2:-1:])
        print(str(base64_out)[2:-1:])
        base64_de_en()
    except:
        print("Error!")
        
def utf_8_de_en():    # UTF-8编/解码
    global utf_8_decode_encode,user_input
    user_input = input()
    if utf_8_decode_encode == "encode":
        utf_8_out = user_input.encode("utf-8")
    elif utf_8_decode_encode == "decode":
        utf_8_decode_swap = user_input[2:-1:]
        # print(utf_8_decode_swap)
        utf_8_decode_swap = codecs.escape_decode(utf_8_decode_swap,"hex-escape")
        # print(utf_8_decode_swap)
        utf_8_out = utf_8_decode_swap[0]
        # print(type(utf_8_out))
        utf_8_out = utf_8_out.decode("utf-8")
    # pyperclip.copy(utf_8_out)
    print(utf_8_out)
utf_8_de_en()
# if __name__ == "__main__":
#     start()