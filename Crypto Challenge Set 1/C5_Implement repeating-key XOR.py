#-*- coding:utf-8 -*-
def xor(b1,b2):
    b = bytearray(len(b1))
    print b2
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

b0 = [
    "Burning 'em, if you ain't quick and nimble\n",
    "I go crazy when I hear a cymbal",
      ]
text = "".join(b0)
key = bytearray("ICE"*len(text))
#key有重复或过长无关系
plaintext = bytes(xor(bytearray(text) , key))
print plaintext.encode("hex")