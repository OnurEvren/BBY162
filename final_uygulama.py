__author__ = "Onurcan EVREN"

import tkinter
from random import choice
from tkinter import messagebox
class Simon() :
    def __init__(self, master) :
        master.wm_iconbitmap("final_anasayfa.ico")
        messagebox.showinfo("Simon Hafıza Oyunu","Hoşgeldiniz!\n\nEkranda 4 adet rengimiz olacak. Bilgisayar öncelikle bu dört renkten herhangi bir kombinasyon oluşturup görsel olarak size gösteriyor. Siz de bu kombinasyonu aynı sırada tekrar etmelisiniz\n\nİyi Eğlenceler!\n\nBaşlamak için \"Tamam\" butonuna tıklayın.")
        self.master = master
        self.master.minsize(700, 540)
        self.master.title("Simon Hafıza Oyununa Hoşgeldiniz")
        self.master.update()

        self.canvas = tkinter.Canvas(self.master, width = self.master.winfo_width(), height = self.master.winfo_height(), highlightthickness = 0)
        self.canvas.pack()

        self.renkler1 = ("red", "darkblue", "darkgreen", "yellow")
        self.renkler2 = ("#ff7f50", "lightblue", "lightgreen", "#FFFFE0")
        self.renk = [color for color in self.renkler1]

        self.pano = []

        self.sira = [choice(self.renkler1)]
        self.sira_konum = 0

        self.canvas_ciz()

        self.sirayi_goster()

        self.master.mainloop()

    def sirayi_goster(self) :
        self.parlat(self.sira[self.sira_konum])

        if(self.sira_konum < len(self.sira) - 1) :

            self.sira_konum += 1
            self.master.after(1250, self.sirayi_goster)
        else :
            self.sira_konum = 0

    def parlat(self, color) :
        index = self.renkler1.index(color)
        if self.renk[index] == self.renkler1[index] :
            self.renk[index] = self.renkler2[index]
            self.master.after(1000, self.parlat, color)
        else :
            self.renk[index] = self.renkler1[index]
        self.canvas_ciz()

    def kontrol(self) :
        color = self.renkler1[self.pano.index(self.canvas.find_withtag("current")[0])]
        if(color == self.sira[self.sira_konum]) :
            if(self.sira_konum < len(self.sira) - 1) :
                self.sira_konum += 1
            else :
                self.master.title("Simon Hafıza Oyunu - Toplam Puanınız: %s" %(len(self.sira)))
                self.sira.append(choice(self.renkler1))
                self.sira_konum = 0
                self.sirayi_goster()
        else :
            messagebox.showinfo("Simon Hafıza Oyunu", "Yanlış tahmin!\n\nToplam puanınız: %s \n\nTekrar oynamak için \"Tamam\" butonuna tıklayın." %str(len(self.sira)-1))
            self.sira[:] = []
            self.sira.append(choice(self.renkler1))
            self.sira_konum = 0
            self.sirayi_goster()

    def canvas_ciz(self) :
        self.pano[:] = []
        self.canvas.delete("all")
        for index, color in enumerate(self.renk) :
            if index <= 1 :
                self.pano.append(self.canvas.create_rectangle(index * self.master.winfo_width(), 0, self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
            else :
                self.pano.append(self.canvas.create_rectangle((index - 2) * self.master.winfo_width(), self.master.winfo_height(), self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
        for id in self.pano :
            self.canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.kontrol())

def main() :
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()