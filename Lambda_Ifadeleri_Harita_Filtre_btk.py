#tek satirlik fonksiyon, bir ya da daha fazla parametre kabul eder. Tek islem yapar.
#map: Parametre olarak aldığı fonksiyona,parametre olarak aldığı listenin her elemanını sırasıyla parametre olarak gönderir.
#filter:Çağırılan fonksiyonun döndürdüğü değerin true olduğu durumlara göre liste döndürür.
#def square(num) : return num ** 2

"""numbers = [1,3,5,9]
#result = list(map(square,numbers))

result = list(map(lambda num: num**2,numbers))
print(result)"""

"""for item in map(square,numbers):
    print(item)"""

numbers = [1,3,5,9,10,12,6]
square = lambda num: num**2
result1 = list(map(square,numbers))
result2 = square(3)
print(result1)
print(result2)

"""def check(num) : return (num%2==0)
result3 = list(filter(check,numbers))"""
#result3 = list(filter(lambda num: num%2==0,numbers))
checkk = lambda num: num%2==0
result3 = list(filter(checkk,numbers))
result4 = checkk(numbers[2])
print(result3)
print(result4)

name = 'global'
def change():
    name = 'Sevde'
    def Hello():
        #name = 'Ada' #Olursa 'Hello Ada' yazilirdi.
        print('Hello '+name)
    Hello()
change()

#parametre yoksa global yazilmali.
x=50
def test():
    global x
    print(f'x: {x}')
    x=100
    print(f'changed x: {x}')
test() #test(x)