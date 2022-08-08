# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:49:36 2022

@author: tosun
"""

#OS Modulu
"""-Isletim sistemi ile ilgili bilgiler sunar.
-Klasor olusturp klasor yeniden adlandirilabilir.
- Dosya islemleri yapilabilir."""

import os
#import datetime

#result = dir(os)

#Dizin degistirme
#os.chdir('C:\\') #Hangi dizin altinda klasor olusturulacagini oldugunu soyler.
#os.chdir('..') #Bir ust klasore gecer.
#os.chdir('../../..') #Uc ust klasore gecer.

#Klasor olusturma
#os.makedirs("newdirectory") #Ayni dizinde bir klasor olusturur.
#os.makedirs("newdirectory/yeni_klasor") #Klasor icersinsnde klasor(ice ice) olusturmaya yarar.
#Dizin degistirerek istenen konumda klasor olsuturulabilir veya direk dizin ismini yazarak klasor olsuturulabilir.
#os.rename("newdirectory","klasor1") #Klasor adini degistirme
#os.rmdir("yeni_klasor") #Klasoru silmeye yarar. Alt klasor olmadigi zaman kullanilir.
#os.removedirs("klasor1/yeni_klasor") #Alt dizin varsa kullanilir.

#Listeleme
#result = os.listdir() #Klasor icindekileri listelememizi saglar.
"""result = os.listdir("C://")
print(result)"""

"""for dosya in os.listdir():
    if dosya.endswith(".py"): #Sonu .py ile biten dosyalari listeler.
        print(dosya)"""
        
#result = os.stat("btk_OS_modulu.py") #Dosya hakkinda bilgi almak icin
#result = result.st_size/1024 #Dosya boyutunu byte turunden verir. Kilobayt olarak bulmak icin.
#result = datetime.datetime.fromtimestamp(result.st_ctime) #olsuturulma tarihi
#result = datetime.datetime.fromtimestamp(result.st_atime) #son erisim tarihi
#result = datetime.datetime.fromtimestamp(result.st_mtime) #degistirilme tarihi
#Okunabilir tarih bilgisine cevirir.
#print(result)

#Etkin dizin ogrenme
#result = os.name #Isletim sistemini soyler.

#Istenilen prgram-dosya calistirma
#os.system("notepad.exe") #Note pad'i acar.

"""result = os.getcwd() #Klasorun hangi dizinde oldugunu soyler.
print(result)"""

#OS modulu icerisindeki path sinifi daha cok uzantilar uzerinde islem yapar. 
#Dosyanin uzantisini ya da ismini degistirme gibi islemler yapar.
#result = os.path.abspath("btk_OS_modulu.py") #Dosyanin tam konumunu verir.
#result = os.path.dirname("C:/Users/tosun/spyder_projeler/btk_OS_modulu.py")
#result = os.path.dirname(os.path.abspath("btk_OS_modulu.py")) #Dizin ismi gerekliyse dosya yolunu veren sinifla yol yazdirilir.
#result = os.path.exists("btk_OS_modulu.py") #Aranilan konumda dosyanin var olup olmadigi degerini dondurur.
#result = os.path.exists("C:/Users/tosun/spyder_projeleri.py") #False - Klasor de sorgulanabilir.
#result = os.path.isdir("C:/Users/tosun/spyder_projeler") #Klasor mu diye sorgular.
#result = os.path.isdir("C:/Users/tosun/spyder_projeler/btk_OS_modulu.py") #Dosya oldugu icin false doner.
#result = os.path.isfile("C:/Users/tosun/spyder_projeler/btk_OS_modulu.py") #True doner - Bu bir dosyadir.
#result = os.path.join("C://","deneme","deneme1") #Bir dizin-yol olsturur. - Ornek: bir resmi tasyacagin yer
#result = os.path.split("C://deneme") #Yolu parcalar.
result = os.path.splitext("btk_OS_modulu.py") #Ulasilan dosyanin ismi ile uzantisini ayirir.
result = result[0] # Resim ismi degistirmek icin isim ve uzanti ayrilir, isim degisitirilir.
#result = result[1]
print(result) #Tam konumu verilen dosyanin dizin ismini aliriz.










