import collections
from random import choice

Card = collections.namedtuple('Card', ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suites = "spades diamonds clubs hearts".split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suites for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def get_random_card(self):
        return choice(self._cards)

deck = FrenchDeck()
print(len(deck))
print(choice(deck))
print(deck.get_random_card())
