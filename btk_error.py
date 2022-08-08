"""try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print("Yanlis bilgi girdiniz!")
    print(e)  # Hangi hataya ait oldugunu belirtmek icin"""

"""while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlis bilgi girdiniz! ",ex)
    else:
         break
    finally:
        print("try except sonlandi! ") #Her durumda cailsir, try - except calissin veya calismasin"""

def check_password(psw):
    import re #parolanin icersinde gezinerek istenen sonuca gore true - false dondurur.
    if(len(psw)<8):
        raise Exception("Paralo en az 8 karakter olmalidir!") #raise ile Exception firlatilir.
    elif not re.search("[a-z]",psw):
        raise Exception("Parola kucuk harf icermelidir!")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola buyuk harf icermelidir!")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam icermelidir!")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alfanumerik karakter icermelidir!")
    elif re.search("[\s]",psw):
        raise Exception("Parola bosluk icermemelidir!")
    else:
        print("Gecerli Parola!")

parola = '1234567aA@'

try:
    check_password(parola)
except Exception as ex:
    print(ex)
else:
    print("Gecerli Parola Olusturuldu!")
finally:
    print("validation tamamlandi!")

class Person:
    def __init__(self,name):
        if(len(name)>10):
            raise Exception("name bilgisi fazla karakter iceriyor.")
        else:
            self.name = name

p = Person("Sevde")
