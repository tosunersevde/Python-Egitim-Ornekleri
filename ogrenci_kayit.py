# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:54:18 2022

@author: tosun
"""

def hesapla(satir):
    satir = satir[:-1] #Satirlardan sonra yazilan bosluklar alinir.
    liste = satir.split(":") #':'  dan itibaran boler. (Notlari almak icin.)
    ogrenci_adi = liste[0]
    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ort = (not1+not2+not3) / 3
    
    if ort>=90 and ort<=100:
        harf = "AA"
    elif ort>=85 and ort<=89:
        harf = "BA"
    elif ort>=65:
        harf = "BB"
    else:
        harf = "FF"
        
    return ogrenci_adi + ':' + harf + '\n'
    

def ortalamalari_oku():
    with open("ogrenci_bilgi.txt","r",encoding = 'utf-8') as file:
        for i in file:
            print(hesapla(i))
def not_gir():
    ad = input("Ogrenci ad:")
    soyad = input("Ogrenci soyad:")
    not1 = int(input("Not1:"))
    not2 = int(input("Not2:"))
    not3 = int(input("Not3:"))
    
    with open("ogrenci_bilgi.txt","a",encoding = 'utf-8') as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' +not3+'\n')
        
def notlari_kaydet():
    with open("sinav_notu.txt","r",encoding = 'utf-8') as file:
        liste2 = []
        for i in file:
            liste2.append(hesapla(i))
            with open("sinav_notu.txt","w",encoding = 'utf-8') as file2:
                for j in liste2:
                    file2.write(j)
        
    
while True:
    islem = input("1-Notlari Oku\n2-Not Gir\n3-Notlari Kaydet\n4-Cikis")
    if islem== '1':
        ortalamalari_oku()
    elif islem== '2':
        not_gir()
    elif islem=='3':
        notlari_kaydet()
    else:
        break
