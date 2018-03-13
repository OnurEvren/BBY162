__author__ = "Onurcan EVREN"

kadinadi = input("Bir kadın adı giriniz...:")
erkekadi = input("Bir erkek adı giriniz...:")
misra    = int(input("Mısra sayısı giriniz...Maksimum 14 mısra yazdırılabilir.."))

print("-"*60)

print("")

siir     = [erkekadi + " güzel gözlü "+ kadinadi +" sever", "Bir de küçük ayaklı, kısa boylu " + kadinadi ,"Hem nasıl sever, öyle sever işte","Terler avuçları, kesilir solukları", erkekadi + " mahzun " + kadinadi + " sever, hüzünlü bakanları","Yavru ceylan gibi olan " + kadinadi + ", ürkekçe","Hem nasıl sever, öyle sever işte.", "Bilemezsiniz ne güzeldir " + kadinadi + " sevdikçe",erkekadi + " akıllı " + kadinadi + " sever,","Düşünen, az konuşan, çok bilen,","Her yerde, her zaman nazı çekilen,","Hem nasıl sever, öyle sever işte,","İçinde büyük, sonsuz ateşler yanmalı,","Ölümün bile " + kadinadi + " yüzünden olmalı..."]

for olusturulacak_siir in siir[:misra]:
    print(olusturulacak_siir)

print("")

print("-"*60)

if misra > 14:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 14") # 14 den büyük bir değer girildiğinde 14 mısraya kadar yazdırıldığı için her zaman 14 yazacak.
    print("Bu şiir Ümit Yaşar Oğuzcan'dan alınıp tekrar düzenlenmiştir.")
else:
    print("Yazdırılan mısra sayısı:", misra)
    print("Bu şiir Ümit Yaşar Oğuzcan'dan alınıp tekrar düzenlenmiştir.")
