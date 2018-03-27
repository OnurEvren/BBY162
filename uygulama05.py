__author__ = "Onurcan EVREN"

import random

bulunacakkelime = random.choice(["elma", "ayva", "armut", "erik", "karpuz", "incir", "üzüm", "böğürtlen", "dut", "kiraz"])

harfhavuzu = []

kalanhak = 6

altcizgi = "_"


gosterimyazisi = list(altcizgi * len(bulunacakkelime))

dongu = 1


while dongu:

    print(" ".join(gosterimyazisi),"\n") # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.

    alinanharf = input("Bir harf giriniz: ").lower() # Büyük-küçük harf uyumluluğu için küçük harfe çevirdim.

    try: # try, input ile alınan verinin sayı olup olmadığını kontrol eder.
        int(alinanharf)
        print("Doğru bir şeyler girdiğinden emin ol.\n")
    except: # Except alınan harf 1 den uzun olduğunda hata mesajı verir.

        if len(alinanharf) > 1:
            print("Harf giriniz!\n")
        else:

            if alinanharf in harfhavuzu:
                print("Bu harfi zaten girdiniz.\n")
            else:

                bulduk = None

                for i in range(len(bulunacakkelime)):
                    # kullanıcının girdiği harf, bulunucak kelimenin "i" nin taşıdığı sayı değerindeki indeksteki harfe eşit ise,
                    if alinanharf == bulunacakkelime[i]:

                        bulduk = True

                        gosterimyazisi[i] = alinanharf

                        harfhavuzu.append(alinanharf) # Alınan harf, harf havuzuna eklendi.

                        if altcizgi not in gosterimyazisi:

                            print(" ".join(gosterimyazisi)) # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.
                            print("\nTebrikler kelimeyi buldunuz!")

                            dongu = 0
                            # Girilen harf aranan kelime içinde yoksa alttaki kodlar çalıştırılacak.
                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkınız: %s\n" %kalanhak)

                        harfhavuzu.append(alinanharf) # Alınan harf, harf havuzuna eklendi

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" %bulunacakkelime)

                    break