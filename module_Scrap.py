# module Person, which will create an instance of Person
import module_Person

# class Scrapping the information out of the website
class Scrap:
    # initialize an instance of Scrap class, with argument 'url'
    def __init__(self, url):
        self.url = url # the url to scrap
        self.data = [] # the DS quote storage (list) that will hold all instance of Person

    # returns the state of Scrap class
    def __repr__(self):
        return f'Scrapping:\nURL -> {self.url}'

    # method that will scrap the information out
    # 'soup' is given as an argument that is an instance of BeautifulSoup class
    def scrapper(self, soup):
        try:
            quote = soup.find_all(class_='quote') # getting all instance of 'quote' CSS class tag
            # 'quote' is a list of all such instance of 'quote' CSS class
            for each in quote: 
                # creating an instance of Person for each item of 'quote'
                person = module_Person.Person(each)
                # appending instance of Person to DS quote storage (list)
                self.data.append(person)
        except:
            # Exception may occur due to internet connectivity
            print('Some Error Occured. Check your Internet connectivity and try again')
            exit(1)

    # returns the DS quote storage (list)
    def get_data(self):
        return self.data