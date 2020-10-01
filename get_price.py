import requests
import bs4

book_prices = []

for n in range(1,51): #pages(1 to 50)
    website_url = "http://books.toscrape.com/catalogue/page-{}.html"
    website_request = requests.get(website_url.format(n))

    soup = bs4.BeautifulSoup(website_request.text, "lxml")
    books = soup.select(".product_pod") #get all the books

    for book in books: #check for 2 star rating books
        if len(book.select(".product_price")) != 0: #if the list is not empty, if list is empty means the book doesn't have 2 star
            book_price = book.select(".price_color")
            #print(book.select(".price_color"))
            for x in book_price:
                print(x.text)
            book_price = book.select(".class_color") #check the <a> tag to find the title
        #in this case the book has 2 <a> tag 1 for the image/link and the scond one([1]) contains the 'title' tag in it
        #so we search the <a> tag and grab the title from it
            book_prices.append(book_price)

#print(book_prices)