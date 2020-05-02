# Hlavicka funkce
def ruleta(prvni, posledni):
    # Pomocna promenna
    vysledek = 0
    # For loop
    for cislo in range(prvni, posledni):
        vysledek += cislo
    # Vraceni vysledku
    return vysledek


vzpocet = ruleta(0, 37)
print(vzpocet)

vzpocet = ruleta(5, 322)
print(vzpocet)
