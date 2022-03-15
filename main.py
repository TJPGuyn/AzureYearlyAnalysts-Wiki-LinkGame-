#Go to wikipedia
#Scan/read the page
#click on the nth link (<a>)
#continue scanning pages and going to the nth link until you:
#a. arrive at a page with less than n links
#b. return to a page that you have already visited.
#c. the nth link is an empty link
#d. you land on a non-wikipedia page


import urllib
import bs4


n = input("Choose an iteger 'n': ")

#start on a random page: https://en.wikipedia.org/wiki/Special:Random

