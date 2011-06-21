'''
Created on Nov 11, 2010

@author: ewang
'''
import math
radius = 10
pix = radius * 2 + 1

l = [0] * pix
# l.append([1,2]*3)
cl = []
for i in range(pix):
    cl.append(l[:])
print(cl)

for i in range(pix):
    y = radius ** 2 - i ** 2    
    if y < 0:
        continue
    else:
        h = int(round(math.sqrt(y)))
        #print(i,h)
        cl[radius + i][radius + h] = 1
        cl[radius - i][radius + h] = 1        
        cl[radius + i][radius - h] = 1   
        cl[radius - i][radius - h] = 1  
              
for i in range(pix):
    for j in range(pix):
        if cl[i][j]:
            print('-',sep='',end='')
        else:            
            print('  ',sep='',end='');
    print('\n',sep='',end='')
