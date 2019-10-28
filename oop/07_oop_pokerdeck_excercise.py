from random import shuffle

class Card:
    suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        if suit not in Card.suites:
            raise ValueError("you can not have a {} suite".format(suit))
        self.suit = suit
        if value not in Card.values:
            raise ValueError("you can not have a {} value".format(value))
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Card.suites for v in Card.values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, amount):
        count = self.count()
        actual = min([amount, count])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full deck can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)


d = Deck()
d.shuffle()
card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.cards)
# card2 = d.deal_card()