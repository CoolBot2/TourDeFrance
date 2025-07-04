import requests
from bs4 import BeautifulSoup

numlist = []
namelist = []
url = "https://www.letour.fr/de/rennfahrer"


response = requests.get(url)

# Prüfen, ob die Seite erfolgreich geladen wurde
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    for link in soup.find_all('span', class_="bib"):

        number = link.get_text(strip=True)
        numlist.append(number)


    for link in soup.find_all('a',class_="runner__link"):
        name = link.get_text(strip=True)
        namelist.append(name)




else:
    print(f"Fehler beim Laden der Seite: Statuscode {response.status_code}")
combined = list(zip(numlist, namelist))
print((combined))