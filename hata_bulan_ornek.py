liste = ['1','2','5a','10b','abc']
for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue


while True:
    sayi = input("Sayi Girin: ")
    if(sayi=='q'):
        break
    try:
        result2 = float(sayi)
        print("Girdiginiz sayi: ",result2)
    except ValueError:
        print("Gecersiz deger girildi!")
        continue



def check(parola):
    turkce_karakter = "ğüşİöçĞÜŞÇÖ"
    for i in parola:
        if i in turkce_karakter:
            raise TypeError("Parola Turkce Karakter Iceremez")
        else:
            pass
    print("Gecerli Parola!")

parola = input("Parolanizi girin: ")

try:
    check(parola)
except TypeError as er:
    print(er)

def factorial(x):
    x = int(x)
    if(x<0):
        raise ValueError("Negatif Deger")
    result = 1
    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)