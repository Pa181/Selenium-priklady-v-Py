def rok (o):
    r = 2020 - o
    return r
def den (o):

    dni = (2020-o) * 365
    tyd = dni / 7
    tyd = round(tyd)
    return dni,tyd
def hodiny (o):
    hod = dni * 24
    return hod
o = int (input ('Ve kterem roce jse se narodil : '))
print ('Je vam let', rok(o))

print ('Pri vasem veku mata dozitych dni a tydnu' , den(o))

