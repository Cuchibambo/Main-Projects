from bs4 import BeautifulSoup
import requests

url = requests.get("http://philippelogel.free.fr/2026/TermSpemaths.php")
Parsethis = url.content
soup = BeautifulSoup(Parsethis, 'html.parser')
CurrentDate = soup.find_all('tr')[-1]
Homework = CurrentDate.find_all('td')[-1]
print(Homework)