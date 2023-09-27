from cards import create_deck, deal_cards


deck = create_deck()
number_of_players = 3
for i in range(0, number_of_players):
    player = deal_cards(deck, 5)
    print(player)

print(len(deck))
