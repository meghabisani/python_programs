from requests import get
from bs4 import BeautifulSoup as soup
import pandas as pd
from time import time,sleep
from random import randint
from warnings import warn
import os

# Clear Screen
def clear():
    os.system( 'cls' )

# Declaration of vars
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

# For every year in the interval of 2000-2018
for year_url in range(2001,2018):

	# For every page in the interval of 1-4
	for start in range(1,152,50):

		# Make request
		url = "http://www.imdb.com/search/title?release_date=" + str(year_url) + "&sort=num_votes,desc&start=" + str(start)
		response = get(url)

		# Pause loop
		sleep(randint(8,15))

		# Monitor the requests
		requests += 1
		elapsed_time = time() - start_time
		# sleep(2)
		clear()
		print("Requests: {}; Frequency: {} requests/s".format(requests, requests/elapsed_time))

		# Warning for non 200 status code
		if response.status_code != 200:
			warn("Requests: {}; Status_Code: {}".format(requests, response.status_code))

		# Break the loop if no of requests exceeds the expectation
		if requests > 76:
			warn("Number of requests was greater than expected.")
			break

		# Parse the contents
		html_soup = soup(response.text, "html.parser")

		# Select all the 50 movie container from the single page
		movie_container = html_soup.find_all("div", {"class":"lister-item mode-advanced"})

		# For every movie
		for movie in movie_container:

			# Scrape the name of movie and year
			name = movie.find("h3", {"class":"lister-item-header"}).a.text.replace(","," |")
			# year = movie.find("span", {"class":"lister-item-year"}).text
			names.append(name)
			years.append(year_url)

			# Scrape the rating
			rating = movie.find("div", {"class":"ratings-imdb-rating"})["data-value"]
			imdb_ratings.append(float(rating))

			# Scrape the Metscore if present
			metascore_container = movie.find("div", {"class":"ratings-metascore"})
			if metascore_container != None:
				metascores.append(int(metascore_container.span.text.strip()))
			else:
				metascores.append("Not Available")

			# Scrape the Votes
			vote = movie.find("span", attrs = {"name":"nv"})["data-value"]
			votes.append(int(vote))


movie_info = pd.DataFrame({"Movie": names,
	"Year": years,
	"Imdb_Rating": imdb_ratings,
	"Metascore": metascores,
	"Votes": votes
	})

print(movie_info.info())
# print(movie_info.head)
movie_info.to_csv('movies_imdb.csv')