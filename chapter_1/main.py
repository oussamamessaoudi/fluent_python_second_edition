# Fluent Python (Second edition)
# Chapter 1: Python Data Model
import collections
import math
from random import choice

# Build a class (like a database record)
Card = collections.namedtuple('Card', ['rank', 'suit'])
Set()

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(f'len(FrenchDeck()): {len(deck)}')
print(f'FrenchDeck()[0]: {deck[0]}')
print(f'choice(FrenchDeck()): {choice(deck)}')
print('for card in reversed(deck[0:4]):')
for card in reversed(deck[0:4]):
    print(f'\tCard: {card}')
print(f'Card("Q","hearts") in deck: {Card("Q", "hearts") in deck}')
print(f'Card("Q","beats") in deck: {Card("Q", "beats") in deck}')

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print('for card in sorted(deck, key=spades_high)[0:5]:')
for card in sorted(deck, key=spades_high)[0:5]:
    print(f'\tCard :{card}')


# Emulating Numeric Types
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        # for adding
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        # for multiplication
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self) -> str:
        # Generate output for developer
        # !r conversion field
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        # Generate output to end user
        return f'Vector with (x = {self.x} & y = {self.y})'


v1 = Vector(2, 4)
v2 = Vector(2, 1)

v = v1 + v2
print(f'v1 + v2 = {v}')

print(f'abd(v) = {abs(v)}')
print(f'v * 3 = {v}')
