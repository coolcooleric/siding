'''
Created on Nov 25, 2010

@author: ewang
'''
l1 = [ i ** 2 for i in range(4,10)]
l2 = [ i ** 2 for i in range(10,32)]
for i in range(0,len(l2) - 1):
  if l2[i] % 10 == 0 or l2[i] // 10 % 10 == 0:
    continue;
  h = l2[i] // 100
  m = l2[i] // 10 % 10
  l = l2[i] % 10
  for j in range(i + 1,len(l2)):    
    if l2[j] % 10 == 0 or l2[j] // 10 % 10 == 0:
      continue;
    hh = l2[j] // 100
    mm = l2[j] // 10 % 10
    ll = l2[j] % 10
    if h * 10 + hh in l1 and m * 10 + mm in l1 and l * 10 + ll in l1:
      print('{0}{1}{2},{3}{4}{5}'.format(h,m,l,hh,mm,ll))

    if hh * 10 + h in l1 and mm * 10 + m in l1 and ll * 10 + l in l1:
      print('{0}{1}{2},{3}{4}{5}'.format(hh,mm,ll,h,m,l))
