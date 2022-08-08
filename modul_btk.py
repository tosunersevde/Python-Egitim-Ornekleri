#Bu sekilde kutuphane adi kullanilmasi gerekir.
"""import math #math modulu import edilir.
import math as islem
value = dir(math) #math modulu icerisindeki bilesenleri yazdirir.
value2 = help(math) #iceriginin ne oldugu da ogrenilir.
value3 = help(math.factorial) # faktoriyeliceriginin ne oldugu da ogrenilir.
print(value)

value = math.sqrt(49)
value1 = math.factorial(5)
value2 = math.floor(5.9)
value3 = math.ceil(5.9)

print(value)
print(value1)
print(value2)
print(value3)

value = islem.sqrt(49)
print(value)"""

"""from math import *
#from math import factorial,sqrt iki tanesi import edilmis olur.
#math kutuphanesinden butun ozellikleri import edilir.

#def sqrt(x):
    #print('x',str(x))
#en son tanimlanana gore islem yapar.

value = sqrt(49)
print(value)"""

import random

#result = random.random() #0.0 ile 1.0 arasinda sayilar uretilir.
#result = random.random() * 100 üretilen sonuclar 100 ile carpilir.
#result = int(random.uniform(1,100)) #Sayinin tam kismi alinir.
result = random.randint(1,100) #Sayiyi int uretir.

kelime = 'Hello'
liste = ['Selma','Sevde','Hafsa','Halime']
isim = liste[random.randint(0,len(liste)-1)] #Listeden rastgele isim alir.
isimm = random.choice(liste) #Herhangi bir elemanini dondurur.
kelimem = random.choice(kelime) #Karakter dizisinin herhangi bir elemanini dondurur.
print(isim)
print(isimm)
print(kelimem)

listem = list(range(10)) #10'a kadar olan rakamlari sirali listeler.
random.shuffle(listem) #Elemanlarin karisik listelenmesini saglar.
print(listem)

liste2 = range(10)
result2 = random.sample(liste2,3) #rastgele uretilen 10 sayidan ücünğ alir ve listeler.
isimler = random.sample(liste,2)
print(result2)
print(isimler)

