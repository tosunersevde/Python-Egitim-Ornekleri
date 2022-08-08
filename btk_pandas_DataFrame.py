# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:10:13 2022

@author: tosun
"""

import pandas as pd
import numpy as np

"""personeller = {
    'Calisan' : ["Sevde","Hafsa","Halime","Selma","Hasan"],
    'Departman' : ["Matematik","Fizik","Kimya","Biyoloji","Sosyal"],
    'Yas' : [30,40,25,15,45],
    'Semt' : ["Bor","Camardi","Altunhisar","Ciftlik","Ulukisla"],
    'Maas' : [5000,6000,7500,1200,3500]    
}

df = pd.DataFrame(personeller)
result = df
result = df["Maas"].sum()
result = df.groupby("Departman").groups #departmana gore gruplar.
result = df.groupby(["Departman","Semt"]).groups 

for name, group in df.groupby("Semt"):
    print(name)
    print(group)
    
result = df.groupby("Semt").get_group("Bor")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Departman")["Maas"].mean() #Sadece maas ort
result = df.groupby("Semt")["Calisan"].count() #Semtlere gore calisan bilgisi
result = df.groupby("Departman")["Maas"].min()  
result = df.groupby("Departman")["Maas"].max()["Matematik"]
result = df.groupby("Departman").agg(np.mean) #ort alir.
result = df.groupby("Departman")["Maas"].agg([np.sum,np.mean,np.min])
#Birden fazla metodu veya alani parantez icinde yazarken [] unutma!
result = df.groupby("Departman")["Maas"].agg([np.sum,np.mean,np.min]).loc["Matematik"]
print(result)"""

#DataFrame ayip bozuk veri
"""data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ['a','b','c','d','e'] , columns = ["column1","column2","column3"])

df = df.reindex(['a','b','c','d','e','f','g','h'])
result = df 
result = df.drop("column1",axis=1)
result = df.drop(["column1","column2"],axis=1)
result = df.drop('a',axis=0)
result = df.isnull()
result = df.notnull().sum()
result = df.notnull()["column1"].sum()

new_column = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = new_column
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"] #column1 icin gecerli olur.

result = df.dropna(axis=0) #İcerisinde null deger olanlar gelmez, olanlari siler.
result = df.dropna(axis=1) #Sutunda varsa siler.
result = df.dropna(how="any") #Hic olmasin
result = df.dropna(how = "all") #Hepsinde varsa gostermesin
result = df.dropna(subset=["column1","column2"]) #column1 ve 2'de arar.
result = df.dropna(subset=["column1","column2"],how = "all")
result = df.dropna(thresh = 2) #En az iki kayit varsa silmez.
result = df.fillna(value = "no input") #olmayan alanlara value'yu yazar.

#result = df.sum() #Kolonlardaki toplamlar
result = df.sum().sum() #Hepsninin toplami
result = df.size() #Eleman sayisi
result = df.isnull.sum()
result = df.isnull.sum().sum() #null deger sayisi

def ortalama(df):
    toplam = df.sum().sum() 
    sayi = df.size() - df.isnull.sum().sum()
    return toplam / sayi

result = df.fillna(value = ortalama(df))
print(result)
#print(df)"""

#pandas string kullanimi
"""data = pd.read.csv("sample.csv")
data.dropna(inplace = True) #Orjinal uzerinde guncelleme yapar.
data["Name"] = data["Name"].str.upper() #Data'daki name kismindaki verileri buyuk harf yapar.
data["Name"] = data["Name"].str.lower() #Data'daki name kismindaki verileri kucuk harf yapar.
data["index"] = data["Name"].str.find('a') #isimde gecen a karakterinin index numaralarini yazar.
data = data.Name.str.contains("Jordan") #Jordan gecenlere true false dondurur.
data = data[data.Name.str.contains("Jordan")] #Jordan gecenleri yazdirir.
data = data.Team.str.replace(" ","-") #Bosluk karakterlerini - ile degistirir.
data[["First Name","Last Name"]] = data["Name"].loc[data["Name"].str.split().str.len() == 2].str.split(expand=True)
#data icerisinde yer alan ad iki kelimeden olusuyor ise onu split ile bolerek yeni kayit olarak ekledik.

print(data)"""

#Tablo Birlestirme
"""customers = {
    'CustomerId':[1,2,3,4],
    'FirstName':["Ahmet","Ali","Hasan","Canan"],
    'LastName':["Yilmaz","Korkmaz","Cevik","Toprak"]
}

orders = {
    'OrderId':[10,11,12,13],
    'CustomerId':[1,2,5,7],
    'OrderDate':['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}

df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

result = pd.merge(df_customers,df_orders,how = "inner") #inner tipinde birlestirme
#Siparisi olanlari yazdirir.
result = pd.merge(df_customers,df_orders,how = "left") #Soldakiler-customer gelsin.
#Siparisi olmayan musteriler de gelir.
result = pd.merge(df_customers,df_orders,how = "right") #Sagdakiler-order gelsin.
#Usterisi olmayan siparisler de gelir.
result = pd.merge(df_customers,df_orders,how = "outer") #Sag - sol butun kayitlar
#Musterisi siparisi olan olmayan hepsi gelir.

print(df_customers)
print(df_orders)
print(result)"""

"""customersA = {
    'CustomerId':[1,2,3,4],
    'FirstName':["Ahmet","Ali","Hasan","Canan"],
    'LastName':["Yilmaz","Korkmaz","Cevik","Toprak"]
}

customersB = {
    'CustomerId':[4,5,6,7],
    'FirstName':["Yagmur","Cinar","Cengiz","Can"],
    'LastName':["Bilge","Turan","Yilmaz","Tuna"]
}

df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB]) #alt alta birlesir.
result = pd.concat([df_customersA,df_customersB],axis = 1) #kolana gore islem yapilir, yana yana gelir.
print(result)"""

#DataFrame Metotlari
data = {
        "Column1":[1,2,3,4,5],
        "Column2":[10,20,13,20,25],
        "Column3":["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df
result = df["Column2"].unique() #Tekrari olamayanlar gelir.
result = df["Column2"].nunique() #Tekrari olamayanlarin sayisi gelir.
result = df["Column2"].value_counts() #Tekrarlama sayilari gelir.
result = df["Column2"] * 2
result = df["Column1"].apply(kareal) #apply'a fonksiyon adi verilebilir.
result = df["Column1"].apply(kareal2) 
result = df["Column1"].apply(lambda x: x * x) 
result = df["Column3"].apply(len) 

df["column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index #index bilgileri - kactan kaca - adim sayisi
result = len(df.index) #Kac satirdan olsur
result = df.info

result = df.sort_values("Column2") #Column2'ye gore siralanir.
result = df.sort_values("Column2", ascending = False) #Tersten siralar.

print(df.pivot_table(index = "Column1",columns ="Column2",values = "Column3"))
#print(df)
print(result)















    





