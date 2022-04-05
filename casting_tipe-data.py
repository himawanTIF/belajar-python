# Casting adalah mengubah suatu tipe data ke tipe data yang lain (konversi tipe data)
# Tipe data: int, float, str, bool

print("=====INT=====")
data_int = 10
print("Data: ", data_int, "tipe data: ", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data: ", data_float, "tipe data: ", type(data_float))
print("Data: ", data_str, "tipe data: ", type(data_str))
print("Data: ", data_bool, "tipe data: ", type(data_bool))

print("=====FLOAT=====")
data_float = 1.5
print("Data: ", data_float, "tipe data: ", type(data_float))
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("Data: ", data_int, "tipe data: ", type(data_int))
print("Data: ", data_str, "tipe data: ", type(data_str))
print("Data: ", data_bool, "tipe data: ", type(data_bool))

print("=====STRING======")
data_string = "1999"
print("Data: ", data_string, "tipe data: ", type(data_string))
data_int = int(data_string)
data_float = float(data_string)
data_bool = bool(data_string)
print("Data: ", data_int, "tipe data: ", type(data_int))
print("Data: ", data_float, "tipe data: ", type(data_float))
print("Data: ", data_bool, "tipe data: ", type(data_bool))

print("=====BOOLEAN=====")
data_bool = True
print("Data: ", data_bool, "tipe data: ", type(data_bool))
data_int = int(data_bool)
data_float = float(data_bool)
data_string = str(data_bool)
print("Data: ", data_int, "tipe data: ", type(data_int))
print("Data: ", data_float, "tipe data: ", type(data_float))
print("Data: ", data_string, "tipe data: ", type(data_string))