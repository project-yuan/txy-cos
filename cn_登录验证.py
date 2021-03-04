# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

def 打印(a):
    return print(a)
def 输入(a):
    return input(a)


用户名1 = 'cly'
密码1 = '1234'

while 1:
    输入的名字 = 输入('输入你的用户名:')
    if 输入的名字 != 用户名1:
        打印('用户错误 重新输入')
        continue
    打印('用户正确')
    输入密码 = 输入("请输入你的密码:")
    if 输入密码 != 密码1:
        打印('密码错误 重新输入')
        continue
    打印('密码正确，欢迎进入')











