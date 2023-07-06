"""
This is an example of doctest
>>> deck = FrenchDeck()
>>> len(deck)
52
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ["rank", "suit"])

class FrenchDeck:
    """ Return a French deck 
    
    >>> deck = FrenchDeck()
    >>> deck.__len__()
    52

    Returns:
        FrenchDeck: A French deck
    """
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suites = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def __init__(self):
        """
        >>> deck = FrenchDeck()
        """
        self._cards = [Card(rank, suit) for suit in self.suites for rank in self.ranks]
        
    def __len__(self):
        """
        >>> deck = FrenchDeck()
        >>> deck.__len__()
        52
        """
        return len(self._cards)
    
    def __getitem__(self, position):
        """
        >>> deck = FrenchDeck()
        >>> deck.__getitem__(0)
        Card(rank='2', suit='spades')
        """
        return self._cards[position]
    
    def get_random_card(self):
        return choice(self._cards)

deck = FrenchDeck()
print(len(deck))
print(choice(deck))
print(deck.get_random_card())
print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card.rank, card.suit, card)

for card in reversed(deck):
    print(card)

print(deck._cards)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

if __name__ == "__main__":
    # python file.py -v
    import doctest
    doctest.testmod()

# python -m doctest -v file.py