# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:51:12 2022

@author: tosun
"""

import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base=" #Varsayilan base turu degisebilir.

bozulan_doviz = input("Bozulan doviz turu: ")
alinan_doviz = input("Alinan doviz turu: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? "))

result = requests.get(api_url+bozulan_doviz) #url sonuna yazilir.
result = json.loads(result.text)
#print(result)
print("1 - {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))

#ilkinde ornek - 1 USD ... TRY
#ikincisinde ornek - 100 USD ...TRY



