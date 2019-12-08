def scope_test():
    def do_local():
        spam = "local spam"
        print("Localdeyiz: ",spam)
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam" #spam degerini doldurdu
    do_local()         # fonksiyon cagirildigi zaman bütün bilgileri cagirir. fifo
    print("After local assignment:",spam) #fonksiyon bittigi icin test spam kalir.
    do_nonlocal() #hangi degiskenin nerden geldigini anlamak icin önemli
    print("After nonlocal assingment:",spam)
    do_global()
    print("After global assingment:",spam)
scope_test()
print("In global scope:",spam)

