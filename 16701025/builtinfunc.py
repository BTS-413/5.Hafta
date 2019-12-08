#abs fonksiyonu mutlak degeri alir.
sayi = -20
print('Sayinin eski degeri -20', abs(sayi))
flosayi = -33.33
print('Sayinin eski degeri -33.33', abs(flosayi))
topla = (3 - 4)
print('Sayi islemi sonucu',abs(topla))
#round sayiyi yuvarlamak icin
topla = (32.23 + 12.43)
print('Yuvarlanmis Toplam: {0} \nGercek toplam:{1}'.format(round(topla),float(topla)))
#all True False kontrolü yapmak icin
list = [7,8,9,4] #sıfır haric bütün sayilar True döner
print(all(list))
list.append(0) #0'ı ekledigimiz icin False degeri dönmeye başlıcak
print(all(list))
list = ['kus','kedi']
print(all(list))
list.append('') #bos karakter dizisi eklendigi icin false doncektir.
print(all(list))
#any bütün degerlerin icinde bir tane true olması yeter true dönmek icin
print(any(list)) #listemizde 1 tane bos karakter dizisi olmasına ragmen true basdi.
#bool nesnenin bool degerini verir.
print(bool(0))
print(bool(1))
#list() list tipinde veri olusturmak icin.
#set()  verileri kume yapmak icin
#tuple  veriyi demet'e donusturur.
#complex() karmasık sayilar ile islem yaparken kullanilir.
#map fonksiyonu bir veri yapısı üzerinde coklu degisiklik yapmak icin kullanirlir.
del list
liste = [1,2,3,4]
def topla(a):
    return a+5
c = map(topla,liste)
print(list(c))
#filter degeri true olanları listeyee atar
def cift(a):
    return a%2==0
c=list(filter(cift,liste)) #fonksiyndan dönen true degerleri ile bize
print(c)                   #bir liste olusturmasi icin ise yarar.

#zip fonksiyonu 2 listeyi birlestirmek icin bire bir
liste2 = ['10','11','12','13','14','15','16']
print(list(zip(liste,liste2))) #matrix islemlerinde llazim olarabilir kullanısli
#enumerate() fonksiyonu veri elemanlarını numaranldırmaya yarar.
print(list(enumerate("oguzhalitsak")))
#len fonksiiyonu nesnelerin uzunluklarını verir.
isim = "oguzhalitsak"
print(len(isim))
#id fonksiyonu her nesnein bir id'si vardı onu ögrenmemize yarar.
print(id(isim))
#pow fonksiyonu birinci sayinin ikinci sayi kadar üssünü alır.
print(pow(2,3))
