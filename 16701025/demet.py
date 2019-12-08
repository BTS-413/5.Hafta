demet = () #demet olusturma
demeta = "Bir","Varmis",1,"Yokumus"
print(type(demeta))
a = (["kavun","karpusz","cilek"],)#sona virgul koymazsak liste gibi gorur.
b = (["ali","veli","kedi"],1,2,3,"bes")
print(type(b))
print(b[4])
print(b[0][2]) #demetlerde ekleme cikarma islemi yoktur. daha hizlidir.
#degistirilmesini istemedigimiz seyleri demetler ile eklememizde fayda vardir.
saydemet = (1,2,3,4,5,6,7,8,9,1,1,1)
print(saydemet.count(1))
#sabitleri demetlerde toplama iyi bir fikir olabilir.
del demet #diyerek demet'i silebiliriz
print(demet)
