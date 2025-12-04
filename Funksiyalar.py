# def salomlashish(ism,fam,ota):
#     return f"Assalomu aleykum {ism} {fam} {ota} jamoamizga hush kelibsiz!"
# ism = input("Ismingizni kiriting: ")
# fam = input("Familyangizni kiriting: ")
# ota = input("Ochestvangizni kiriting: ")
# print(salomlashish(ism,fam,ota))
#

print('='*31)
print('='*9,'KOLKULIATOR','='*9)
print('='*31)

def kolkulyator(X, Y, amal):
    if amal == '-':
        return f"Ayirma: {X-Y}"
    elif amal == '+':
        return f"Yig'indi: {X+Y}"
    elif amal == '*':
        return f"Ko'oaytma: {X*Y}"
    elif amal == '/':
        return f"Bo'linma: {X/Y}"
    elif amal == '√':
        return f"Kvadrat ildiz: {X ** 0.5}"
    elif amal == '²':
        return f"Kvadrati: {X**Y}"
    elif amal == '//':
        return f"Sonlar bo'lindi va butun qismi: {X//Y}"
    elif amal == '%':
        return f"Foizi: {X * Y / 100}"
X = int(input("X sonni kiriting: "))
Y = int(input("Y sonni kiriting: "))
amal = input("Amalni kiriting: ")

print(kolkulyator(X,Y,amal))