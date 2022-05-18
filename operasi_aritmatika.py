# Operasi Aritmatika

a = 15
b = 4

print("a = ",a)
print("b = ",b)

# Operasi Penjumlahan
jumlah = a + b
print("a", "+", "b", "=", jumlah)

# Operasi Pengurangan 
kurang = a - b
print("a", "-", "b", "=", kurang)

# Operasi Perkalian
kali = a * b
print("a", "*", "b", "=", kali)

# Operasi Pembagian
bagi = a / b
print("a", "/", "b", "=", bagi)

# Eksponen atau pangkat
eksponen = a ** b
print("a", "**", "b", "=", eksponen)

# Modulus atau sisa hasil bagi
modulus = a % b
print("a", "%", "b", "=", modulus)

# Floor Division -> pembagian dengan hasil yang dibulatkan ke bawah
floor_div = a // b
print("a", "//", "b", "=", floor_div)

# Prioritas Operasi (Operational Precedence)
"""
    1.Kurung -> ()
    2.Eksponen -> **
    3.Perkalian, Pembagian, Modulus, dan Floor Division -> * / % //
    4.Penjumlahan dan Pengurangan -> + -
"""

x = 3
y = 4 
z = 5

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)