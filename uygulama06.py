_author_ = "Onurcan EVREN"

import random

from tkinter import Tk, Label, Button

class bilgi_patlamasi:
    def __init__(self, master):
        self.master = master
        master.title("İlginç Bilgiler Ekranı")

        self.label = Label(master, text = "     Kategori seç ve bilgilen!     ", font = ("Arial", 17))
        self.label.pack()

        self.label = Label(master, text = "Onurcan EVREN tarafından oluşturuldu.", font = ("Arial",7))
        self.label.pack()

        #############

        self.hayvanlar = Button(master, text = "Hayvanlar", font = ("Arial", 14), command = self.hayvanlar)
        self.hayvanlar.pack()

        self.insanlar = Button(master, text = "İnsanlar", font = ("Arial", 14), command = self.insanlar)
        self.insanlar.pack()

        self.exit = Button(master, text = "Kapat", font = ("Arial", 14), command = master.quit)
        self.exit.pack()

    def hayvanlar(self):
        hayvan_bilgi = random.choice(["Kara sinekler \"Fa\" notasıyla vızıldarlar.","Bukalemunun dili kendi vücudu kadar uzayabilir.","Penguenler dünyanın en kıskanç canlılarıdır ama eşlerine asla şiddet uygulamazlar.","Kurtlar 750 kg çene basınç gücüne sahiptir ama eşlerine asla saldırmazlar.","Boz ayılar bir sığırı tek darbede öldürebilecek güçtedir ama bu güçlerini eşlerine karşı kullanmazlar.","İstiridyeler yaşamları boyunca birçok kez kendi cinsiyetlerini değiştirirler.","Çitalar 0'da 96 km hıza 3 saniyede erişir.","Erkek imparator pengueni birşey yemeden kuluçkada 2 ay boyunca dişisinin yemek getirmesini bekler.","Deniz atları tek eşli canlılardır. Hayatları boyunca sadece tek bir eşleri olur.","Yetişkin bir panda günün 12 saatini yemek yemeye harcar ve bu süre boyunca 12 kg bambu yer.","Karıncayiyenler günde 35 bin karınca yerler.","Kurtlar günde 9 kg et yerler.","Kral kobra bir fili öldürebilecek zehre sahiptir.","Kraliçe arı öldüğü zaman, işçi arılar bir dişi arıyı onu daha verimli hale getirecek olan \"arı sütü\" ile besleyerek yeni bir kraliçe meydana getirirler.","\"Jaguar\" kelimesinin yerli Amerikan dilindeki anlamı \"bir sıçramada öldürür\" dür."])
        self.bilgi1 = Label(self.master, text = hayvan_bilgi)
        self.bilgi1.pack()

    def insanlar(self):
        insan_bilgi = random.choice(["En yararlı tavsiyeleri veren insanlar en çok problemi olanlardır.","İnsan beyninin depolayabileceği bilgi miktarı Encyclopedia Britannica’nın içindeki bilgiden 5 kat fazla.","İnsan beyni kandaki oksijenin yüzde 20’sini harcıyor.","Ortalama bir insan günde 60-100 saç teli kaybeder.","İnsan kalbinin yarattığı basınç, kanı 10 metre yüksekliğe fışkırtmaya yeterlidir.","Midenizdeki asit bir jileti eritebilecek kadar kuvvetlidir.","İnsan vücudundaki damarların toplam uzunluğunun yaklaşık 96,500 km olduğu tahmin ediliyor.","Midenizin iç çeperi her 3 ila 4 günde bir yenilenir.","Kadınların kalbi, erkeklerden daha hızlı atar.","Kadınların ortalama sır tutabilme süreleri 47 saat 15 dakikadır."," Uzun zamandır yalnız olmak sağlığınızı günde 15 sigara içmek kadar kötü etkiler.","Kırmızı kan hücreleri bütün vücudu yaklaşık 20 saniyede dolaşır.","Bebeklerin yetişkinlere göre 60 fazla kemiği vardır.","İnsan gözü dijital bir kamera olsaydı, 576 megapiksel olurdu.","Hamilelik süresince, eğer annede organ hasarı ortaya çıkarsa, rahimdeki bebek hasarlı organı onarmak için kök hücre gönderir."])
        self.bilgi2 = Label(self.master, text = insan_bilgi)
        self.bilgi2.pack()

root = Tk()
my_gui = bilgi_patlamasi(root)
root.mainloop()