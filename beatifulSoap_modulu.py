# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:03:18 2022

@author: tosun
"""

#Bu modulle HTML icerigi analiz edilebilir.
#Bu modul internet uzerinden yuklenmelidir.

html_doc = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>MatematikCanavari.com</title>
    <link rel="stylesheet" href = "style.css">
</head>
<body>
<div class= "menu">
		<ul>
			<li class="#">
				<a href="Anasayfa.html">Anasayfa</a>
			</li>
			<li class="#">
				<a href="Iletisim.html">Iletisim</a>
                <a href="https://google.com.tr">Iletisim</a>
			</li>
			<li class="#">
				<a href="Iletisim.html">Gorsel</a>
				<img src="ornek_resim.png" alt="">
			    </li>
	</div>
</body>
</html>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser") #html dosyasini pars edecek.

#result = soup.prettify() #Bozulan dokuman duzeltilir.
#result = soup.title #<title>MatematikCanavari.com</title
#result = soup.title.name #title gelir.
#result = soup.title.string #MatematikCanavari.com gelir.
"""result = soup.h2 derse tek etiket alirken;
result = soup.find_all('h2') #Butun h2 etiketleri gelir.
result = soup.find_all('h2')[0] #Ilk h2 etiketi gelir."""
#result = soup.find_all('div')[0].ul
#result = soup.find_all('div')[0].ul.li
#result = soup.find_all('div')[0].ul.find_all('li') #Dizi seklinde gelir.
#result = soup.div.findChildren() #Alt elemanlar - cocuklar getirilir.
#result = soup.div.ul.li.findNextSibling() #Bir sonraki kardes li'yi alir.
#result = soup.div.ul.li.findPreviousSibling() #Bir oncekine gecer.

result = soup.find_all('a')
for link in result:
    #print(link)
    print(link.get('href')) #ozelliklere erisilebilir.
#print(result)







