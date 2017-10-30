# Week5_option

## Meet-in-the-middle attack
[wiki](https://en.wikipedia.org/wiki/Meet-in-the-middle_attack)

meet-in-the-middle attack(!=Man-in-the-middle attack)  
中间相遇攻击：以空间换取时间。
ENC加密函数；DEC解密函数。 \
当攻击者已知明文P与密文C时，攻击者可以穷举所有 k1的组合，将产生出来的第一层密文ENC_k1(P)用大量空间储存下来。再穷举所有k2的组合，将DEC_k2(C)的值与前面储存下来的结果比对，进而得出正确的k1与k2。   
这使得攻击者计算的量从k1与 k2各自的可能组合数相乘，变成相加。
![setch map](https://wikimedia.org/api/rest_v1/media/math/render/svg/549ca6b05f8687821656d9f2f43a9ca214e9da9c)

## 该题思路
详见PDF
主要方法：
构造 x = x0 * B + x1  
先存储2^20个h / (g ^ x1)值，再遍历2^20个x0值

### 跟着超哥的程序学习一波python编程

## python : Multiple-precision Integers
### gmpy
[gmpy2](http://gmpy2.readthedocs.io/en/latest/mpz.html)
 1. divm(...)  
> divm(a, b, m) returns x such that b * x == a modulo m. Raises a ZeroDivisionError exception if no such value x exists.
 适用于a/b，且a/b之前原式有mod的运算
 2. powmod(...)   
> powmod(x, y, m) returns (x ** y) mod m. The exponenent y can be negative, and the correct result will be returned if the inverse of x mod m exists. Otherwise, a ValueError is raised.

### Dictionary
    middle = {}
    middle[0] = 100
    middle: {0:100, 1:101, ..., ...}

    for i in middle:
        print i
        => 0, 1, ...（键值对的键）

### Lists
    middle = []
    middle.append(1)
    middle = [1, 2, ..., ...]

## 编程习惯：
1. 多用函数（直接写一大串下来-ugly，不elegant）
2. 主函数入口

    if __name__ == "__main__":  
        self_test()