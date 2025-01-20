hand = [["spader", 2], ["ruter", "kung"],['\u0394', 2], ["ruter", 2], ["klöver", 2]]


antal_2 = 0
for kort in hand:
    print(kort)
    if kort[1] == 2:
        antal_2 += 1

print(f"Antal tvåor: {antal_2}")