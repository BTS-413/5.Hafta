# -*- coding: utf-8 -*-
l = []
for x in range(10):#istemedigimiz halde bir x degişkeni oluşuyor.
    l.append(x**2)
print(l)
print(x) #x'in tanımlanmamasi lazim o zaman daha verimli olur.
karesi = list(map(lambda y: y**2, range(10))) #her bir liste elemana islem uygulanmasi icin map fonksiyonunu kullandik

print(karesi)
try:         #isimsiz fonksiyon tanimlamak amacımız
    print(y) #burda y degerinin tanimlanmamasi gerek.
except:      #gereksiz kullanimlardan kacinmak için.
    print("Y degeri tanimlanmamis")
def f(x):
    return x+5
l2 = [2,8,3]
print(list(map(f,l2)))#listenin ilk elemanini al fonksiyona sok.ikinci elemani al fonksiyona sok.seklinde ilerletir.f fonksiyonunu al listeye uygula.bunu lamda ile inline yapabiliriz.
print(list(map(lambda z: z+5,l2))) #daha pratik
karesi2 = [c ** 2 for c in range(10)] #bu şekilde kullanirsakda gereksiz tanimlardan kaçınmış oluyoruz.
print(karesi2)
try:
    print(c)
except:
    print("c degeri tanimli degil")
li = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y] #esit olmayanlardan ikili liste olusturdu.
print(li)
#for x in [1,2,3]:
#    for y in [3,1,4]:
#        if x != y:
#            print("x ve y esit degil",x,y)
li2 = [(x,y,z,v) for x in [1,2,3,4] for y in [1,2,3,4]]

