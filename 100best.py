from bs4 import BeautifulSoup
import requests
 
html_text = requests.get("https://web.archive.org/web/20240504003319/https://www.empireonline.com/movies/features/best-movies-2/").text #capture the website in text format
 
souped_html = BeautifulSoup(html_text, 'lxml') #save instance of Beautiful Soup object to a variable, provide the html_text variable and lxml parsing
 
 
movies = souped_html.find_all ("h3") #find all elements under the h3 tag
movies_list = [] #find all h3 elements that have been passed through Beautiful Soup

for movie in movies: #instantiating a for loop through the movies that have been captured by Beautiful Soup.
  movies_list.append(movie) #loop through the movies and save them to a list
  print(movies_list)

  