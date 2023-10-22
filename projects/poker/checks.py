from collections import Counter


def check_hand(hand):
    values = []
    for card in hand:
        card_value = card[0]
        values.append(card_value)

    # Could have used shorter "list comprehension":
    # values = [card[0] for card in hand]

    result = Counter(values)  # result = Counter({'5': 3, '9': 1, '8': 1})
    most_common = max(result.values())
    if most_common == 2:
        return "Pair"
    if most_common == 3:
        return "Three of a kind"
    if most_common == 4:
        return "Four of a kind"


# def check_hand(hand):
#     result = {}
#     for card in hand:
#         value = card[0]
#         if value in result.keys():
#             result[value] = result[value] + 1
#         else:
#             result[value] = 1
#     # result = {'5': 3, '9': 1, '8': 1}
#     most_common = max(result.values())
#     if most_common == 2:
#         return "Pair"
#     if most_common == 3:
#         return "Three of a kind"
#     if most_common == 4:
#         return "Four of a kind"
