buah = {'Apel':'5000>Apel',
 'Jeruk':'8500>Jeruk',
 'Mangga':'7800>Mangga',
 'duku':'6500>Duku'}

data = list(buah.values())
data.sort()

for x in data:
    print(x)

buaha =[5000,8500,7800,6500]
rerata= sum(buaha)/len(buaha)
print('rata rata = ',+int(rerata))


while True:
    print('Masukkan nama buah:', end='')
    nama = input()
    print('Masukan kg: ', end='')
    kilo = int(input())
    if nama == '':
        break


    if nama in hargabuah:
        print('Harga: Rp',hargabuah[nama]+kilo)

