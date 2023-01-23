# Old-Driver-Tools Python Edition
# Author: zhouxuanyi-zxy
# Licence: MIT Licence
# Version: v0.3b
# Language: Python
# 2023.1.3-v0.1b
# 2023.1.23-v0.2b
# 2023.1.23-v0.3b

import base64
import os
import sys
import codecs 
try:
    import pyperclip    # 复制到剪切板
    import gmssl    
except ModuleNotFoundError:    # 如果没有此包,则使用国内pip源安装
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyperclip")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gmssl")
    os.system("python Old_Driver_Tools.py")    # 自动重启程序
    exit()
from gmssl import sm2
# 导入结束,程序开始
base64_decode_encode = "encode" # base64模式判断
utf_8_decode_encode = "decode" # UTF-8模式判断
user_input = ""    # 用户输入

def base64_de_en(CLI_base64_input=None):    # base64编/解码具体实现
    global user_input,base64_decode_encode
    user_input = str(CLI_base64_input)
    user_input = bytes(user_input,encoding="utf-8")    # 转换为bytes类型
    try:
        if base64_decode_encode == "encode":    # 编码
            base64_out = base64.b64encode(user_input)    # 编码
        elif base64_decode_encode == "decode":               # 解码
            base64_out = base64.b64decode(user_input)    # 解码
        # pyperclip.copy(str(base64_out)[2:-1:])
        print(str(base64_out)[2:-1:])
    except:
        print("Error!")
        
def utf_8_de_en(CLI_utf8_input=None):    # UTF-8编/解码
    global utf_8_decode_encode,user_input
    user_input = str(CLI_utf8_input)
    # print(type(user_input),user_input)
    if utf_8_decode_encode == "encode":
        utf_8_out = user_input.encode("utf-8")
    elif utf_8_decode_encode == "decode":
        utf_8_decode_swap = user_input[2:-2] # 输入格式 推荐，但是最好写个函数校验一下 b’\xe4\xbd\xa0\xe5\xa5\xyd’
        # print(utf_8_decode_swap)
        utf_8_decode_swap = utf_8_decode_swap.encode("unicode_escape").decode("utf-8").replace("\\\\x", "%") # 转为url编码形式
        from urllib import parse
        utf_8_out = parse.unquote(utf_8_decode_swap) # 终于结束了
    # pyperclip.copy(utf_8_out)
    print(utf_8_out)
# utf_8_de_en()
# base64_de_en()

def sm2_decrypt_encrypt():
    SM2_PUBLIC_KEY = ""    # 公钥
    SM2_PRIVATE_KEY = ""    # 私钥
    sm2_crypt = sm2.CryptSM2(public_key=SM2_PUBLIC_KEY,private_key=SM2_PRIVATE_KEY)

if __name__ == "__main__":
    CLI_input = ""
    if sys.argv[1] == "base64":
        if sys.argv[2] == "decode":
            CLI_input = sys.argv[3]
            base64_decode_encode = "decode"
        if sys.argv[2] == "encode":
            CLI_input = sys.argv[3]
            base64_decode_encode = "encode"
        base64_de_en(CLI_input)
    elif sys.argv[1] == "utf-8":
        if sys.argv[2] == "decode":
            CLI_input = sys.argv[3]
            utf_8_decode_encode = "decode"
        if sys.argv[2] == "encode":
            CLI_input = sys.argv[3]
            utf_8_decode_encode = "encode"
        utf_8_de_en(CLI_input)
