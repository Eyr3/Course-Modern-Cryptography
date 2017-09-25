#-*-coding:utf-8-*-
def xor(b1, b2):
    b = bytearray(len(b1))
    #新建一个字符串 len(b1)=len(b2)=18
    #b = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    for i in range(len(b2)):
        b[i] = b1[i] ^ b2[i]
        #异或需要按位一位一位异或
    return b

b1 = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
#b1 = b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'
b2 = bytearray.fromhex("686974207468652062756c6c277320657965")
#b2 = b"hit the bull\'s eye"

b = bytes(xor(b1, b2))
#b = the kid don't play

print b.encode("hex")
#746865206b696420646f6e277420706c6179