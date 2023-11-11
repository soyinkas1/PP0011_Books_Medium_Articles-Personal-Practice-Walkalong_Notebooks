# Update the `Card` class with the comparison operands overloading
class Card:
    suits = ['Clubs', "Diamonds", 'Hearts', 'Spades']
    ranks = ['narf', 'Ace', '2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1

        # Suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1

        # Ranks are the same ... it's a tie
        return 0

    def __str__(self):
        return self.ranks[self.rank] + ' of ' + self.suits[self.suit]

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne_(self, other):
        return self.cmp(other) != 0


# Update the Deck class with method to remove and deal cards
# Update the Deck class with method to shuffle the deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):  # Outer loop enumerates the suits - 4 times
            for rank in range(1, 14):  # Inner loop enumerates the ranks - 13 times
                self.cards.append(Card(suit, rank))  # 52 cards (4 x 13)

    #     def print_deck(self):
    #         for card in self.cards:
    #             print(card)

    def __str__(self):
        s = " "
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + '\n'
        return s

    def shuffle(self):
        import random
        rng = random.Random()  # Create a random generator
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    # Another shuffle method using random().shuffle
    def shuffle_rng(self):
        import random
        rng = random.Random()  # Create a random generator
        rng.shuffle(self.cards)  # Use its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):  # removes the last card - deal from the back
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break           # Break if out of cards
            card = self.pop()   # Take the top card
            han = hands[i % num_hands]
            han.add(card)


class Hand(Deck):
    def __init__(self, name=''):
        super().__init__()
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = 'Hand ' + self.name
        if self.is_empty():
            s += ' is empty\n'
        else:
            s += ' contains\n'
        return s + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print('Hand {0}: {1} matches {2}'.format(self.name, card, match))
                count += 1

        return count

#
# deck = Deck()
# deck.shuffle()
# hand = Hand('Frank')
# deck.deal([hand], 5)
# print(hand)
#
# game = CardGame()
# hand = OldMaidHand('Frank')
# game.deck.deal([hand], 13)
# print(hand)
#
# hand.remove_matches()
#
# print(hand)


class OldMaidGame(CardGame):

    def __init__(self):
        super().__init__()
        self.hands = None

    def find_neighbour(self, i):
        num_hands = len(self.hands)
        for nest in range(1, num_hands):
            neighbour = (i + nest) % num_hands
            if not self.hands[neighbour].is_empty():
                return neighbour

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def play(self, names):
        # Remove Queen of clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print('--------- Cards have been dealt')
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print('--------- Matches discarded, play begins')
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print('--------- Game is Over')
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbour = self.find_neighbour(i)
        picked_card = self.hands[neighbour].pop()
        self.hands[i].add(picked_card)
        print('Hand', self.hands[i].name, 'picked', picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count



game = OldMaidGame()
game.play(['Allen', 'Jeff', 'Chris'])