# module to choose a random value
from random import choice

# each instance of Game refers to each time player plays the guessing game
# Takes the DS quote Storage (list) as an argument
class Game:
    '''
    Game class is for each time a game is being played
    Class takes the DS quote storage (list) as an argument

    Game have attributes like:
    __guess_count, game

    Methods:
        1. __init__(data)
        2. __repr__()
        3. get_guess_count() -> returns the value of private
                                attribute '__guess_count'
        4. decrease_guess_count() -> decreases the value of private
                                     attribute '__guess_count' by 1
        5. game_logic() -> implements the game
        6. get_hint() -> returns the hint for a particular
                         '__guess_count' value
    '''

    # initialize an instance of Game play
    def __init__(self, data):
        self.__guess_count = 4 # max allowed guess (private data)
        # choose an instance from data, which is actually an instance of Person
        self.game = choice(data)

    # returns object state
    def __repr__(self):
        return 'Guessing Game'

    # method to fetch the value of no. of guess left
    def get_guess_count(self):
        return self.__guess_count

    # method to decrease to value of user guess, each time a wrong guess is made
    def decrease_guess_count(self):
        self.__guess_count -= 1

    # method that implements game logic
    def game_logic(self):
        # getting the quote said by a choosen Person instance
        quote = self.game.get_quote()
        print(f'\n\nQuote: {quote}')
        # playing game until 4 guesses are made by user
        while self.get_guess_count() > 0:
            user_guess = input('\nGuess who said ? ')
            self.decrease_guess_count() # decreasing value of guesses left for user
            # checking if user guess matched the Person's name
            if user_guess == self.game.get_name():
                print('Congratulations !!!')
                break
            # if wrong guess is made and user still has not made 4 guesses
            elif self.get_guess_count() in (1,2,3):
                msg = self.get_hint() # getting hint text for display
                print('Hint: ' + msg) # displaying hint text to user
            # if 4 wrong guesses have been made, then displaying message and answer
            else:
                print('Sorry you ran out of of attempts !!!')
                print(f'Answer : {self.game.get_name()}') # displaying answer to user
        
    # method to get the hint text for user
    def get_hint(self):
        # getting the no. of guesses left
        count = self.get_guess_count()
        res = '' # resultant string that will be returned
        if count == 3: # is 3 more guess is left
            # getting birth_date and location information of the instance of Person
            self.game.more_info()
            # getting birthdate value
            res = self.game.get_birthdate()
            return f'Born on {res}' # returning hint text
        elif count == 2:
            # getting location value
            res = self.game.get_location()
            return f'From {res[3:]}' # returning hint text
        else:
            # getting first letter of Person's name
            res = self.game.get_first_letter()
            return f'Name starts with \'{res}\'' # returning hint text