# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:00:18 2022

@author: tosun
"""

"""def my_decorator(func):
    def wrapper():
        print("Fonksiyondan onceki islemler")
        func()
        print("Fonksiyondan sonraki islemler")
    return wrapper
    

@my_decorator #sayHello()'yu my_decorator icerisine gonderir.
def sayHello():
    print("Hello")
sayHello()"""
        
#2.yol   
"""sayHello = my_decorator(sayHello)
sayHello()"""
    
"""def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan onceki islemler")
        func(name)
        print("Fonksiyondan sonraki islemler")
    return wrapper
    

@my_decorator #sayHello()'yu my_decorator icerisine gonderir.
def sayHello(name):
    print("Hello",name)
sayHello("Ali")"""

#Fonksiyon sureleri
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time() #Fonksiyonun baslama zamanini alir.
        time.sleep(1) #Fonksiyonu bir saniye uyutur.
        func(*args,**kwargs)
        finish = time.time() #Fonksiyonun bitis zamanini alir.
        print("Fonksiyon"+func.__name__+" "+str(finish-start)+"saniyede gerceklesti.")
    return inner

@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))
    
@calculate_time 
def faktoriyel(number):
    print(math.factorial(number))

usAlma(2,3)
faktoriyel(4)
    
    
    
    
    
    
    