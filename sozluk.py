sehirler = ['Kocaeli','Istanbul']
plaka = [41,34]

#print(plakalar[sehirler.index('Kocaeli')])

plakalar = {'Kocaeli' : 35 , 'Istanbul' : 34}
print(plakalar['Kocaeli'])
plakalar['Ankara'] = 6
plakalar['Kocaeli'] = 41
print(plakalar)

kisiler = {'1.Kisi ' : {'ad': 'Sevde', 'yas':15,'roles':[0,1]} , '2.Kisi ' : {'ad': 'Hafsa', 'yas':5}}
print(kisiler['1.Kisi ']['roles'][0])