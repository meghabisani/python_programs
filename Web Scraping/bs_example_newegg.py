from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
u_client = req(url)
html_page = u_client.read()
u_client.close()

soup_page = soup(html_page, "html.parser")
containers = soup_page.find_all("div", {"class":"item-container"})

headers = "Brand,Title,Shipping,Price,Offers\n"
whandle = open("products.csv", "w")
whandle.write(headers)

for container in containers:
	price = 0
	offer = "No Offers"
	brand_container = container.find("a", {"class":"item-brand"})
	brand = brand_container.img["title"]

	title_container = container.find("a", {"class":"item-title"})
	title = title_container.text.replace(",", " |")

	shipping_container = container.find("li", {"class":"price-ship"})
	shipping = shipping_container.text.strip()

	price_container = container.find("li", {"class":"price-current"})
	int_price = price_container.strong.text.replace(",","")
	float_price = price_container.sup.text
	price = '$' + int_price + float_price
	# price = '$ %.3f' % (float(price_container.strong.text + price_container.sup.text))

	offer_container = price_container.find("a",{"class":"price-current-num"})
	if offer_container != None:
		offer = offer_container.text[1:-1]

	print(price)
	whandle.write(brand + "," + title + "," + shipping + "," + price + "," + offer + "\n")


whandle.close()




