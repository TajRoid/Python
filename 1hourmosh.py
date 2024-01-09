# variables
age = 20
price = 19.95
first_name = "Taj"
is_online = False
print()

# input
name = input("what is your name? ")
print("Hello "+name)
birth_year = input("enter yout birth year: ")
age = 2023 - int(birth_year)
print(age)
print("\nKalkulator")
angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")
hasil = float(angka1) + float(angka2)
print("Hasil: "+ str(hasil))

# Strings
course = 'belajar dengan python'
print('dengan' in course)

# Arithmetic Operators
x=100
x+=3
print(x)

# Operator Precedence
x = (10 - 2) * 3
print(x)

# Comparion Operator
x=3!=4
print(x)

# Logical Operators
price = 10
print(not price>100)

# If Statements
temp = input("Masukkan Suhu saat ini: ")
if int(temp) > 30:
    print("panas")
elif int(temp)>20:
    print('wenak')
elif int(temp)>10:
    print('rodok adem')
else:
    print('adem')
print('done')

# Exercise
berat = input("Masukkan berat badan: ")
print("a. Kg\n"
      "b. Lbs")
satuan = input("Kg atau Lbs?: ")
a = float(berat) * 2.2
b = float(berat) / 2.2
if a:
    print("Berat dalam Lbs: ", a)
else:
    print("Berat dalam Kg: ", b)

# While Loops
i = 1
while i<=10:
    print(i*'*')
    i=i+1

# Lists
nama = ['Asok', 'das', 'raf', 'gav', 'ans']
nama[0] = "eh ha'ah lah"
print(nama[0:4])

#Lists Methods
angka = [1,2,3,4,5]
print(len(angka))

# For Loops
angka = [1,2,3,4,5]
for isi in angka:
    print(isi)

# The range() Function
angka = range(0,12, 2)
for item in angka:
    print(item)
for items in range(5):
    print(items)

# Tuples
angka = (1,2,3)
angka.count()