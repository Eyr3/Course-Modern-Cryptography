#coding: utf-8
import re
import gmpy2

'''
dirpath = path.dirname(__file__)
path = os.path.join(dirpath, filepath)
'''

Data = []
for i in range(21):  #0~20
    with open('Frame' + str(i)) as fp:
        data = re.findall('(.{256})(.{256})(.{256})',fp.read().replace('\n',''))
        Data += data

N = [int(n, 16) for n, e, c in Data if int(e, 16)]
C = [int(c, 16) for n, e, c in Data if int(e, 16)]
E = [int(e, 16) for n, e, c in Data if int(e, 16)]
