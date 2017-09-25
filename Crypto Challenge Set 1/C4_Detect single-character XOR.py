#-*- coding:utf-8 -*-
'''
4.txt共有327行，按行读取，依据所有值最大的解密。
'''

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

def break_sb_xor():
    max_score = 0

    for line in open("4.txt", "r"):
        line = line.rstrip()
        #rstrip()删除string字符串末尾的指定字符（默认为空格）
        b1 = bytearray.fromhex(line)

        for i in range(256):
            b2 = [i] * len(b1)
            plaintext = bytes(xor(b1, b2))
            pscore = score(plaintext)

            if pscore > max_score or not max_score:
                max_score = pscore
                r_plaintext = plaintext
                key = chr(i)
    return key, r_plaintext

print break_sb_xor()