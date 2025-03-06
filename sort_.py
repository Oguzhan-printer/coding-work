
sayilar = [15, 8, 22, 5, 42, 17]

en_kucuk = sayilar[0]
en_buyuk = sayilar[0]

for sayi in sayilar:
  if sayi < en_kucuk:
    en_kucuk = sayi
  if sayi > en_buyuk:
    en_buyuk = sayi

print("En küçük sayımız:", en_kucuk)
print("En büyük sayımız:", en_buyuk)