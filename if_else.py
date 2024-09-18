"""ifade = True
if ifade:
    print("Hos Geldiniz!")
#ifade false olsaydi calismazdi."""

name=input("Adinizi Girin:")
age=int(input("Yasinizi Girin: "))
lesson=input("Egitim Durumunuzu Girin(ilkokul-ortaogretim-lisans): ")

if(age>=18 and (lesson=='ortaogretim' or lesson=='lisans')):
    print("Ehliyet alabilirsiniz!")
else:
    print("Ehliyet alamazsiniz!")

