#*-* coding:utf-8 *-*
from collections import defaultdict

'''
本身提供了默认值功能的字典，defaultdict类的初始化函数
接受一个类型作参数，当访问的键不存在时，可实例化一个值作为默认值
这种形式的默认值只有在通过dict[key]或dict._getitem_(key)访问时才有效
'''

def repeated(buffer, block_l = 16):
    reps = defaultdict(lambda:-1)
    #每次循环，为buffer中各block的reps值均赋值-1

'''
已知一个buffer中，存在多个字母块(block)，且单个明文字母块长度为block_l=16byte，
利用这一串16byte的bytes流作为该block的标识，每出现一个标识，就为其reps[block]（初值为-1）赋值+1，
当在一个buffer内block重复出现，则reps[block]值>0.
'''

    for i in range(0, len(buffer), block_l):
        block = bytes(buffer[i : 1+block_l])
        reps[block] += 1
    return sum(reps.values())
...
sum([x,y,z])=x+y+z //x,y,z is num
reps.values()=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  //经计算得：非AES-ECB加密buffer的value值为18个0
ECB：reps.values()=[0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0]  //经计算得：AES-ECB加密buffer的value值中0个数减少，并出现2个3
...

max_reps = 0
ecb_ciphertext = ""

for ciphertext in list(open("8.txt" , "r")):
    ciphertext = ciphertext.rstrip()
    # rstrip()删除string字符串末尾的指定字符（默认为空格）,常用在读取文件中字符串时
    reps = repeated(bytearray(ciphertext))
    
'''
由于16进制编码不会出现块重复的现象，即reps.value为18个0，
而经AES-ECB加密的buffer会出现reps.value值>0的现象，
因此，只要对reps.value中各值求和，大于0者对应buffer，即为经AES-ECB加密的密文块.
'''

    if reps > max_reps:
        max_reps = reps
        ecb_ciphertext = ciphertext

print ecb_ciphertext
