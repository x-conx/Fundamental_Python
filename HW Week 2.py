#buat sebuah fuction yang menerima sebuah kata
#reverse semua huruf dari kata itu
###########
#SOAL 1#
#########
inf = input('Masukkan kalimat: ')
inf = list(inf)
inf.reverse()
inf = ''.join(inf)
print(inf)


##############
### SOAL 2 ###
##############
#remove 0 and 1 and summary the list
g = [[2,4,0,1,11],[7,0,3,1,7,9],[5,0,3,2,1]]

def rand(x):
    for j in range(len(x)):
        newg = list(x[j])
        s = newg.index(0)
        ss=newg.pop(s)
        z = newg.index(1)
        dz=newg.pop(z)
        print(sum(newg))
    j+=1

rand(g)

# print(len(g[0]))
# print(g[0][1])
# n = list(g[0])
# print(n)
# o = n.index(1)
# print(o)
