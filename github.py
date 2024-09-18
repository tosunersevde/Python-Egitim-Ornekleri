# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:06:13 2022

@author: tosun
"""
"""Kalici bilgiler data bse'lerde tutulurken;
anlik bilgiler sitelere gonderilen request'ler(talepler ile tutulur."""
import requests

class Githup:
    def __init__(self):
        self.api_url = "https://api.githup.com"
        self.token = "2a0cebe35888589a756953098fb345a5c26fc79b"
        
    def getUser(self,username):
        response = requests.get(self.api_url+"/users/"+username) #bilgi talebi
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+"/users/"+username+"/repos") #bilgi talebi
        return response.json()
    
    def createRepository(self,name):
        response = request.post(self.api_url+"/user/repos?access_token="+self.token+json={
            "name": name,
            "description": "This is your next repository <Some message>",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True}) #gonderme
        return response.json()
    
githup = Githup()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeciminiz:  ")
    if secim == '4':
        break
    elif secim =='1':
        username = input("Username: ")
        result = githup.getUser(username)
        print(f"name: {result['name']} public repos: {result['public repos'] followers: {result['followers']}")
    
    elif secim =='2':
        username = input("Username: ")
        result = githup.getRepositories(username)
        for repo in result:
            print(repo["name"])
        
    elif secim =='3':
        name = input("repository name: ")
        result = githup.createRepository(name)
        print(result)
    else:
        print("Yanlis secim!")