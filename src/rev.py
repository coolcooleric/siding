'''
Created on Nov 10, 2010

@author: ewang
'''
def rev(list):
    for i in range((len(list)>>2)+1):
        list[i],list[len(list)-1-i] = list[len(list)-1-i],list[i]
        
s = 'amanaplanacanalpanama'
b = 'before:{0:<6}'.format(s)
print(b)  
      
l = list(s)
rev(l)
print('after:',''.join(l))