#*-* coding:utf-8 *-*
from collections import defaultdict

'''
本身提供了默认值功能的字典，defaultdict类的初始化函数
接受一个类型作参数，当访问的键不存在时，可实例化一个值作为默认值
这种形式的默认值只有在通过dict[key]或dict._getitem_(key)访问时才有效
'''

def repeated(buffer, block_l = 16):
    reps = defaultdict(lambda:-1)
    for i in range(0, len(buffer), block_l):
        block = bytes(buffer[i : 1+block_l])
        reps[block] += 1
    return sum(reps.values())

max_reps = 0
ecb_ciphertext = ""

for ciphertext in list(open("8.txt" , "r")):
    ciphertext = ciphertext.rstrip()
    # rstrip()删除string字符串末尾的指定字符（默认为空格）,常用在读取文件中字符串时
    reps = repeated(bytearray(ciphertext))
    if reps > max_reps:
        max_reps = reps
        ecb_ciphertext = ciphertext

print ecb_ciphertext