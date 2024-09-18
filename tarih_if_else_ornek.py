import datetime
tarih = input("Aracinizin trafige cikma tarihini giriniz(2012/12/12): ")
tarih = tarih.split('/')
cikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
bugun = datetime.datetime.now()
fark = bugun - cikis
gun = fark.days

if(gun<=365):
    print("Arac 1.yil bakiminda")
elif(gun>365 and gun<=365*2):
    print("Arac 2.yil bakiminda")
elif(gun>365*2 and gun<=365*3):
    print("Arac 3.yil bakiminda")
else:
    print("Arac 3.yil bakimini gecti bile!")
