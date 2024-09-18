# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:42:05 2022

@author: tosun
"""

#Cihazlar arasinda veri tasima islemlerinde kullanilir.
#Json ifade string olmak zorundadir.

import json

person_string = '{"name":"Ali","languages":["English","Turkce"]}'
person_dict = {
    "name":"Ali",
    "languages":["English","Turkce"]
}

#Json String to Dict
"""result = json.loads(person_string)
result = result["languages"][0]
print(result)

with open("json_person.txt") as f:
    data = json.load(f)
    print(data["name"])"""

#Json Dict to String

"""result = json.dumps(person_dict) #Ifadeyi Json yani string ifadeye cevirir.
print(result)

with open("json_person.txt","w") as f:
    json.dump(person_dict, f)"""
    
person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4 ,sort_keys=True) #4 girinti
print(person_dict)
print(result)

    