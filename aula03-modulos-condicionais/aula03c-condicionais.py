#estrutura simples
nota_final = 3

if nota_final < 6:
    print("Reprovado")

print("FIM")

#estrutura composta
print()

nota_final = 6

if nota_final < 4:
    print("Reprovado")
else:
    print("Aprovado")

print("FIM")

#estrutura encadeada
print()

nota_final = 4

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")

#estrutura encadeada-elif
print()

nota_final = 6

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
        print("Aprovado")

print("FIM")

