# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:27:30 2022

@author: tosun
"""

#request modulu python kurulumunda hazir olarak gelmez.
#Bu metotla internet sitelerinin kaynak kodlarina erisilebilir.
#jsonplaceolser sayfasi ile Html kodlari yerine json kodlarina ulasilabilir.
#pypi.org'dan ve console ekranindan paketi yukluyoruz.

import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos") #talepte bulunmak istenen adres
#result = result.text #json bilgi
result = json.loads(result.text)
#print(result[0]["title"]) #birinci kaydin baslik kismi
#print(result[0]) #birinci kayit
for i in result:
    if i["userId"] == 1:
         print(i["title"])
    #print(i) #Kayitlar
    #print(i["title"]) #Kayitlarin titile bilgisi
#print(result) #<Response [200]> dogru sonuc verdigini gosterir.
