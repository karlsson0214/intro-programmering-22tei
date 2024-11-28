# definition av funktionen g(x)
# funktionen beräknar kvadraten på x och skriver ut svaret
def g(x):
    svar = x * x
    print(svar)

# Exempel på anrop av funktionen g

i = 1
print("x", "g(x) = x^2")
while i < 6:
    print(i, end=" ") #end=" " används för att unvika ny rad
    g(i)
    i = i + 1
