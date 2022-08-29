"""values = 1,2,3,4,5
x,y,*z = values
#basina yildiz koyarsak z icin de ayri bir liste olusturulur.
print(x,y,z)

#not(x>0) Sayinin negatif oldugu anlamina gelir.

#sayi = int(input("Bir sayi girin:"))
#if(sayi>100):
    #print("Sayiniz 100'den buyuk")"""



name = input("Adiniz: ")
kg = int(input("Kilogram cinsinden kilonuz: "))
boy = float(input("m cinsinden boyunuz: "))

kitle = (kg) / (boy**2)
if(kitle<19):
    print(f'{name} Beden kitele indeksiniz: {kitle} Degerlendirme Zayif')
elif(19<=kitle<=25):
    print(f'{name} Beden kitele indeksiniz: {kitle} Degerlendirme Normal')
elif(kitle>25):
    print(f'{name} Beden kitele indeksiniz: {kitle} Degerlendirme Obez')

# x = 5, y = 5, x is z = True , x is not z = True
"""liste = [0,1,2,3]
for i in range(len(liste)):
    if(1 in liste):
        return true
#not in """
