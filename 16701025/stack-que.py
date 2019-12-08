# -*- coding: utf-8 -*-
"""

#yigin icin listeler
#bir yigin seklinde ilk koydunumuz en altta
#ilk giren son cikar
#liste fonksiyonlari ile yapicaz

l = [1,2,3]
l.append(55) # liste sonuna eklenicek
print(l)
l.pop() #stacklarde pop ve push kullanicaz
        #burda pop en sondaki elemani alicak
print(l)
l.pop() #sondaki elemandan silmeye baslar
        #yigindan cikariyoruz.
print(l)
l2 = [44,55,66]
l2.append(77)
# print(l2.popleft()) bunun icin kutuphane lazim
#bunun yerine index numarasi verilerek pop left yapilir kutuphaneye gerek kalmaz.
print(l2.pop(0))
#pop left ise basdan eleman aliyor.
#stacklarde queue yapisi kullanilir.bunun icin kutuphane kullanicaz.
from collections import deque
l3 = deque([11,12,23,45]) #deque yapisinda bastiriyor.
print(l3)
l3.append(67)
print(l3.popleft()) #basdan ccikarma yapmak icin
print(l3)           #sira ilk eklenen ilk cikar
                    #stackde ise yeni eleman alinir.
"""
l = []
#x degiskeni otomatik tanimlaniyor.ve verilen degere kadar dondu 11 olunca ciktı ama bu istemedigimiz bir durum.
for x in range(1,11): #birden baslamasi icin 1,11 arasini aldik
    l.append(x**2) # ** ustu anlamina geliyor.
print(l)
kara = list(map(lambda x: x**2, range(1,11))) 
#lambda onemli(fonksiyonel programlama trend bu ara) matematiksel denklem yazar gibi program yazmak anlamina gelir.deger icermeyen gecisler lambda boslugu ifade eder.isimsiz bir fonksiyon tanimlamak icin.
#function pointer olarakda kullanilir.bir fonksiyonu al listenin butun elemanlarina uygula.
def f(x):
    return x+5
l2 = [2,8,3] #map ile her elemani fonksiyono sokup ciktisini listeye gonderdik.map fonksiyonu cok onemli
print(l2)
print(list(map(f,l2))) # verilen uzerine fonksiyonun tek tek uygulanmasi icin map fonksiyonu kullaniliyo
#map fonksiyonu listenin icindeki elemanlara verilen fonksiyonun islemini tek tek uygular ve yeni liste elamanlarda butun degisiklikler isler.
#lambda isimsiz fonksiyon tanimlamamiza yariyor.
print(list(map(lambda y:y+5,l2))) #lamda kullanarak fonksiyon acmaya gerek duymadanda islemi yaptirabiliyoruz.
#isimsiz ve gecici bir fonksiyon yaratmak icin kullanilan bir fonskyion 
# artik x degeri yok
#print(y) # gereksiz olarak y degisknini tutmuyor artik. satir icinde tanimlanir ve satir bitince yok olur. 
print(x) # gereksiz bir x degeri var diger turlu.

l3 = [z**2 for z in range(10)] #buda bir kullanim seklidir.
print(l3)

#print(z) #python2 de tanimlanirken python3 de tanimlanmiyor.
l4 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l4)


