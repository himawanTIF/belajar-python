# Operasi Komparasi
""" Setiap hasil dari operasi komparasi adalah Boolean.
    Notasi-notasi yang ada pada operasi komparasi:
    > (Lebih besar dari)
    < (Kurang dari)
    >= (Lebih besar dari sama dengan)
    <= (Kurang dari sama dengan)
    == (Sama dengan)
    != (Tidak sama dengan)
    is ()
    is not ()
"""
a = 2
b = 4

# Lebih besar dari >
print("----- Lebih Besar Dari > -----")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 4
print(b, ">", 4, "=", hasil)

# Kurang dari <
print("----- Kurang Dari < -----")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 4
print(b, "<", 4, "=", hasil)

# Lebih besar dari sama dengan >=
print("----- Lebih besar dari sama dengan >= -----")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 4
print(b, ">=", 4, "=", hasil)

# Kurang dari sama dengan <=
print("----- Kurang dari sama dengan <= -----")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 4
print(b, "<=", 4, "=", hasil)

# Sama dengan ==
print("----- Sama dengan == -----")
hasil = a == 3
print(a, "==", 3, "=", hasil)
hasil = b == 3
print(b, "==", 3, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

# Tidak Sama dengan !=
print("----- Tidak Sama dengan != -----")
hasil = a != 3
print(a, "!=", 3, "=", hasil)
hasil = b != 3
print(b, "!=", 3, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)

print('\nOperasi komparasi "is" dan "is not"\n')
# 'is' dan 'is not' sebagai komparasi object identity
""" A = 5
    A bisa disebut sebagai object
    5 bisa disebut Literal
    'is' pada python terbaru hanya digunakan untuk membandingkan object identity
"""
print('Object identity "is"')
x = 5 # Assignment membuat object
y = 5
print('Nilai x = ', x, ', id = ', hex(id(x)))
print('Nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('\nObject identity "is"')
x = 5 # Assignment membuat object
y = 6
print('Nilai x = ', x, ', id = ', hex(id(x)))
print('Nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('\nObject identity "is not"')
x = 5 # Assignment membuat object
y = 5
print('Nilai x = ', x, ', id = ', hex(id(x)))
print('Nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)

print('\nObject identity "is not"')
x = 5 # Assignment membuat object
y = 6
print('Nilai x = ', x, ', id = ', hex(id(x)))
print('Nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)
