__author__ = "Onurcan EVREN"

# Stok bilgisini gösteren uygulama03.py
# Kullanıcı input ile stok bilgisini görmek istediği kitabın adını girer ve stok bilgisi ekrana yazdırılır.

print("-"*172)
kitaplik = {"Sapiens":1213, "Bozkurtlar":3532, "Adam":12333, "İnsan İnsana":4554, "Nutuk":5133, "Martı":5456, "Homodeus":123127, "Dönüşüm":8554, "İçimizdeki Şeytan":2139, "Serenad":10454, "Tutunamayanlar":1231, "Artemis":1254, "Marslı":1233}

print(kitaplik.keys())
print("-"*172)
print("")
girdi= input("Lütfen stok bilgisini öğrenmek istediğiniz eserin adını giriniz. (Küçük-büyük harf duyarlı değildir!) : ")
print("")

if girdi in kitaplik.keys():
    print("\"",girdi,"\"", "Stok Bilgisi :\n \n", kitaplik[girdi],"adet bulunmaktadır.")
else:
    print("\nGeçerli bir kitap ismi girmediniz! Lütfen kitap ismini doğru yazdığınızdan emin olup sistemin büyük-küçük harfe duyarlı olmadığına dikkat ediniz.")
