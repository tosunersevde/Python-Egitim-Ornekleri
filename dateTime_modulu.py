# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:44:09 2022

@author: tosun
"""

#from datetime import date
#import datetime

from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
bugun = datetime.today()

result = simdi.hour
result2 = bugun.year
print(result)
print(result2)

result3 = datetime.ctime(simdi)
result4 = datetime.strftime(simdi,"%Y %X %B") #dateime.python'da yaziyor.
#result4 = datetime.strftime(simdi,"%X")
#result4 = datetime.strftime(simdi,"%d")
#result4 = datetime.strftime(simdi,"%A")
#result4 = datetime.strftime(simdi,"%B")
print("Simdi: ",result3)
print(result4)
print("\n")

#Yazilan string ifade split() ile ayrilabilir.
t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
year = dt.year
print(dt)
print(year)
print("\n")

birthday = datetime(1983,4,9,12,30,10)
birth = datetime.timestamp(birthday) #saniye - 1970'ten itibaren olcer.
birth2 = datetime.fromtimestamp(birth) #saniye to datetime
milat = datetime.fromtimestamp(0) #Bilgisayarlar icin 1970

print(birthday)
print("Saniye:",birth)
print(birth2)
age = simdi - birthday
result5 = age.days
print("Age: ",age) #timedelta
print(result5)
print("\n")

print(simdi)
result6 = simdi + timedelta(days=10,minutes=10) #Bugune,saniyeye 10 gun ekler.
print(result6)


