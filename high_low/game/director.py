from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.card1 = 0
        self.card2 = 0
        self.guess = "l"
        card = Card()
        card.draw()
        self.card2 = card.value


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.update_score()
            self.end_game()
            self.get_output()


    def update_score(self):
        """Determinds if the guess was correct and awards points to the total_score accordingly.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        if self.guess == "l":
            if self.card1 > self.card2:
                points = 100
            elif self.card1 < self.card2:
                points = -75
            else:
                points = 0
        elif self.guess == "h":
            if self.card1 < self.card2:
                points = 100
            elif self.card1 > self.card2:
                points = -75
            else:
                points = 0
        self.total_score += points

    def get_inputs(self):
        """Set and print the first card value.  Ask for higher or lower.  
        Draw and print the second card value.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        card = Card()
        self.card1 = self.card2
        print(f"The card is:  {self.card1}")
        self.guess = input("Higher or lower? [h/l] ")
        card.draw()
        self.card2 = card.value
        print(f"Next card was:  {self.card2}")

    def get_output(self): 
        """Prints the total score and asks to play again.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return        
        print(f"Your score is {self.total_score}")
        playing = input("Play again?  [y/n]")
        print()
        self.is_playing = (playing == "y")
    
    def end_game(self):
        """Automatically end the game if the total_points drop to 0

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        if self.total_score <= 0:
            print("Game Over")
            self.is_playing = False
       

