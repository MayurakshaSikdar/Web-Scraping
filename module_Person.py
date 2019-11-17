import requests # module for requesting website
from bs4 import BeautifulSoup # module bs4.BeautifulSoup for Scrapping

# each instance of Person refers to the individual person whose quote is listed on the website
class Person:
    '''
    Person class is for each individual Person instance.
    
    Person have attributes like: 
    name, quote, birth_date, about_link, location

    Methods:
        1. __init__()

        2. __repr__()
        
        3. more_info() -> used to get the birth_date
                          and location attributes of Person
        
        4. get_birthdate() -> returns string containing
                              Birth Date info of Person
        
        5. get_location() -> returns string containing place
                             of residence of Person
        
        6. get_first_letter() -> returns string containing 
                                 first letter of Person's name

    '''
    # initializing Person class instance. 'soup' is the object of BeautifulSoup module
    def __init__(self, soup):
        # getting the tag with CSS class 'text'
        quote = soup.find(class_='text')
        self.quote = quote.get_text() # getting the text content under class 'text' tag
        # getting the tag with CSS class 'author'
        name = soup.find(class_='author')
        self.name = name.get_text() # getting the text content under class 'author' tag
        # getting the HTML tag 'a'
        about_link = soup.find('a')
        self.about_link = about_link['href'] # getting value of 'href' in HTML tag 'a'
        # setting birth_date and location attributes to 'None'. When in game a particular
        # instance is choosen, then only the value of these attributes are scrapped
        self.birth_date = None
        self.location = None
    
    # returns object state
    def __repr__(self):
        return '''Person: {}\nQuote: {}\nProfile Link: 
        http://quotes.toscrape.com{}/'''.format(self.name, self.quote, self.about_link)
    
    # gets the value of birth_date and location attributes of a Person instance, 
    # when a particular instance is choosen
    def more_info(self):
        # scrapping instance specific url stored in Person's about_link attribute
        url = 'http://quotes.toscrape.com{}/'.format(self.about_link)
        # Error may occur, mostly internet connectivity
        try:
            resp = requests.get(url) # requesting page
            soup = BeautifulSoup(resp.text, 'html.parser') # making BeautifulSoup object
            # getting Person's birth_date & location attribute using CSS class value 
            self.birth_date = soup.find(class_='author-born-date').get_text()
            self.location = soup.find(class_='author-born-location').get_text()
        except:
            print('Error fetching Birthdate, Location')
    
    # method returning the 'quote' of a choosen instance of Person
    def get_quote(self):
        return self.quote
    
    # method returning the 'name' of a choosen instance of Person
    def get_name(self):
        return self.name

    # method returning the 'birth_date' of a choosen instance of Person
    def get_birthdate(self):
        return self.birth_date
    
    # method returning the 'location' of a choosen instance of Person
    def get_location(self):
        return self.location
    
    # method returning the first letter of Person's 'name' of a choosen instance of Person
    def get_first_letter(self):
        return self.name[:1]

# if __name__ == "__main__":
#     data = []
#     url = 'http://quotes.toscrape.com/page/'
#     resp = requests.get(url+str(1)+'/')
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     if resp.status_code == 200 and soup.find(class_='next'):
#         quote = soup.find_all(class_='quote')
#         for each in quote:
#             data.append(Person(each))
#     else:
#         print('Error')
#     for each in data:
#         each.more_info()
#         print('From '+each.get_location()[3:])