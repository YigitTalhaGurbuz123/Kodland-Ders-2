import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifrenin uzunluğunu giriniz: "))

sifre = ""

for i in range(sifre_uzunlugu):
    sifre += random.choice(karakter) + sifre

print(sifre)
