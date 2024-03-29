"""
Doctest can be put in the top of the script
>>> deck = FrenchDeck()
Class was created!
>>> len(deck)
52
"""

import collections
from random import choice
from datetime import datetime

Card = collections.namedtuple('Card', ['rank', 'suit'])
Card.__doc__ = """
>>> card = Card('A', 'spades')
>>> card.rank
'A'
>>> card.suit
'spades'
"""

class FrenchDeck:
    """Return a FrenchDeck
    
    >>> deck = FrenchDeck()
    Class was created!
    >>> deck.__len__()
    52

    Returns:
        FrenchDeck: A FrenchDeck representation
    """
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs heart".split()
    
    def __new__(cls):
        """
        >>> deck = FrenchDeck().__new__
        Class was created!
        """
        print("Class was created!")
        return super().__new__(cls)
    
    def __init__(self):
        """
        >>> deck = FrenchDeck()
        Class was created!
        """
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
    
    def __call__(self):
        """
        >>> deck = FrenchDeck()
        Class was created!
        >>> deck()
        FenchDeck was called!
        """
        print("FenchDeck was called!")
    
    def __getitem__(self, position):
        """
        >>> deck = FrenchDeck()
        Class was created!
        >>> deck.__getitem__(0)
        Card(rank='2', suit='spades')
        """
        return self._cards[position]
    
    def __len__(self):
        """
        >>> deck = FrenchDeck()
        Class was created!
        >>> deck.__len__()
        52
        """
        return len(self._cards)
    
    def __str__(self):
        """
        >>> deck = FrenchDeck()
        Class was created!
        >>> print(deck)
        FrenchDeck()
        """
        return "FrenchDeck()"

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(choice(deck))

for card in deck: # doctest: +ELLIPSIS
    print(card)
    
suit_values = dict(spades=3, heart=2, diamonds=1, clubs=0)
print(suit_values)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
    
### Working with sorted method
items = [2, 4, 8, 3, 5, 7]
values_level = dict(even=1, odd=0)

def odd_first(value):
    """
    >>> odd_first(5)
    0
    """
    tag = "odd" if value%2!=0 else "even"
    return value*values_level[tag]

for item in sorted(items, key=odd_first):
    print(item)

### Another example
# (id, name, datetime)
db_records = [
    (1,"john", datetime(2024, 1, 15)),
    (2,"pink", datetime(2024, 2, 14)),
    (3,"mark", datetime(2023, 9, 19))
    ]

for record in sorted(db_records, key= lambda item: item[2]):
    print(record)
    
if __name__ == "__main__":
    # python file.py -v
    import doctest
    doctest.testmod()

# python -m doctest -v file.py