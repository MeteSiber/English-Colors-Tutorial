# selinin zeka oyunu
from tkinter import *
import random
import time
#from gtts import gTTS
import os
sayısıdır = 1
while sayısıdır > 0:
    puan = 0
    ofof = ["",""]
    started = 0

    def nextt():

        global started
        started += 1
        btn.config(text="Tekrar Oynamak icin Bas")
        btn.pack()

        global puan
        global ofof

        game_yz = ["black","pink","red","white","yellow","green","blue","purple","orange"]
        a = random.randint(0, 8)
        a = game_yz[a]
        a = a.lower()
        ofof.append(a)
        """try:
            tts = gTTS(text='{}'.format(a))
            tts.save("merhaba.mp3")
            os.system("merhaba.mp3")
        except:
            print("İnternet bağlantınız olmadığı için hata oluştu.")"""

        if a == "black" or a == "BLACK":
            text1.config(bg="white")
        else:
            text1.config(bg="white")


        a = a.lower()
        cvp = ent.get()
        cvp = cvp.upper()
        cvp = cvp.replace("i","ı")
        cvp = cvp.replace("İ","I")

        if started > 1:
            cevap = ofof[-2]
            cevap = cevap.upper()
            cevap = cevap.replace("i","ı")
            cevap = cevap.replace("İ","I")

            if cevap == cvp:

                puan += 1
                print(cevap,"==",cvp)
                kontrol.config(text="Doğru!\nScore: {}".format(puan),bg="green",fg="black")
                kontrol.pack()
            else:
                puan -= 1
                print(cevap, "==", cvp)
                kontrol.config(text="Yanlış!\nScore: {}".format(puan),bg="white",fg="black")
                kontrol.pack()
        else:
            pass

        a = a.upper()
        text1.config(text=">> {} <<".format(a), fg="{}".format(a))
        text1.pack()
        if puan == -5:
            sayısıd = 0






    def rot():
        root = Tk()
        root.title("Color Game that Teach English")
        root.geometry("1280x700")
        root.resizable(0,0)
        root.config(bg="")

        yazi1 = "\nDeveloper: Mertcan Balcı\nUpdater: Mete Tunc\nTürkce Versiyon\n18.03.2023\n"
        text = Label()

        text.config(text="{}".format(yazi1),bg="white",fg="black",font=("Calibri",28))
        text.pack()
        global text1
        a = 0
        text1 = Label()
        text1.config(text="{}".format("Hazır!"),fg="black",bg="{}".format("white"),font=("Calibri",70))
        text1.pack()

        bos = Label()
        bos.config(bg="White",fg="White",font=("Calibri",13))
        bos.pack()
        global ent
        ent = Entry()
        ent.config(font=("Calibri",25))
        ent.pack()

        bos2 = Label()
        bos2.config(bg="White", fg="White", font=("Calibri", 13))
        bos2.pack()



        global btn
        btn = Button()
        btn.config(text="Başla!",bg="black",font=("Calibri",30),fg="white",command=nextt)
        btn.pack()

        bos3 = Label()
        bos3.config(bg="white", fg="white", font=("Calibri", 13))
        bos3.pack()

        global kontrol
        kontrol = Label()
        kontrol.config(text="{}\nSkor: {}".format("Hadi Başla Butonuna Bas Ve Eğlenceye Başla !",puan),fg="black",bg="white",font=("Calibri",23))
        kontrol.pack()

        root.mainloop()

    rot()
    Tekrar = input("Tekrar Oynamak istermisiniz» ")
    if Tekrar == "evet" or Tekrar == "Evet":
        sayısıdır = sayısıdır + 1
    if Tekrar == "hayır" or Tekrar == "Hayır":
        input("Oynadığınız icin Teşekkürler ♥")
