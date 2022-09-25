import random


class Card:
    """There are 13 possible values when randomly drawing a card.  Generates a random value between
    1 and 13 corresponding to the value of the card.
   
    Attributes:
        value (int): The value of the drawn card.
    """
    def _init_(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = ""
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Die.
        """
        self.value = random.randint(1,13)



