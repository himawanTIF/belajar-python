# Secara default, input dari user akan terbaca sebagai string
data = input("Masukkan angka: ")
print("Data: ", data, ", bertipe: ", type(data))

# Menggunakan metode casting (konversi) untuk mengubah tipe data input dari user
data_int = int(input("Masukkan angka: "))
print("Data: ", data_int, ", bertipe: ", type(data_int))

data_float = float(input("Masukkan angka: "))
print("Data: ", data_float, ", bertipe: ", type(data_float))

# Untuk boolean perlu melakukan casting ke integer, jika tidak akan selalu dibaca true
data_bool = bool(int(input("Masukkan nilai boolean: ")))
print("Data: ", data_bool, ", bertipe: ", type(data_bool))