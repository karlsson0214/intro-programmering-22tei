def read_input(message):
    return input(message).lower()


svar = read_input("Är du bra?")
while svar != "ja":
    svar = read_input("Försök igen. Är du bra?")
print("tack och hej")

tärning = 5
ans = input("tärningen visar: " + str(tärning) + ". Vill du kasta igen? ")

print("tärningen visar", tärning)