#tuple'lar liste ile cok benziyor. Koseli parantez yerine parantez kullaniliyor.
#Eleman ekleme silme islemleri listelerde oldugu gibi yapilamaz.
message = "Hello World. Merhaba Dunya".split()
#Listeye cevirme islemi split(,) ile saglanabilir.
print(message[0])
my_list1 = [1,2,3]
my_list2 = ['Sevde', 'Nur']
#isteler = my_list1 + my_list2
listeler = [my_list1,my_list2]
print(listeler)
print(listeler[0][0])
listeler[0][1] = 2
print(listeler[0][1])
print(len(listeler))
# "Okul" in listeler
fstring = f"{listeler[0][0]} Numarali ogrenci {listeler[1][0]}'dir.'"
print(fstring)

numbers = [0,1,2,4,5]
numbers[3] = 40
numbers.append(45)
numbers.insert(3,78) #verilen index numarasindan once ekler.
numbers.insert(-1,68)
numbers.pop() #En sondan siler. Index Verilir.
numbers.remove(1) #Direk rakami siler.
minumum = min(numbers)
print(minumum)
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5)) #5 kac tane var
print("\n")


letters = ['s','e','v','d','e']
minumumm = min(letters)
letters.sort()
print(minumumm)
print(letters)
letters.reverse()
print(letters)
letters.clear()
print(letters)
