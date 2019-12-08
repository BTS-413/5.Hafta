# -*- coding: utf-8 -*-
#key-value iliskisi
l = [1,19,3,2,1]
l[3] #her degeri bir sayiya atıyor aslında herhangi bir sayi vererekde elemana ulasabilriyorum.
tel = {'oguz':1235, 'ali':4567}
print(tel['oguz']) #sayilar yerine, benim tanimladigim degerler ile degistirmek.
d = dict([('sape',4123),('guido',4125),('kasl',4521)])
print(d)
print(type(d))
print(type(tel))

for k, v in d.items():
    print(k,v)
for i,v in enumerate(['tic','tac','toe']): #listeyi indexli bir şekilde yazdirmak icin
    print(i,v)

cevaplar = ['isim','görev','sevdiginiz renk']
sorular  = ['oguz','ögrenci','mor']
for q,a in zip(cevaplar,sorular):#zip metodu iki liste verilerini birleştirmek icin
    print("Merhaba {0}niz, {1}".format(q,a))
for i in reversed(range(1,10,2)):
    print(i)

