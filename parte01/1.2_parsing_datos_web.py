import requests
import feedparser

url = 'https://github.com/Fhernd/Python-Curso'
respuesta = requests.get(url)
print(respuesta.status_code)