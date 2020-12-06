buah = {'Apel':'5000',
     'Jeruk':'8500',
     'Mangga':'7800',
     'duku':'6500'}

while True:
    print('Nama buah yang dibeli: ', end='')
    nama = input()

    if nama == '':
        break

    if nama in buah:
        print('Harga: ', buah[nama])
    else:
        print('Nama buah' + nama +'beluam ada daftar harga')
        harga = int(input())

        buah[nama]=harga
        print('yey')
