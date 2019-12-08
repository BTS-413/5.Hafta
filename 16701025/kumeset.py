# -*- coding: utf-8 -*-
l = [1,2,3] #liste *list  *sıralı
t = (1,2,3) #kayit *tuple *ımmutable
k = {1,2,3,1,2,3} #kume  *set   *sırasız   *tekrar olmaz
k2 = set(l)
k3 = set([1,2,3,1,32,3])
k4 = set('bilgisayarkodlari')#aynilari bastirma
k5 = set('oguzhalitsak')     #siranin bir onemi yoktur
for x in l,t,k,k2,k3,k4,k5:
    print(x)
print(k4|k5) #set union , birlesim, tekrarlı olanları atar.
print(k4-k5) #set diff  , farkı,    k4 olup k5'de olmayan
print(k4&k5) #kesisim   , ortak
print(k4^k5) #exclusive or, iki yonlu kume farkının birlesimi
