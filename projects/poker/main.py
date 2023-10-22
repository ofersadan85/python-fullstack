from cards import create_deck, deal_cards
from checks import check_hand

deck = create_deck()
number_of_players = 5
for i in range(0, number_of_players):
    player_hand = deal_cards(deck, 5)
    hand_result = check_hand(player_hand)
    print(player_hand, hand_result)

print(len(deck))
