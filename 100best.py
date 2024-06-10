from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://web.archive.org/web/20240504003319/https://www.empireonline.com/movies/features/best-movies-2/").text #capture the website in text format
souped_html = BeautifulSoup(html_text, 'lxml') #save instance of Beautiful Soup object to a variable, provide the html_text variable and lxml parsing

movies = souped_html.find_all ("h3") #find all elements under the h3 tag
movies_list = [] #find all h3 elements that have been passed through Beautiful Soup
for movie in movies: #instantiating a for loop through the movies that have been captured by Beautiful Soup.
  no_space = ' '.join(movie.text.split()) #used CHAT GPT here as I noticed double whitespaces in the text file in some cases. This splits the code into individual words and the join puts it back together using one whitespace. I used it as I didn't know how to accomplish this.
  movies_list.append(no_space) #loop through the movies and save them to a list
movies_list.reverse() #reverse the list. Found this on https://unstop.com/blog/how-to-reverse-a-string-in-python. Tried it and it worked!
with open("100_best_movies.txt", "w", encoding="utf-8") as file: #this part I used https://www.geeksforgeeks.org/writing-to-file-in-python/ for some help, without adding encoding="utf-8 the text file will not recognise certain characters"
    for title in movies_list: #instantiating a for loop, iterating through the list of movies
        file.write(title + "\n") #save to a text file in list format by iterating through the list writing each movie and separating with /n
file.close()

