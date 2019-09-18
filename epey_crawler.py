from bs4 import BeautifulSoup
import requests

main_url = "http://www.epexspot.com/de/marktdaten/dayaheadauktion"
req = requests.get(main_url)
soup = BeautifulSoup(req.text, "html.parser")

# Finding the main title tag.
title = soup.find("table", class_ = "list hours responsive")
line = title.contents
print (len(line))

td = title.find_all("tr", class_ = "no-border")

print (td[0].children)
print (td[1].contents[1].string)


# for x in td[0].children:
#     print(x)


