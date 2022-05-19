# Latihan Konversi Satuan Temperatur

# Konversi Celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam Celcius : "))
print("Suhu adalah", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Reamur : ", reamur, "R")

# Fahrenheit
fahrenheit = (9/5) * celcius + 32
print("Fahrenheit : ", fahrenheit, "F")

# Kelvin
kelvin = celcius + 273
print("Kelvin : ", kelvin, "K")

print("\nFahrenheit Ke Kelvin\n")
fahrenheit1 = float(input("Masukkan suhu dalam F : "))
print("Suhu F adalah ", fahrenheit1, "F")

# Kelvin
kelvin1 = (5/9) * (fahrenheit1 - 32) + 273
print("Kelvin : ", kelvin1, "K")