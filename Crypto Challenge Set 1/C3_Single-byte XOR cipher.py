#-*- coding:utf-8 -*-
def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
    scores = 0
    for c in s.lower():
        if c in freq:
            scores += freq[c]
    return scores
#利用前定义的字母频率得分表，对字符串s中各字符得分累加，求得字符串终总分scores并返回

def break_sb_xor(b1):
    max_score = 0
'''
首先，遍历ASCII表中256个字符，利用#2的异或函数xor(b1,b2)；
然后，分别对密文按位进行异或，得到各组字符串plaintext;
再求得每组plaintext的计分函数score(s)值scores；
最后比较各组scores值，取最大得分，对应的字符即为key.
'''
        for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        pscore = score(plaintext)

        if pscore > max_score or not max_score:
            max_score = pscore
            r_plaintext = plaintext
            key = chr(i)
    return key, r_plaintext

b1 = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
print break_sb_xor(b1)
