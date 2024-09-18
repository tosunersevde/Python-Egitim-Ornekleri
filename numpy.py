# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:56:36 2022

@author: tosun
"""

#Veri analizinde kullanılır.
#numpy verileri cok daha az yer kaplar ve cok daha hizli calisirlar.
#Liste islemlerinden daha karmasik isler yapmak icin, buyuk veriler icin kullanilir.

import numpy as np #kisa kullanim

"""#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9]) #tek tek yazilirsa her birini bir parametre olarak algilar.
#listeyi bir numpy dizisine cevirir.

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]] #cok boyutlu liste
np_multi = np_array.reshape(3,3) #matris

print(py_multi)
print(np_multi)

print(np_array.ndim) #array boyut - 1
print(np_multi.ndim) #matris boyut - 2

print(np_array.shape) #sekil bilgisi
print(np_multi.shape)"""

"""result = np.arange(10,50,3) #10-50 arasi 3'er artan dizi
result = np.zeros(10) #10 tane float sifirdan olusan dizi
result = np.ones(10)
result = np.linspace(10,100,5) #Verilen araligi 5 paracaya boler.
result = np.random.randint(0,10) #0-10arasi rastgele bir sayi uretir.
result = np.random.randint(0,10,3) #rastgele sayi listesi
#Sadece bitis degeri verilirse de rastgele sayi uretirken sifirdan baslatir.
result = np.random.rand(5) #rastgele float sayi listesi
result = np.random.randn(5) #rastgele float negatif veya pozitif sayi listesi
print(result)"""

"""np_array = np.arange(50) #50 dahil degil
np_multi = np_array.reshape(5,10) #5-10'luk matris
print(np_multi.sum(axis=1)) #satir toplamlarini verir.
print(np_multi.sum(axis=0)) #sutun toplamlarini verir."""

"""rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.min() #uretilenlerin en kucugu
result = rnd_numbers.max()
result = rnd_numbers.mean() #uretilenlerin ortalamasi
result = rnd_numbers.argmin() #uretilenlerin en kucugunun indeksi
result = rnd_numbers.argmax()
print(result)"""

#Dizi indeksleri
"""numbers = np.array([0,5,10,15,20,25,50,75])
result = numbers[-1] #en sondaki eleman
result = numbers[0:3] #0-3 arasindaki elemanlar, sondaki dahil olmaz.
result = numbers[:3] #0-3 arasindaki elemanlar , 3.dahil degil
result = numbers[3:] #3. indekseten sona kadar git
result = numbers[::] #butun liste
result = numbers[::-1] #sonuncu adim sayisi, listeyi tersten yazar.
result = numbers[::-2] #listeyi tersten 2'ser atlayarak yazar.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers2)
result = numbers2[0] #ilk satiri yazar.
result = numbers2[1,2] #Birinci satirin 2.indeksindeki(3.sutun) eleman
result = numbers2[:,2] #Butun satirlar : ile secilir, 3.sutundakileri yazar.
result = numbers2[:,0:2] #0-2.indeks arasindaki satir-sutun elemanlari
result = numbers2[-1,:] #Son satiri secer ve ordaki butun sutunlari alir.
result = numbers2[:3,:3] #Dizinin tamami
print(result)

arr1 = np.arange(0,10)
#arr2 = arr1 #referans kopyalama
#Degisiklik her iskisinde de olur, ayni adresi gosterdikleri icin
arr2 = arr1.copy() #Farkli adresler
arr2[0] = 20 
#arr1'deki  her ikisini de etkilerken arr2'deki sadece kendisini etkiler.
print(arr1)
print(arr2)
#Degisiklik her iskisinde de olur, ayni adresi gosterdikleri icin"""

#matematiksel islemler
"""numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1)
print(numbers2)
result = numbers1 + numbers2
result = numbers1 + 10 #her elemani uzerine 10 ekler.
result = numbers1 - 10
result = numbers1 - numbers2
result = numbers1 * 10
result = numbers1 * numbers2
result = numbers1 / 10
result = numbers1 / numbers2
result = numbers1 - 10
result = np.sin(numbers1) #sin alir.
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)
print(result)

mnumbers1 = numbers1.reshape(2,3) #2-3'luk matris
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)
result = np.vstack((numbers1,numbers2)) #Dikey olarak birlestirir. Parantezlere dikkat!
result = np.hstack((numbers1,numbers2)) #Yatay olarak birlestirir.
print(result)

result = numbers1 >=50
result = numbers2 %2 == 0
print(numbers2[result]) #true-false degeri donduren degerleri yazar.
print(result) #true-false degerlerini liste seklinde dondurur."""

result = np.random.randint(10,50,15).reshape(3,5)
cift = result[result % 2 == 0]
ciftler = cift[cift > 0]
print(result)
print(ciftler)
































