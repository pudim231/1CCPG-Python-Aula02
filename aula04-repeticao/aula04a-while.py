cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp = cp + 1

    #while decrecente
print()

i = 4

while i >= 0:
    print(i)
    i -= 1

# repetição com entrada de usuario
print()
#jogar = "sim"

#while jogar.lower() == "sim":
    #print("Repete ou inicia o jogo")
    #jogar = input("Deseja jogar novamente ?")

#Modificadores de laço break - continue
print()
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 7:
        break


    print(f"produto {i}")

