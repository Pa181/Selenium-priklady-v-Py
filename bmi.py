def na_kg(vaha):
    return vaha * 0.45


def na_metry(vyska):
    return vyska * 0.025


def bmi(vaha, vyska):
    return na_kg(vaha)/ na_metry(vyska) **2

moje_bmi = bmi(226,85)
print(moje_bmi)
print (na_metry (90)