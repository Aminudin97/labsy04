print ("\n==============================================\n")
print ("\t\tLATIHAN\t\t")
print ("\n==============================================\n")

List = [2, 4, 8, 16, 32]



#Akses List

print("Akses List")

Data1 = List[2]

Data2 = List[1:4]

Data3 = List[-1]

print(Data1)

print(Data2)

print(Data3)



#Ubah Elemen List

print("Ubah Elemen List")

print(List)

List[4] = 80

print(List)

List[4:6] = [64, 128]

print(List)



#Menambahkan Elemen List

print("Menambahkan Elemen List")

print(List)

a = List

print(a)

b = a[2:4]

print(b)

b.append(64)

b.extend([128, 256, 512])

print(b)

c = a + b

a.extend(b)

print(c)

