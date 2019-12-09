from requests import get
from bs4 import BeautifulSoup as soup

url = "http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1"
response = get(url)

html_soup = soup(response.text, "html.parser")
movie_container = html_soup.find_all("div", {"class":"lister-item mode-advanced"})

headers = "Movie_Name,Movie_Year,Movie_Rating,Movie_MetaScore,Movie_Votes\n"
whandle = open("Movie_List.csv", "w")
whandle.write(headers)

for movie in movie_container:
	movie_metascore = "Not Available"
	movie_name_container = movie.find("h3", {"class":"lister-item-header"})
	movie_name = movie_name_container.a.text.replace(","," |")

	movie_year_container = movie.find("span", {"class":"lister-item-year text-muted unbold"})
	movie_year = movie_year_container.text

	movie_rating_container = movie.find("div", {"class":"inline-block ratings-imdb-rating"})
	movie_rating = (movie_rating_container["data-value"])

	movie_metascore_container = movie.find("div", {"class":"inline-block ratings-metascore"})
	if movie_metascore_container != None:
		movie_metascore = (movie_metascore_container.span.text.strip())

	movie_votes_container = movie.find("span", attrs = {"name":"nv"})
	movie_votes = (movie_votes_container["data-value"])

	whandle.write(movie_name + "," + movie_year + "," + movie_rating + "," + movie_metascore 
		+ "," + movie_votes + "\n")

whandle.close()