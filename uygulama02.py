__author__ = "Onurcan EVREN"

girdi = int(input("Saniye cinsinden bir değer giriniz...:"))
print("-"*53)
print("")

yil = girdi / 31557600
ay = (girdi % 31557600) / 2629800
gun = ((girdi % 31557600) % 2629800) / 86400
saat = (((girdi% 31557600) % 2629800) % 86400) / 3600
dakika = ((((girdi % 31557600) % 2629800) % 86400)% 3600) / 60
saniye = (((((girdi % 31557600) % 2629800) % 86400) % 3600) % 60)

"""
1 yıl  = 365 gün 6 saat
1 ay   = 30 gün olarak hesaplanmıştır.

"""


print(int(yil) , "Yıl" , "," , int(ay) ,"Ay" , "," , int(gun) ,"Gün" , "," , int(saat) , "Saat" , "," , int(dakika)  ,"Dakika", "," , int(saniye) , "Saniye")
print("")
print("-"*53)
