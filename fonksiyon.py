__author__ = "Onurcan EVREN"

def dortgen_alan_hesapla_v1(a,b):
    dortgen_alan = a*b
    print("Dikdörtgenin Alanı = " , dortgen_alan)

kisa_kenar = int(input("Dikdörtgenin kısa kenarını giriniz...: "))
uzun_kenar = int(input("Dikdörtgenin uzun kenarını giriniz...: "))

dortgen_alan_hesapla_v1(kisa_kenar,uzun_kenar)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def daire_alan_hesapla_v1(a,b): #a=pi,b=yaricap
    dairenin_alani = a*(b**2)
    print("Dairenin alanı = " , dairenin_alani)

yaricap = int(input("Alanını hesaplamak istediğiniz dairenin yarıçapını giriniz...: "))
pi = 3.14

daire_alan_hesapla_v1(pi,yaricap)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def dortgen_alanı_hesapla_v2(a,b):
    dortgen_alanin_karesi = a*b
    print("Dikdortgen Alanının Karesi = " , dortgen_alanin_karesi)

kisa_kenar = int(input("Dikdörtgenin kısa kenarını giriniz...: "))
uzun_kenar = int(input("Dikdörtgenin uzun kenarını giriniz...: "))

dortgen_alanı_hesapla_v2(kisa_kenar**2,uzun_kenar**2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def daire_alanı_hesapla_v2(a,b):
    dairenin_alaninin_karesi = a*((b**2)**2)
    print("Daire alanının karesi = " , dairenin_alaninin_karesi)

yaricap = int(input("Karesini hesaplamak istediğiniz dairenin yarıçapını giriniz...: "))
pi = 3.14

daire_alanı_hesapla_v2(pi,yaricap)

