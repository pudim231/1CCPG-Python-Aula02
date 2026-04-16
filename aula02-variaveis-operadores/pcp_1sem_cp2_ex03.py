CP1 = float(input(f"Colocar nota do checkpoint 1 de 0 a 10: "))
CP2 = float(input(f"Colocar nota do checkpoint 2 de 0 a 10: "))
CP3 = float(input(f"Colocar nota do checkpoint 3 de 0 a 10: "))
SP1 = float(input(f"Colocar nota do Sprint 1 de 0 a 10 : "))
SP2 = float(input(f"Colocar nota do Sprint 2 de 0 a 10 : "))
GS = float(input(f"Colocar nota do Global solution de 0 a 10: "))
menor = 0

if CP1 < CP2 and CP1 < CP3:
    menor = CP1
elif CP3 < CP2 and CP3 < CP2:
    menor = CP3
else:
    menor = CP2


media = (CP1 + CP2 + CP3 - menor + SP1 + SP2 / 4) * 0.4 + GS * 0.6

print(media)