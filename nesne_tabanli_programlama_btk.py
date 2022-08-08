"""class Person:
    # class attributes
    adress = 'no information'

    # constuctor(yapici metot)
    def __init__(self,name,year):

        # object attributes
        self.name = name
        self.year = year
        #print("init metodu calistirildi.")

    # instance methods
    def intro(self):
        print("Hello There! I'm "+self.name)

    def calculateAge(self):
        return 2022 - self.year

#object(instance)
p1=Person(name='Ali',year=1990)
p2=Person('Yagmur',1995)

#updating
p1.name = 'Ahmet'
p1.adress = 'Kocaeli'

#accessing object attributes
print(f'Name: {p1.name}, Year: {p1.year} Adress: {p1.adress}')
print(f'Name: {p2.name}, Year: {p2.year} Adress: {p2.adress}')

p1.intro()
p2.intro()

print(f"Name: {p1.name},Yas: {p1.calculateAge()}")
print(f"Name: {p2.name},Yas: {p2.calculateAge()}")

#self icin bir parametre gondermeye gerek yoktur. self otomatik olarak olusturulacak objeleri temsil eder.
#self yerine this de denilebilirdi."""

class Circle:
    # class attributes
    pi=3.14

    # constuctor
    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    # instance methods
    def cevre(self):
        return 2 * self.pi * self.yaricap

    def alan(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()
c2 = Circle(5)

print(f"Yaricap: {c1.yaricap} Cevre: {c1.cevre()} Alan: {c1.alan()}")
print(f"Yaricap: {c2.yaricap} Cevre: {c2.cevre()} Alan: {c2.alan()}")

#Inheritance (Kalitim): Miras Alma

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        print("person created")

    def who_am_i(self):
        print("i'm a person.")

class Student(Person):
    def __init__(self,name,lastname,number):
        self.studentnumber = number
        Person.__init__(self,name,lastname)
        print("student created")

    #override - Ayni isimdeki metod temel siniftaki metodu ezer.
    def who_am_i(self):
        print("i'm a student.")
    #Person class'i icindeki metodu ezer.

    def sayHello(self):
        print("Hello i'm a student.")

class Teacher(Person):
    def __init__(self,name,lastname,branch):
        #Person.__init__(self,name,lastname) yerine super() kullanilabilir. super() icerisinde self kullanilmaz.
        super().__init__(name,lastname)
        self.branch = branch

    def who_am_i(self):
        print(f"i'm a {self.branch} teacher.")

p1 = Person('Ali','Yilmaz')
s1 = Student('Fatma','Yilmaz',126)
t1 = Teacher('Sevde', 'Tosuner' , 'Computer')

print(p1.name + ' ' + p1.lastname)
print(f"{s1.name}  {s1.lastname} {s1.studentnumber}")
print(f"{t1.name}  {t1.lastname} {t1.branch}")

p1.who_am_i()
s1.who_am_i()
s1.sayHello()
t1.who_am_i()
#p1 icerisindeki objeye p2 icinden de ulasilabilir.

class Movie:
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi olsuturldu.")

    def __str__(self):
        return f"{self.title} by {self.duration}"

    def __len__(self):
        return self.duration
    #seklinde yazilmalidir. len() metodu icerisnde yoksa calismaz.

    def __del__(self):
        print("Film objesi silindi!")
    #Obje kullanilmadiginda del yazilmasa bile silinir.

m1 = Movie("Fight Club","Tarantino",180)

print(len(m1))
print(str(m1))
#del m1
