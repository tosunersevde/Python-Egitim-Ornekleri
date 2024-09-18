message = "Hello World. Merhaba Dunya"
print(message.upper())
#lower(),title(),capitalize()
print(message.split())
print(message.split('.')) #Noktalardan ayirir.
print(''.join(message))
print('*'.join(message)) #Birlestirirken aralara yildiz ekler.
#strip()
print(message[2])
index = message.find('World')
print(index)
isFound = message.startswith('W')
print(isFound) # W ile mi basliyor.
message = message.replace("World","Dunya")
print(message) #harf degisiklerinde kullanilabilir.
message = message.center(50,'*')  #Ortalar ve yildiz koyar.
print(message)