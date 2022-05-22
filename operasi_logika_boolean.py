# Operasi Logika atau Boolean

# NOT, OR, AND, XOR

print("=====NOT=====")
# Bernilai kebalikannya. Misal, jika a adalah true, nilai b not a hasilnya false
a = False
b = not a
print("A = ", a)
print("B NOT A")
print("B = ", b)

print("=====OR=====")
# Jika salah satu bernilai true, maka hasilnya True
a = True
b = True
c = a or b
print(a, " OR", b, " =", c)
a = True
b = False
c = a or b
print(a, " OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, " =", c)
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

print("=====AND=====")
# Akan bernilai True jika keduanya bernilai True
a = True
b = True
c = a and b
print(a, " AND", b, " =", c)
a = True
b = False
c = a and b
print(a, " AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, " =", c)
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

print("=====XOR=====")
# Akan bernilai True jika salah satu bernilai True
a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c)
a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)