#-*- coding: utf-8 -*-
import hashlib
import itertools
import time

pw = '67ae1a64661ac8b4494666f58c4822408dd0a3e4'
start = time.clock()

#data = str(list(product(base, repeat = 8)))
#hash_sha1 = hashlib.sha1(data)
#if (hash_sha1 == pw):
#    print data

for a in ['5','%']:
    for b in ['8','(']:
        for c in ['=','0']:
            for d in ['Q','q']:
                for e in ['w','W']:
                    for f in ['i','I']:
                        for g in ['*','+','~']:
                            for h in ['N','n']:
                                base = a+b+c+d+e+f+g+h
                                for i in itertools.permutations(base, 8):  #生成列表
                                    data = ''.join(i)  #列表转换为换行的字符串
                                    hash_sha1 = hashlib.sha1(data).hexdigest()
                                    if (str(hash_sha1) == pw):
                                        print data
                                        break

elapesd = (time.clock() - start)
print("Time used:", elapesd)