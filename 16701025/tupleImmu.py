# -*- coding: utf-8 -*-
l = [1,2,3]
t = (1,2,3)
print(l)
print(t)
l[2] = 10
print(l)
try:
    t[2] = 5
except:
    print("Tuple immutable'dir")
x , y ,z = t
print(x)
print(z)
z = 10
print(t)
t = (x,y,z)
print(t)             #tuplelar üzerinde degisiklik yapilamaz.
v = ([1,2,3],[3,2,1])#tuple aslında pointer tutuyor.
v[0][1]=100 #tuple'ın icindeki listeye degisklik yapilabilr.
print(v)
print(type(v))
