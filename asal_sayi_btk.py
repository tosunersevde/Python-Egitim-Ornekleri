sayi=int(input("Bir Sayi girin: "))
asalmi=True
if(sayi==1 or sayi==0):
    asalmi=False
for i in range(2,sayi):
    if(sayi%i==0):
        asalmi=False
        break
if asalmi:
    print("Sayiniz Asaldir!")
else:
    print("Sayiniz Asal Degildir!")
