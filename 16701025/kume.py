#kume belirteci yoktur set fonksiyonu kullanilir.
kume = set() # bos kume olusturma
kume = set(["ali","veli","kedi"]) #listeler ile kume olusturabiliriz.
kume = set(("ali","veli",2,"ali")) #demetler ile kume yapabilirz
"""
sayi = 25
kume = set(sayi)
bu sekilde kume olusturulamaz.
"""
print(kume) #kumelerde 1 oge ancak bir kere gosterilir.
print(type(kume))
string = "asfgdshsfdhf"
kume = set(string) # stringlerde kume olarak eklenebilir.
print(kume)
kume = {"ali","veli","kedi",12} #ama bu sekilde bos kume olusturulamaz. kume = set()
kume2 = {"kus","kedi","at","tavuk"}
print(type(kume))

for i in dir(kume):
    if "__" not in i:
        print(i)
kume.add("kus")
#kume.discard("kedi") #varsa cikartir yoksa islem yapmaz.
kume.remove("kedi") #eger kumede yoksa hata verir.
print(kume,kume2)
print(kume.difference(kume2))
print(kume2.difference(kume))
#kume2.difference_update(kume) #kume2'den kus cikti ve bu sekide guncellendi.
#print(kume2)
print(kume2.intersection(kume)) #kume ve kume2 kesisim kumesini basar.







