# -*- coding: utf-8 -*-
import islem
import sys
print(islem.topla(4,6))
print(islem.topla(int(sys.argv[1]),int(sys.argv[2])))
for x in dir(islem): #modül icinde kullanilabilecekleri bastirmak icin.
    if "__" not in x:
        print(x)
#birden fazla python kodunu tek bir cati altında import ederek toplayabiliriz.
#sys kütüphanesi ile parametre alarak islem yaptırabilirz.

