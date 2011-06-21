'''
Created on Nov 10, 2010

@author: ewang
'''
import sys
l1 = list(str(sys.argv[1]))
l2 = list(str(sys.argv[2]))
mul = []
for i in range(len(l1) + len(l2)):
    mul.append(0)

def add(val, i):
    tmp = val + mul[i]
    if tmp < 10:
        mul[i] = tmp
    else:
        mul[i] = tmp % 10
        add(tmp // 10, i + 1)

l1.reverse()
l2.reverse()
for i in range(len(l1)):
    for j in range(len(l2)):
        add(int(l1[i]) * int(l2[j]), i + j)

mul.reverse()
if mul[0] == 0:
    mul = mul[1:]
print("the result:", end='')
for i in mul:
    print(i, sep='', end='')
print();

