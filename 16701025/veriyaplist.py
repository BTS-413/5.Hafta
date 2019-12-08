l = [1,2,3,4,2,2]
print(l)
l.append(55) # sonuna ekler
l.insert(2,111) # index i 2 olan yere 111'i ekler
l.append(111) #2 tane 111 olursa removeda ilk buldugunu siler 2.ciyi ellemez
l.remove(111) # 111'i listeden siler.
l.pop() #son ekleneni cikartiyor. silme veya geri alma islemi gibi dusunulebilir veri yapilarinda siklikla kulllanilir.
print(l)
print(l.index(3)) # 3 sayisinin bize indexini bulur.
print(l.count(2)) #listede 2 nin kac tane oldugunu saydiriyor.
l2 = [3,4,5]
l.extend(l2)
l.sort()
print(l)



