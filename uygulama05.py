__author__ = "Onurcan EVREN"

import random

secilen_kelime = random.choice(["elma", "ayva", "armut", "erik", "karpuz", "incir", "üzüm", "böğürtlen", "dut", "kiraz"])
can_sayisi = 6
pano = []
alt_cizgi = "_"

print("Adam Asmaca oyununa hoşgeldiniz..\n")

for kelime in secilen_kelime:

    pano.append(alt_cizgi)

print(pano)

while can_sayisi > 0:

    i = 0

    girdi = input("\nBir harf giriniz: ").lower()

    if girdi in secilen_kelime:
        for kontrol in secilen_kelime:
            if secilen_kelime[i] == girdi:
                pano[i] = girdi
            i += 1

        print("")
        print(pano)
        print("\n \"%s\" harfi doğru tahmin!" %girdi)

    else:
        can_sayisi -= 1
        print("")
        print(pano)
        print("\n\"%s\" harfi yanlış tahmin. Pes etme ve devam et :)" % girdi)
        print("\nKalan can sayısı = " + "[" + can_sayisi * " ♥ " + "] = " + str(can_sayisi))

    if can_sayisi == 0:
        print("Başaramadın! Doğru cevap: %s" %secilen_kelime)
        break

    if alt_cizgi not in pano:
        print("\nTebrikler! Kelimeyi buldun!")
        break