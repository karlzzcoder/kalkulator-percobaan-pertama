angka_pertama = float(input("masukan angka pertama: "))
angka_kedua = float(input("masukan angka kedua: "))
operasi = input("Masukan operasi (+ - * /): ")

if operasi == "+":
    hasil = angka_pertama + angka_kedua
elif operasi == "-":
    hasil = angka_pertama - angka_kedua
elif operasi == "*":
    hasil = angka_pertama * angka_kedua
elif operasi == "/":
    hasil = angka_pertama / angka_kedua
else:
    print("ngawur, ulang lagi")
    hasil = None

if hasil is not None:
    print(f"hasil nya adalah: {hasil}")
