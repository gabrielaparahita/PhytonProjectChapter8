# langkah kerja 1
print('================langkah kerja 1================')
a = 'a = [1,5,6,3,6,9,11,20,12]'
b = 'b = [7,4,5,6,7,1,12,5,9]'
print(a)
print(b)

# langkah kerja 2
print('================langkah kerja 2================')
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)

#langkah kerja 3
print('================langkah kerja 3================')
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
a.append(4)
b.append(8)
print(a)
print(b)

# langkah kerja 4
print('================langkah kerja 4================')
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
a.sort()
b.sort()
print(a)
print(b)

# langkah kerja 5
print('================langkah kerja 5================')
c = 'c = [1,5,6,3,6,9,11,20]'
d = 'd = [15,5,6,10,7,1,12,5]'
print(c)
print(d)

# langkah kerja 6
print('================langkah kerja 6================')
c = [1,5,6,3,6,9,11,20]
d = [15,5,6,10,7,1,12,5]

q=(c[0]*d[0])
w=(c[1]*d[1])
e=(c[2]*d[2])
r=(c[3]*d[3])
t=(c[4]*d[4])
y=(c[5]*d[5])
u=(c[6]*d[6])
i=(c[7]*d[7])
print('e = [',q,w,e,r,t,y,u,i,']')

# langkah kerja 7
print('================langkah kerja 7================')
myList= [q,w,e,r,t,y,u,i]
myTuple= tuple(myList)
print('e =',myTuple)

myTuple= [q,w,e,r,t,y,u,i]
myList= list(myTuple)
print('e =',myList)

# langkah kerja 8
print('================langkah kerja 8================')
may = [15, 25, 36, 30, 42, 9, 132, 100]
print('Nilai min elemen e = ',min(may))
print('Nilai max elemen e = ',max(may))
print('Jumlah seluruh elemen e = ',len(may))
