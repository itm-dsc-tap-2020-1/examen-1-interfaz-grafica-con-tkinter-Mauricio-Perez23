#MAURICIO PÉREZ CÁRDENAS
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

def califica():
    cal = 0
    if res1.get() == "-10X+Y":
        cal=cal+10
    if res2.get() == "PITAGORAS":
        cal = cal +10
    if r1.get() == 1:
        cal = cal +10
    if rw2.get() == 2:
        cal = cal + 10
    if c1.get() and c4.get():
        if c2.get() or c3.get():
            print("Mala respuesta")
        else:
            cal=cal+20
    else:
        if c2.get() or c3.get():
            print("mala respuesta")
        else: 
            if c1.get() or c4.get():
                cal= cal + 10
    
    im=tk.Tk()
    im.title("---> CALIFICACION <---")
    im.geometry('600x400')
    ejj=ttk.Label(im, text="CALIFICACION: " + str(cal) , background='black', foreground='gold')
    ejj.place(x=0,y=30)











ven=tk.Tk()
ven.title("---> E X A M E N   D E   A L G E B R A <---")
ven.geometry('600x400')

cap1=ttk.Label(ven, text="1 -> ¿Cuato es -4X+9Y-6X-10Y? ", background='black', foreground='gold')
cap1.place(x=0,y=30)
res1= tk.StringVar()
ress1= tk.Entry(ven,width=20,textvariable=res1)
ress1.place(x=0,y=50)

cap2=ttk.Label(ven, text="2 -> ¿De quien es el Terema que establece que 'c^2 = a^2 + b^2'? ", background='black', foreground='gold')
cap2.place(x=0,y=80)
res2= tk.StringVar()
ress2= tk.Entry(ven,width=20,textvariable=res2)
ress2.place(x=0,y=100)


cap3=ttk.Label(ven, text="3 -> ¿Cual es el elemento neutro para la SUMA? ", background='black', foreground='gold')
cap3.place(x=0,y=130)
r1=tk.IntVar()
rad1=tk.Radiobutton(ven, text="+0", variable=r1, value=1)
rad1.place(x=0, y=150)
rad2=tk.Radiobutton(ven, text="-X", variable=r1, value=2)
rad2.place(x=80, y=150)
rad3=tk.Radiobutton(ven, text="1", variable=r1, value=3)
rad3.place(x=160, y=150)


capi4=ttk.Label(ven, text="4 -> ¿Cual es el elemento neutro para MULTIPLICACIÓN? ", background='black', foreground='gold')
capi4.place(x=0,y=180)
rw2=tk.IntVar()
rad12=tk.Radiobutton(ven, text="1/X", variable=rw2, value=1)
rad12.place(x=0, y=200)
rad22=tk.Radiobutton(ven, text="1", variable=rw2, value=2)
rad22.place(x=80, y=200)
rad32=tk.Radiobutton(ven, text="0", variable=rw2, value=3)
rad32.place(x=160, y=200)



pasa = ttk.Label(ven, text="5 -> ¿De que manera se puede represnetar un PRODUCTO?", background='black', foreground='gold')
pasa.place(x=0, y=230)

c1 = tk.IntVar()
cas1=tk.Checkbutton(ven, text="(X)(Y)", variable=c1)
cas1.place(x=0, y=250)

c2 = tk.IntVar()
cas2=tk.Checkbutton(ven, text="X+Y", variable=c2)
cas2.place(x=50, y=250)

c3 = tk.IntVar()
cas3=tk.Checkbutton(ven, text="X/Y", variable=c3)
cas3.place(x=100, y=250)

c4 = tk.IntVar()
cas4=tk.Checkbutton(ven, text="XY", variable=c4)
cas4.place(x=150, y=250)


boton = ttk.Button(ven, text="CALIFICAR", command= califica)
boton.place(x=150,y= 320)

ven.mainloop()