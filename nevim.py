def vanoce (x):
    van = 358 - x
    return van
def den (x):
    dni = 365 -x
    tyden = dni / 7
    ty =round(tyden)
    return dni,ty
def hodiny (x):
    hod = (365-x) * 24
    return hod
x = int (input ('Kolikati den v roce je : '))
y = den(x)
print ("Do konce roku zbyva dni" ,y[0] ,"a tydnu " ,y[1] ,"A do konce roku zbyva tolik hodin",hodiny(x))
print ("Do Vanoc zbyva dni" ,vanoce(x))

print(round(-16.54))