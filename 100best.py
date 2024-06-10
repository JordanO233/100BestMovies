from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
print(dir(html_text))
souped_html = BeautifulSoup(html_text, 'lxml')

movies = souped_html.findall('h3')
movies_list = []

for movie in movies:
    print(movie.text.strip())