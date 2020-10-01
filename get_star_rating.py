# Goal - Get every book title with 2 star rating

import requests
import bs4 
"""
website_url = "http://books.toscrape.com/catalogue/page-{}.html"

website_request = requests.get(website_url.format(1))

class_soup = bs4.BeautifulSoup(website_request.text,'lxml')

spans_of_books = class_soup.select(".product_pod") #select all the span which is under the the class of toctext

#print(soup)
#print(spans_of_classes)
print(len(spans_of_books)) # to see how many books in that page
example = spans_of_books[0]
star_rating = example.select(".star-rating.Three")
print(star_rating)

"""
#get the title - Method one
#title = example.select("a")[1] #the title is inside the <a> tag
#print(title) #we will get 2 <a> tags 1) the first <a> tag is the image
#the second one contains the title inside it
#print(title['title'])
"""

#get the title - Method 2
title = (example.select('a')[1]['title'])
print(title)

"""

Book_titles = []

for n in range(1,51): #pages(1 to 50)
    website_url = "http://books.toscrape.com/catalogue/page-{}.html"
    website_request = requests.get(website_url.format(n))

    soup = bs4.BeautifulSoup(website_request.text, "lxml")
    books = soup.select(".product_pod") #get all the books

    for book in books: #check for 2 star rating books
        if len(book.select(".star-rating.Two")) != 0: #if the list is not empty, if list is empty means the book doesn't have 2 star
            book_title = book.select("a")[1]["title"] #check the <a> tag to find the title
        #in this case the book has 2 <a> tag 1 for the image/link and the scond one([1]) contains the 'title' tag in it
        #so we search the <a> tag and grab the title from it
            Book_titles.append(book_title)

num = -1

for B in Book_titles:
    num += 1
    print(f"Book {num} is {B}")
    

print(f"Total Books with 2 star-rating {num}")


