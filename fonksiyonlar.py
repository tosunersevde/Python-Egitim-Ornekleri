#liste de bir class'tir. Icerisinde birden fazla metot barindirir.
def sayHello(name = 'user'):
    """"
    DOCSTRING:Mesaj Yazdirma
    INPUT:
    OUTPUT:
    """
    print('Hello '+ name)
sayHello('Sevde')
sayHello()
print(help(sayHello))

"""def add(a,b,c=0):
    return sum((a,b,c))
print(add(10,20,30))"""

def add(*parameter):
    return sum((parameter))
print(add(10,20,30))

def displayUser(**args):
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'Cinar',age=2,city='Istanbul')
displayUser(name= 'Ada',age=2,city='Kocaeli')
displayUser(name= 'Yigit',age=2,city='Ankara')

"""def tekrar(kelime,sayi):
    for i in range(sayi):
        print(kelime)


kelime = input("Kelimeyi girin: ")
sayi = int(input("Kac kez yazdirmak istiyorsunuz?"))
tekrar(kelime,sayi)"""


"""def liste_cevrim(*parametre):
    liste = []
    for i in parametre:
        liste.append(i)
    return liste

result = liste_cevrim(10,20,'Sevde')
print(result)"""

"""def asallar(sayi1,sayi2):
    for i in range(sayi1,sayi2+1):
        if(i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
                else:
                    print(i)

sayi1=int(input("Ilk sayiyi girin:"))
sayi2=int(input("Son sayiyi girin:"))
asallar(sayi1,sayi2)"""

def tam_bolen(sayim):
    tam_bolenler=[]
    for i in range(2,sayim):
        if (sayim%i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

sayim=int(input("Sayiyi girin:"))
print(tam_bolen(sayim))