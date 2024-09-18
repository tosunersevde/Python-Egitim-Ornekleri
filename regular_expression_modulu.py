# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:17:52 2022

@author: tosun
"""

#Girilen input ifadelerde kontrol yapilmasini saglar.
#Bu iafadeleri kullanarak bir arama islemini re modulu araciligi ile yapabiliriz.

import re

"""result = dir(re)
print(result)"""

#re modulu
str = "Python Kursu : Python Programlama Rehberiniz | 40 Saat"

#re.findall()
"""result = re.findall("Python",str) #Metinde arananlari liste olarak dondurur.
sayi = (len(result))
print(result)
print(sayi)"""

#re.spilit()
"""result = re.split(" ",str) #Bosluklardan itibaren boler, liste dondurur.
#result = re.split("R",str) #R'den hemen oncesinden boler.
print(result)"""

#re.sub()
"""result = re.sub(" ","-",str) #Degistirme islemi yapar.
#result = re.sub("\s","-",str) #Bosluk karakteri \s ile de belirtilebilir.
print(result)"""

#re.search()
"""result = re.search("Python",str) #match objesi dondurur. Buldugu ilk kelimenin hangi katakterler arasinda oldugunu soyler.
#result = result.span() #Konumunu soyler.
#result = result.start() #Hangi karakterden basladigini soyler.
#result = result.end() #Bitis karakterini soyler.
#result = result.group() #Aradigi iafadeyi dondurur.
result = result.string #Hangi metinde aradigini dondurur.
print(result)"""

#regular expression
#result = re.findall("[abc]",str) #Koseli parazntez icerisindeki butun karakterler str icinde aranir. Liste dondurur.
#result = re.findall("[a-z]",str) #a'dan z'ye karakterleri arar.
#result = re.findall("[0-5]",str) #[0-39] : [01239] arar.
#[^abc] : abc karakterleri disinda arama yapar. 
#[^0-9] : rakam olmayan karakterler
#result = re.findall("...",str) #Her uclu grubu dondurur.(Bosluklar da dahil)
#result = re.findall("Py..on",str) #arada farkli karakterler olabilir.
#result = re.findall("^P",str) #String ifade P ile basliyor mu? Evet - Ilk bastaki P'yi dondurur.
#result = re.findall("t$",str) #String ifade t ile bittigi icin t'yi dondurur.
#result = re.findall("Saat$",str) #String ifade 'Saat' ile bittigi icin t'yi dondurur.
#result = re.findall("Sa*t$",str) #a'dan 0 ya da daha fazla var. 'Saat' ifadesini dondurur.
#result = re.findall("Sa+t$",str) #a'dan 1 ya da daha fazla(en az 1) var. 'Saat' ifadesini dondurur.
#result = re.findall("Sa?t$",str) #a'dan 0 ya da 1 tane yok. [] ifadesini dondurur.
#result = re.findall("a{2}",str) #a'dan arka arkaya 2 tane varsa dondurur.
#result = re.findall("a{2,3}",str) #a'dan arka arkaya en az 2 en fazla 3 tane varsa dondurur.
#result = re.findall("[0-9]{2}",str) #0'dan 9'a kadar rakam arar, iki basamakli varsa dondurur.
#result = re.findall("\APython",str) #En basta ifadenin varligini arar.
result = re.findall("Saat\Z",str) #En sonda ifadenin varligini arar.
print(result)

















