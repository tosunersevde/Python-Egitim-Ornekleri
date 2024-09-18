import random
rastgele = random.randint(0,100)
toplam = 100
hak = 10
sayi = int(input("Tahmin sayinizi girin: "))
while(hak>0):
    if(sayi==rastgele):
        print(f'Tebrikler Bildiniz! Puaniniz: {toplam} Kalan Hakkiniz: {hak}')
        break
    elif(sayi<rastgele):
        hak-=1
        toplam-=10
        sayi = int(input("Daha Yuksek Bir sayi Girin: "))
        print(f'Kalan Hakkiniz: {hak}')
    else:
        hak -= 1
        toplam -= 10
        sayi = int(input("Daha Kucuk Bir sayi Girin: "))
        print(f'Kalan Hakkiniz: {hak}')
if(hak<=0):
    print(f'Maalesef Kaybettiniz! Puaniniz: {toplam} Hakkiniz Doldu: {hak}')