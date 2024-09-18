SevdeHesap  = {
    'ad' : 'Sevde Tosuner',
    'hesapno' : '123456',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

HafsaHesap  = {
    'ad' : 'Hafsa Tosuner',
    'hesapno' : '654321',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if(hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print("Paranizi alabilirsiniz.")
        bakiye_sorgula(SevdeHesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if(toplam>=miktar):
            ek=input("Ek hesabiniz kullanilsin mi?: (e/h)")
            if(ek == 'e'):
                ekkullanim = miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap'] -= ekkullanim
                print("Paranizi alabilirsiniz!")
                bakiye_sorgula(SevdeHesap)
            elif(ek == 'h'):
                print(f"{hesap['hesapno']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print("Uzgunuz! Bakiye yetersiz!")
            bakiye_sorgula(SevdeHesap)

def bakiye_sorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir. Ek hesap Limitiniz {hesap['ekHesap']}'dir.")

paracek(SevdeHesap,3000)
paracek(SevdeHesap,2000)