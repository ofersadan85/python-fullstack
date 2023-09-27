import itertools
import random

# def create_deck():
#     suits = "♥♦♣♠"
#     values = "23456789TJQKA"
#     # ♥ = ALT + 3
#     # ♦ = ALT + 4
#     # ♣ = ALT + 5
#     # ♠ = ALT + 6
#     deck = []
#     for value in values:
#         for suit in suits:
#             card = str(value) + suit
#             deck.append(card)
#     return deck


def create_deck():
    suits = "♥♦♣♠"
    values = "23456789TJQKA"
    return list(itertools.product(values, suits))


def deal_cards(deck, number):
    random.shuffle(deck)
    player_cards = [deck.pop() for i in range(0, number)]
    return player_cards


# def deal_cards(deck, number):
#     player_cards = random.sample(deck, number)
#     for card in player_cards:
#         deck.remove(card)


# def deal_cards(deck, number):
#     player_cards = []
#     for i in range(0, number):
#         card = random.choice(deck)
#         deck.remove(card)
#         player_cards.append(card)


# def deal_cards(deck, number):
#     player_cards = []
#     random.shuffle(deck)
#     for i in range(0, number):
#         card = deck.pop()
#         player_cards.append(card)
