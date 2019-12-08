#list = ['kedi',1,2,3]
#yeni_list = list.copy()
#yeni_list.append('kus')
#
#print('yeni liste: ', yeni_list)
#print('eski lise : ', list)
#x = range(0,3)
#for n in x:
#    print(n)
#tuslar = [[1,2,3],[4,5,6],[7,8,9]]
#for tus in tuslar:
#    print(tus)
#
#for i in range(len(tuslar)):
#    for j in range(len(tuslar[i])):
#        print(tuslar[i][j],end=" ")
#    print()

m = 4
n = 5
a = [[0 for x in range(n)] for x in range(m)]
a.append([1,2,3,4,5])
for tab in a:
    print(tab)

