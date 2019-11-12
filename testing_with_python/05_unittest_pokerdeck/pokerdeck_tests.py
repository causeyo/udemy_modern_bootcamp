"""
Your goal in this assignment will be to add tests to the classes you created in the last section: Card  and Deck .
Try to test that instances have the right structure, and write some tests for the methods.
Use some before hooks, and try to test for expected errors as well!

Note that the shuffle  method will be difficult to test, since it produces a random output.
Rather than trying to test randomness, you may just want to write some smaller, more straightforward tests.
For instance, you could test that shuffle  doesn't change the size of the deck,
or that the list of cards before the shuffle is in a different order than after the shuffle.

"""

import unittest
from pokerdeck_main import Deck, Card


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Clubs", "7")

    def test_card_suit(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Clubs")
        self.assertEqual(self.card.value, "7")

    def test_card_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "7 of Clubs")

    # def test_say_name(self):
    #     self.assertEqual(
    #         self.mega_man.say_name(),
    #         "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
    #     self.assertEqual(self.mega_man.battery, 49)


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_init(self):
        """decks should have a cards attribute, which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_repr(self):
        """repr should return a string of the form 'Deck of COUNT() of cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_deck_count(self):
        """count should return a count of the number of cards"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number od cards passed"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck is not full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()
