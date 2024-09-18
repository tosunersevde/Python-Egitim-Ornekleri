# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:39:27 2022

@author: tosun
"""

"""Gelen Bilgileri veya kendi olusturdugumuz, analiz sonucunda elde edilen
bilgileri daha anlamli hale getirmek icin grafikler uzerinde gosteririz."""


#matplotlib.pylot.plot #internet sitesinden stiller degistirilebilir.
import matplotlib.pyplot as plt
import numpy as np

#Ornek1 
"""x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r",linewidth ="2") #cizgi grafigi (x'in karesi) 
#cizgi kalinlik - linewidth
#yuvarlak marker(nokta) - o
#-g -> green solid line
plt.axis([0,6,0,20]) #grafik araligi

plt.title("Grafik Basligi")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()"""

#Ornek2
"""x = np.linspace(0,2,100) #0-2 arasi 100 parca
plt.plot(x,x,label ="linear",color="red") #cizgi adi,rengi
plt.plot(x,x**2,label ="quadratic",color="yellow")
plt.plot(x,x**3,label ="cubic",color="green")

plt.xlabel("x label") #satir adi
plt.ylabel("y label")

plt.title("Simple Plot") #grafik adi
plt.legend()
plt.show()"""

#Birden fazla grafik
"""x = np.linspace(0,2,100)
fig,axs = plt.subplots(3) #Ayri ayri 3 grafik

axs[0].plot(x,x,color="red",)
axs[0].set_title("Linear")
axs[1].plot(x,x**2,color="green")
axs[1].set_title("Quadratic")
axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("Cubic")

plt.tight_layout() #Basliklari duzene koyar.
plt.show() """

"""x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2) #Ayri ayri 3 grafik
fig.suptitle("Grafik Basligi")

axs[0,0].plot(x,x,color="red",)
axs[0,0].set_title("Linear")
axs[0,1].plot(x,x**2,color="green")
axs[0,1].set_title("Quadratic")
axs[1,1].plot(x,x**3,color="yellow")
axs[1,1].set_title("Cubic")
axs[1,0].plot(x,x**4,color="blue")

plt.tight_layout() 
plt.show()"""

#Stack Plot
"""yil = [2011,2012,2013,2014,2015]

oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,5,15,21]
oyuncu3=[18,20,22,25,19]

plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("Yillara gore atilan goller")

plt.xlabel("Yil")
plt.ylabel("Gol sayisi")

plt.legend()
plt.show()"""

#Pie- Pasta Grafigi
"""goal_types = 'Penalti','Kaleye Atilan Sut', 'Serbest Vurus'

goals = [12,35,7]
colors=["y","r","b"]

plt.pie(goals,labels=goal_types,colors = colors,shadow = True, explode=(0.05,0.05,0.05), autopct=%1.1%%)
#autopct=%1.1%% - yuzdelik ifade formati
#shadow - golgelendirme / explode - grafik dilimleri arasi bosluk
plt_show()"""

#Bar - Sutun Grafigi
#Direk deger karsiliklarini yazar.
"""plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label='BMW',width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label='Audi',width=.5)
#width = sutun genislik

plt.legend()

plt.xlabel("Gun")
plt.ylabel("Mesafe (km)")

plt.title("Arac Bilgileri")"""

#Histogram Grafigi
#Degerler arasi verileri sayar.
"""yaslar = [22,55,62,45,21,22,34,42,4,2,102,12,16]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype = "bar",rwidth=0.8)

plt.xlabel("Yas Gruplari")
plt.ylabel("Kisi Sayisi")

plt.title("Histogram Grafigi")"""

#Verinin Grafigini Olusturma
"""import pandas as pd

df = pd.read_csv("nba.cvs")

df = df.drop(["Number"],axis=1).groupby("Team").mean()
df.head(5).plot(subplots = True) #ayri ayri yas - agirlik icin grafikleri olsuturur.

plt.legend()
plt.show()"""

#Figur Olusturma
"""x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) #soldan 0.1 / alttan 0.1 / genislik / yukseklik

axes_cube.plot(x, y, color="b")
axes_cube.set_xlabel("X axis")
axes_cube.set_xlabel("Y axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25]) 

axes_square.plot(x, z, color="r")
axes_square.set_xlabel("X axis")
axes_square.set_xlabel("Y axis")
axes_square.set_title("Square")

plt.show()"""

#Tek figurde
"""x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1]) #Sayfayi oldugu gibi kaplar.

axes.plot(x, y, label="Square")
axes.plot(x, z, label="Cube")
axes.legend(loc=1) #sag ust kose loc=2,3,4 vs."""

"""figs,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8)) #2 axes
#figure boyu genisligi ve yuksekligi = figsize

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("fig.png") #Figur kayit islemi
plt.show()"""

 




