# x = 5, x adalah variabel yang menyimpan nilai 5

# Tipe data angka satuan : integer (int)
data_integer = 2
print("Data : ", data_integer)
print("Bertipe data : ", type(data_integer))

# Tipe data angka dengan koma : float (float)
data_float = 3.14
print("Data : ", data_float)
print("Bertipe data : ", type(data_float))

# Tipe data kumpulan karakter : string (str)
data_string = "Hai"
print("Data : ", data_string)
print("Bertipe data : ", type(data_string))

# Tipe data biner true/false : boolean (bool)
data_boolean = True
print("Data : ", data_boolean)
print("Bertipe data : ", type(data_boolean))

## Tipe data khusus
# Bilangan kompleks (complex)
data_complex = complex(11,12)
print("Data : ", data_complex)
print("Bertipe data : ", type(data_complex))

## Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.4)
print("Data : ", data_c_double)
print("Bertipe data : ", type(data_c_double))