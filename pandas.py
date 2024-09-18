# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:45:32 2022

@author: tosun
"""

#Numpy sayisal islemlerinde kullanilirken Pandas data islemlerinde kullanilir.
#Pandas'ta Numpy'da oldugu gibi elemanlarin ayni veri tipinde olmasi gerekmez.

import pandas as pd
import numpy as np
#import sqlite3
#from numpy.random import randn

#data
"""numbers = [20,30,40,50]
letters = ['a','b','c','d'] #20 de icerisine konulursa tipi object olur.
dict = {'a':10,'b':20,'c':30,'d':40}
rnumbers = np.random.randint(10,100,6)

pandas_series = pd.Series()
pandas_series = pd.Series(numbers) #index verir.
pandas_series = pd.Series(letters)
pandas_series = pd.Series(5,[0,1,2,3,]) #Butun indexlere 5 verir.
pandas_series = pd.Series(numbers,['a','b','c','d']) #a-b-c-d indexlerine numbers elemanlarini verir.
#Numbers eleman sayisi verielen index sayisi ile ayni olmali.
pandas_series = pd.Series(dict)
pandas_series = pd.Series(rnumbers)
pandas_series = pd.Series([20,30,40,51],['a','b','c','d'])
result = pandas_series[-1] #son eleman
result = pandas_series[-2:] #son iki eleman
result = pandas_series['a'] 
result = pandas_series[['a','b']] #bu indekslere karsilik gelenler
result = pandas_series.ndim #boyut verir.
result = pandas_series.dtype #int64
result = pandas_series.shape #kaca-kaclik
result = pandas_series.sum #eleman toplam
result = pandas_series.max 
result = pandas_series.min
result = pandas_series + pandas_series #elemanlar iki katina cikar
result = pandas_series + 50
result = np.sqrt(pandas_series)
result = pandas_series >=50
result = pandas_series % 2 == 0
print(pandas_series[pandas_series%2==0])
print(pandas_series)
print(result)"""

"""opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insigna"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insigna"])

total = opel2018 + opel2019
print(total)
print(total["astra"])"""

#Iki seri toplami = dataframe
#s1 = pd.Series([3,2,0,1])
#s2 = pd.Series([0,3,7,2])

#data = dict(apples = s1,oranges = s2) #DataFrame'lerde kolon isimleri de verilir.

#df = pd.DataFrame(data)

"""data = [["Ali",50],["Ayse",60],["Mehmet",70],["Zeynep",80]]
df = pd.DataFrame([0,1,2,3])
df = pd.DataFrame(data, columns=["Name","Grade"]) #Sutunlara isim verilebilir.
df = pd.DataFrame(data, columns=["Name","Grade"],index = [1,2,3,4]) #indeks no
df = pd.DataFrame(data,[1,2,3,4],["Name","Grade"]) #isimsizse sira bu olmali.
df = pd.DataFrame(data,index =[1,2,3,4],columns=["Name","Grade"],dtype = float)

dict = {"Name":["Ali","Ayse","Mehmet","Zeynep"],"Grade":[50,60,70,80]}
df = pd.DataFrame(dict)
df = pd.DataFrame(dict,index = [212,232,262,292])

dict_list = [
    {"Name":"Ali","Grade":50},
    {"Name":"Ahmet","Grade":60},
    {"Name":"Mehmet","Grade":70},
    {"Name":"Zeynep","Grade":80}
]
df = pd.DataFrame(dict_list,index = [212,232,262,292])
print(df)"""

#DataFrame Dosya okuma
"""#df = pd.read_csv("sample.csv")
#df = pd.read_csv("sample.json",encoding = 'utf-8')
#df = pd.read_csv("sample.xlsx",encoding = 'utf-8')

connection = sqlite3.connect("sample.db") #database baglanti
df = pd.read_sql_query("SELECT * FROM student")
print(df)"""

#DataFrame Satir-Sutun
"""df = pd.DataFrame(randn(3,3),index = ["A","B","C"],columns = ["Column1","Column2","Column3"])
result = df["Column1"]
result = df[["Column1","Column2"]] #Parantezlere dikkat
result = df.loc["A"] #İlk indekse ait sutunlar
#loc["row","column"] - loc["row"] - loc[":","column"]
result = df.loc[:,"Column1"] #tum column1 verileri
result = df.loc[:,"Column1":"Column3"] #column1 ile column3 arasindaki tum veriler
result = df.loc[:,:"Column3"] #column1 ile column3 arasindaki tum veriler
result = df.loc[:"B",:"Column3"] #B'ye kadar olanlar
result = df.iloc[2] #C Satirindakiler
result = df.loc["B","Column3"]
result = df.loc[["A","B"],"Column2","Column3"]

df["Column4"] = pd.Series(randn(3),["A","B","C"])#yeni satir ekleme
df["Column5"] = df["Column1"] + df["Column2"]

result = df.drop("Column5",axis=1,inplace=True) #Silinenin kolon oldugu 1 ile belirtilmeli
#Silindikten sonraki halini yazdirmak icin kullanilir.

print(df)
print(result) #Series"""

#DataFrame Filtreleme
data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])
result = df
result = df.columns
result = df.head(10) #ilk 10 kayit
result = df.tail(10) #son 10 kayit
result = df["Column1"].head(5)
result = df.Column1.head(5)
result = df[["Column1","Column2"]].head(5)
result = df[5:15][["Column1","Column2"]].tail(5) #5-15 arasi son bes kayit

result = df > 50
result = df[df>50]
result = df["Column1"] > 50
result = df[df["Column1"] > 50][["Column1","Column2"]] #Paranteze dikkat
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] < 70)]
result = df.query("Column1 > 50 & Column2 %2 == 0")
result = df.query("Column1 > 50 & Column2 %2 == 0")[["Column1","Column2"]]
print(result)
#print(data)
























