# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 08:45:34 2022

@author: tosun
"""

"""write:
    -Dosyayi ilgili konumda yeni dosya yoksa olusturur, 
    -Dosya icerigini siler ve yeniden ekleme yapar."""
"""file = open("newfile.txt","w",encoding='utf-8') 
print(file)
#file.write("Sevde")
file.close()"""

"""file = open("C:/Users/tosun/OneDrive/newfile2.txt","w")
print(file)
file.close()"""

"""append:
    -Dosyayi ilgili konumda yeni dosya yoksa olusturur, 
    -Dosya icerigini silmez, uzerine ekleme yapar."""

"""file = open("newfile.txt","a",encoding='utf-8') 
print(file)
file.write("Sevde\n")
file.close()"""

"""create:
    -Dosyayi ilgili konumda yeni dosya yoksa olusturur, varsa hata verir."""
    
"""file = open("newfile.txt","x",encoding='utf-8') 
print(file)
file.write("Sevde")
file.close()"""    

"""read:
    -Varsayilan dosya konumda yoksa hata verir.
    -'r' modu yazilmasa bile dosya acma isleminde varsayilan mod okuma modudur."""
   

"""try:
    file = open("C:/Users/tosun/OneDrive/newfile3.txt","r")
except FileNotFoundError:
    print("Dosya okuma hatasi")
finally:
    print("Dosya Kapandi!")
    file.close()"""

"""file = open("newfile.txt","r",encoding = 'utf-8')
for i in file:
    print(i)
content1 = file.read()
print(content1)
content2 = file.read()
print(content2)"""

"""file = open("newfile.txt","r",encoding = 'utf-8')
content3 = file.read(3) #Karakter okur.
print(content3)"""

"""file = open("newfile.txt","r",encoding = 'utf-8')
content4 = file.readline() #Satir okur.
print(content4) #Tek satiri okur ve yazdirir.
print(file.readline(),end="") #Sonlarina bosluk yazdirmaz. readline her zaman bir bosluk getirir.
print(file.readline()) 
file.close()"""
#Dosya kapanmadan tekrar okundugunda imlec sonda oldugu icin okumaz. Dosya file= ile tekrar alinirsa okunur.

"""file = open("newfile.txt","r",encoding = 'utf-8')
liste = file.readlines() #Dosyadaki satirlari liste elemanlari olarak dondurur.
print(liste) #Her eleman sonuna bosluk karakteri de ekler.
print(liste[0]) #Bosluk karakteri olmadan listenin birinci elemanini dondurur."""

"""with open("newfile.txt","r",encoding = 'utf-8') as file:
    content5 = file.read(5)
    print(content5)
    file.seek(5) #cursor'un gitmesi gerektigi konumu verir.
    print(file.tell()) #cursor konumunu verir.
    content6 = file.read()
    print(content6)
#Dosya with ile acilirsa islem sonunda otomatik kapanir."""

#Dosya Guncelleme
"""with open("newfile.txt","r+",encoding = 'utf-8') as file:
    file.seek(6)
    file.write("deneme") #Belirtilen indexten itibaren yazar,gunceller.
with open("newfile.txt","r+",encoding = 'utf-8') as file:
    print(file.read())
#'r+' hem okuma hem yazma anlamina gelir."""

#Sayfa Sonunda Guncelleme
"""with open("newfile.txt","a",encoding = 'utf-8') as file:
    file.write("\nHafsa Nur Tosuner")
with open("newfile.txt","r+",encoding = 'utf-8') as file:
    print(file.read())"""
    
#Sayfa Basinda Guncelleme
"""with open("newfile.txt","r+",encoding = 'utf-8') as file:
    content = file.read()
    content = ("Hasan Tosuner\n") + content
    file.seek(0)
    file.write(content)
    
with open("newfile.txt","r+",encoding = 'utf-8') as file:
    print(file.read())"""
    
#Sayfa Ortasinda Guncelleme
with open("newfile.txt","r+",encoding = 'utf-8') as file:
    liste = file.readlines()
    print(liste)
    liste.insert(2,"Halime Tosuner\n") #Ikinci indeksten hemen once ekler.
    print(liste)
    file.seek(0)
    file.writelines(liste) #Direk liste elemanlarini satir olarak ekler.
    """for i in liste:
        file.write(i)"""
with open("newfile.txt","r+",encoding = 'utf-8') as file:
    print(file.read())



    


