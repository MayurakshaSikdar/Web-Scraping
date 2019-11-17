import requests # module for requesting website
from bs4 import BeautifulSoup # module bs4.BeautifulSoup for Scrapping
import module_Game, module_Scrap # modules for Game and Scrap

if __name__ == "__main__":
    '''
    driver code for Web Scrapping Project
    '''
    # url to scrap -> http://quotes.toscrape.com/page/
    url = 'http://quotes.toscrape.com/page/'
    scrap = module_Scrap.Scrap(url) # calling Scrap class with 'url' as argument
    breadcrumb = 1 # for multiple pages of website
    
    while True:
        try:
            # requesting website for data
            resp = requests.get(url+str(breadcrumb))
            breadcrumb += 1 # next page
            if resp.status_code == 200: # if response is a valid page
                # BeautifulSoup can parse XML, so 'html.parser' needs to be mentioned
                soup = BeautifulSoup(resp.text, 'html.parser')
                # if the 'next' button is available or for last page the 'quote' class
                if soup.find(class_='next') or soup.find(class_='quote'):
                    # calling scrapper() of Scrap class with BeautifulSoup object
                    scrap.scrapper(soup)
                else: break # if no more page with quotes are available
        except: 
            # some error has occured, possibly internet connectivity
            print('Some Error Occured. Check your Internet connectivity and try again')
            exit(1)
    
    # getting list of instances of class Person using get_data() method of Game class
    data = scrap.get_data()
    
    while True:
        try:
            # creating object of Game class with 'data' as an argument
            game = module_Game.Game(data)
            # calling the game_logic() method of Game class, which implements the game
            game.game_logic()
            # for multiple game plays
            play = input('\n\nPlay again (y/Y)? ')
            # checking validity of user input and if user wants to continue or not
            if isinstance(play, str) != True or play.lower() not in ('y', 'yes'):
                print('\n\nThanks for playing !!!')
                break # breaking out if user refuses to play anymore
        except: print('Error')