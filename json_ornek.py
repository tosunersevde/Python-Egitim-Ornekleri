# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:19:04 2022

@author: tosun
"""

import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username #Burda kontroller yapilabilir.
        self.password = password
        self.email = email
        
class UserRepository:
    def __init__(self):
        self.users = [] #Direk program icinde user'lara erismek icin
        self.isLoggedIn = False #User giris yapmamis
        self.currentUser = {} #Giris yapmissa ozelliklerine erismek icin
        
        #load usr from .json file
        self.loadUsers()
        
    def loadUsers(self): #Dosya okuma islemi
        if os.path.exists("json_users"):
            with open("json_users","r",encoding = "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    #print(user["name"]) yazabilmek icin string olmamali
                    newUser = User(username = ["username"],password = ["password"],email = ["email"])
                    self.users.append(newUser)
                    #print(user)
            print(self.users)
                   
    def register(self, user: User): #Disardan gelen user bilgisi User tipinde
        self.users.append(user)
        self.savetoFile() #Eklenen listeyi direk dosyaya kaydet
        print("Kullanici Olusturuldu!")
    
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user #Su an kullanan kisi
                print("Login yapildi!")
                break
            
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Cikis yapildi!")
        
    def identity(self):
        if self.isLoggedIn:
            print(f'username : {self.currentUser.username}')
        else:
            print("Giris yapilmadi!")
    
    def savetoFile(self):
        list = []
        
        for user in self.users:
            list.append(json.dumps(user.__dict__)) #class'lar dict'e cevrilerek listeye eklendi.
            
        #class tipindeki nesneler json modulu ile string'e cevrilemez ve dosyaya kaydedilemez.
            
        with open("json_users","w") as file:
            json.dump(list,file) #dump kaydeder, dumps kaydedilecek sekle, json'a, donusturur.

repository = UserRepository() #Dongu icerisinde tanimlanirsa dongu her dondugunde icindeki liste bilgisi sifirlanir.

while True:
    print("Menu".center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity5- Exit\nSeciminiz: ")
    if secim == 5:
        break
    else:
        if secim =='1':
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            
            user = User(username = username, password=password, email=email)
            
            repository.register(user)
            
            #print(repository.users)
            
        elif secim =='2':
            if repository.isLoggedIn:
                print("Zaten giris yaptiniz!")
            else:
                username = input("Username: ")
                password = input("Password: ")
                
                repository.login(username,password)
            
        elif secim =='3':
            repository.logout()
            
        elif secim =='4':
            repository.identity()
        else:
            print("Yanlis Secim!")