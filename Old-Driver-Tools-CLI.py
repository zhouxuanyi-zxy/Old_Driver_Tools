# Old-Driver-Tools Python Edition
# Author: zhouxuanyi-zxy
# Licence: MIT Licence
# Version: v0.5b1
# Language: Python
# 2023.1.3-v0.1b
# 2023.1.23-v0.2b
# 2023.1.23-v0.3b
# 2023.1.31-v0.4b
# 2023.2.1-v0.5b1
# 2023.2.25-v0.5b2
VERSION = "v0.5b2"
# 在0.4b后更改为正确的版本命名方式
import base64
import os
import sys
import codecs 
try:
    import pyperclip    # 复制到剪切板
    import gmssl    
    import chardet
except ModuleNotFoundError:    # 如果没有此包,则使用国内pip源安装
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyperclip")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gmssl")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple chardet")
    os.system("python {}".format(sys.argv[0]))    # 自动重启程序
    # sys.exit()
from gmssl import sm2

# 导入结束,程序开始
base64_decode_encode = "" # base64模式判断
utf_8_decode_encode = "" # UTF-8模式判断
sm2_decrypt_encrypt = "encrypt"
use_cli = "1"    # 给我调试新功能时用的 1=true 0=false
user_input = ""    # 用户输入

def base64_de_en(CLI_base64_input=None):    # base64编/解码具体实现
    global user_input,base64_decode_encode
    user_input = CLI_base64_input
    user_input = bytes(user_input,encoding="utf-8")    # 转换为bytes类型
    # print(user_input)
    try:
        if base64_decode_encode == "encode":    # 编码
            base64_out = base64.b64encode(user_input)    # 编码
        elif base64_decode_encode == "decode":               # 解码
            base64_out = base64.b64decode(user_input)    # 解码
        if chardet.detect(base64_out)["encoding"] == "utf-8":    # 有可能出错,后续增加可信度检测以及跳过检测
            # pyperclip.copy(base64_out.decode("utf-8"))
            print(base64_out.decode("utf-8"))
        else:
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
        utf_8_decode_swap = user_input[1::]
        # print(utf_8_decode_swap)
        utf_8_decode_swap = codecs.escape_decode(utf_8_decode_swap, "hex-escape")    # tuple
        # print(utf_8_decode_swap)
        utf_8_out = utf_8_decode_swap[0]    # bytes
        # print(type(utf_8_out))
        utf_8_out = utf_8_out.decode("utf-8")    # 终于结束了
    # pyperclip.copy(utf_8_out)
    print(utf_8_out)

def sm2_de_en():    # 初步框架,无法使用
    global sm2_decrypt_encrypt,user_input
    # user_input = input()
    user_input = b'123'
    # user_input = bytes(user_input,encoding="utf-8")
    print(user_input)
    sm2_output = ""
    pubric_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'    # 公钥
    SM2_PUBLIC_KEY = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'    # 公钥
    SM2_PRIVATE_KEY = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'    # 私钥
    private_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'    # 私钥
    sm2_crypt = sm2.CryptSM2(public_key=pubric_key,private_key=private_key)
    if sm2_decrypt_encrypt == "encrypt":
        sm2_output = sm2_crypt.encrypt(user_input.encode("utf-8"))
    elif sm2_decrypt_encrypt == "decrypt":
        sm2_output = sm2_crypt.decrypt(user_input).decode("utf-8")
    print(sm2_output)

# sm2_de_en()
if __name__ == "__main__" and use_cli == "1":
    CLI_input = ""
    try:
        if sys.argv[1] == "base64":
            if sys.argv[2] == "decode":
                CLI_input = sys.argv[3]
                base64_decode_encode = "decode"
            elif sys.argv[2] == "encode":
                CLI_input = sys.argv[3]
                base64_decode_encode = "encode"
            else:
                raise IndexError()
            base64_de_en(CLI_input)
        elif sys.argv[1] == "utf-8":
            if sys.argv[2] == "decode":
                CLI_input = sys.argv[3]
                utf_8_decode_encode = "decode"
            elif sys.argv[2] == "encode":
                CLI_input = sys.argv[3]
                utf_8_decode_encode = "encode"
            else:
                raise IndexError()
            utf_8_de_en(CLI_input)
        elif sys.argv[1] == "help" or sys.argv[1] == "h":
            # print("\033[32m \033[0m")    模板
            print('''
 _____ _     _       ______    _      _                     _____           _ 
|  _  | |   | |      |  _  \  | |    (_)                   |_   _|         | |
| | | | | __| |______| | | |__| |_ __ ___   _____ _ __ ______| | ___   ___ | |
| | | | |/ _` |______| | | / _` | '__| \ \ / / _ \ '__|______| |/ _ \ / _ \| |
\ \_/ / | (_| |      | |/ / (_| | |  | |\ V /  __/ |         | | (_) | (_) | |
 \___/|_|\__,_|      |___/ \__,_|_|  |_| \_/ \___|_|         \_/\___/ \___/|_|
''')
            print("\033[32mOld-Driver-Tool Python Edition\033[0m")
            print("\033[32mVersion:\033[0m",VERSION)
            print("\033[32mby zhouxuanyi-zxy\033[0m")
            print("用法/Usage:")
            print("python Old-Driver-Tools-CLI.py [base64/utf-8] [decode/encode] [内容]")
            print("帮助/help:")
            print("python Old-Driver-Tools-CLI.py h")
        else:
            raise IndexError()
    except IndexError:
        print('''用法/Usage:
            python Old-Driver-Tools-CLI.py [base64/utf-8] [decode/encode] [内容]
            ''')
        print('''帮助/help:
            python Old-Driver-Tools-CLI.py h
        ''')
        
