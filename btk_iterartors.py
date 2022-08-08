# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:42:56 2022

@author: tosun
"""

class myNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
            
list = myNumbers(10,20)

my_iter = iter(list)
print(next(my_iter))

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

"""for x in list:
    print(x)"""
    
def cube():
    for i in range(20):
        yield i**3 #O an olusturulur, bellekte yer kaplamaz.
        
for i in cube():
    print(i)

"""iterator = cube()
#iterator = iter(generator)
print(next(iterator))"""


#liste = [i**3 for i in range(5)] #Bellekte yer kaplar.
generator = (i**3 for i in range(5))#generator - bellekte yer kaplamaz.
print(generator)
for i in generator:
    print(i)


        