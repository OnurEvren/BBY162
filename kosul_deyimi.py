__author__ = "Onurcan EVREN"

yas = int(input("Yaşınızı yazınız...: "))

if yas>100:
    print("Lütfen 0-100 değerleri arasında bir değer yazınız...")

elif yas<0:
    print("Lütfen pozitif bir tamsayı değeri giriniz...")

elif yas<50:
    print("Girilen değer 0-50 arasındadır...")

else:
    print("Girilen değer 50-100 arasındadır...")