listas_frutas = ["banana", "Maçã", "Morango"]

#lista de frutas [0] = banana
#lista de frutas [1] = Maçã
#lista de frutas [2] = Morango
print(listas_frutas[1:3])

listas_frutas.append("Pera")
print(listas_frutas)

qtd_frutas = len(listas_frutas)
print("Qtd de frutas: ",qtd_frutas)

#for indexado para percorrer

for i in range(qtd_frutas):
    print(listas_frutas[i])
print()

#for EACH em python
for fruta in listas_frutas:
    print(fruta)