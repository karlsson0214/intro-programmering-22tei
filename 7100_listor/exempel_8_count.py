import random
colors = ['\u2660', '\u2661', '\u2662', '\u2663']
names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
name_to_value = {}
value = 2
for name in names:
    name_to_value[name] = value
    value += 1

deck = []
for color in colors:
    for value in names:
        deck.append([value, color])


random.shuffle(deck)
hand = []
for i in range(5):
    hand.append(deck.pop())

print(hand)     

antal_2 = 0
for kort in deck:
    # print(kort[0], kort[1])
    if kort[0] == '2':
        antal_2 += 1

print(f"Antal tvåor: {antal_2}")