from random import shuffle


def make_cards():
    suits = ('треф', 'пик', 'бубен', 'червей')
    card_ranges = tuple(str(i) for i in range(2, 11)) + ('валет', 'дама', 'король', 'туз')
    deck = []
    for rang in card_ranges:
        for suit in suits:
            deck.append((rang, suit))
    shuffle(deck)
    for card in deck:
        yield card


a = make_cards()

choice = input('Press Enter for show next card. Press "n" for exit. ')

while choice.lower() != 'n':
    print(*next(a))
    choice = input('Press Enter for show next card. Press "n" for exit. ')
