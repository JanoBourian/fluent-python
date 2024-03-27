import collections
from random import choice
from datetime import datetime

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs heart".split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __len__(self):
        return len(self._cards)

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
items = [3, 5, 7, 8, 4, 2]
values_level = dict(even=1, odd=0)

def odd_first(value):
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