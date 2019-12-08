sozluk = {"home" : "ev",
          "book" : "kitap",
          "pen"  : "kalem"
        
        }

print(sozluk["home"])
karakter = {"ad" : "oguz",
            "guc": 80,  
            "silah":"kilic",
            "can":100}
karakter2 = {"ad":"karakter2",
             "guc":70,
             "silah":"kilic",
             "can":100}
def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["guc"]
    vurulan["can"] = vurulan["can"]- eksilen
vur(karakter,karakter2)
vur(karakter2,karakter)
print("karakter1 can : {}".format(karakter["can"]))
print("karakter2 can : {}".format(karakter2["can"]))
#sozluk veri tipi onemli.
