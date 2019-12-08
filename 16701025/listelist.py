# -*- coding: utf-8 -*-
#list of list
l = [1,2,3]
m = [[1,3,5],[3,4,5],l]
print(m)
#l[1]=100
#birden fazla yapida eleman tutmaya yariyor.
#birinci kolonda maaslar ikinci kolonda adresler gibi birden fazla veri lazım oldugu zaman kullanilir.
p = [[row[i] for row in m] for i in range(3)] #matrixi transpoze ettik.
#birinci satirin ilk elemanini alıyor. bir row olusturuyor birinci elemanlardan.
print(p)


