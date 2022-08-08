"""names = ['Sevde','Nur','Tosuner']
for name in names:
    print(f'my name is {name}')

tuple=[(1,2),(1,3),(5,6)]
for a,b in tuple:
    print(a)"""

"""d = {'k1':1,'k2':2,'k3':3}
#for item in d:
    #print(item)
#for item in d.items():
    #print(item)
for key,value in d.items():
    print(key,value) #print(value)"""


sayilar = [1,3,5,7,9,12,19,21]
liste=[]
toplam=0
"""for i in sayilar:
    toplam+=i
    if(i%3==0):
        liste.append(i)
    else:
        continue"""
yeniliste=[]
for i in sayilar:
    if(i%2==0):
        yeniliste.append(i)
        continue
    else:
        i=i**2
        yeniliste.append(i)
print(sayilar)
print(yeniliste)
"""print(liste)
print(f'toplam:{toplam}')"""

sehirler = ['Kocaeli','Istanbul','Ankara','Izmir','Rize']
for i in sehirler:
    if(len(i)<=5):
        print(i)

urunler = [
    {'name':'Samsung S6','price':3000},
    {'name':'Samsung S7','price':4000},
    {'name':'Samsung S8','price':5500},
    {'name':'Samsung S9','price':6600},
]

fiyat = 0
for i in urunler:
    if(i['price']<=5000):
        print(i['name'])
    else:
        continue
    fiyat+=i['price']
print(fiyat)

"""name = '' #False
while not name.strip(): #Girilen bosluk karakterini siler.
    name = input("Isminizi Girin:")"""

"""sayilarr = [1,3,5,7,9,12,19,21]
x=0
while (x<=len(sayilarr)):
    print(sayilar[x])
    x+=1"""

"""baslangic = int(input("Bir baslangic degeri girin: "))
bitis = int(input("Bir bitis degeri girin: "))
while(baslangic < bitis):
    if(baslangic%2==1):
        print(baslangic)
        baslangic+=1
    else:
        baslangic+=1"""

"""y=100
while(y>0):
    print(y)
    y-=1"""

"""urunler=[]
urun = {}
urun_sayi=int(input("Kac adet urun gireceksiniz?:"))
for i in range(urun_sayi):
    name = input("Urun adini girin: ")
    urun['name'] = name
    fiyat = int(input("Uurun Fiyatini Girin: "))
    urun['price'] = fiyat
    urunler.append(urun)

i=0
while(i<urun_sayi):
    print(urunler)
    i+=1"""

""""#break direk donguyu durdururken continue o anki dongu durumunu es gecer.
z= 0
while(z<5):
    if z==2:
        continue
    print(z)
    z+=1 #Artirma islemi continue dan sonra oldugu icin 2 de surekli basa doner."""

"""for item in range(5,10,2):
    print(item)
print(list(range(5,10,2)))
# 5'den baslar 10'a kadar 2'ser 2'ser artirarak yazdirir. Liste seklinde de direk yazdirilabilir."""

greeting = "Hello World"
for item in enumerate(greeting):
    #print(f'index:{index},letter:{letter}')
    print(item)

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))
for item in zip(list1,list2):
    print(item)
for a,b in zip(list1,list2):
    print(a,b)

numbers = [x for x in range(10)]
print(numbers)
numbers = [x**2 for x in range(10)]
print(numbers)
numbers = [x**x for x in range(10) if(x%3==0)]
print(numbers)

myString = "Hello World"
myList = [letter for letter in myString]
print(myList)

years = [1936,1985,1978,2001,2013]
ages = [2022-age for age in years]
print(ages)

results = [x if(x%2==0) else 'TEK' for x in range(1,10)]
print(results)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)