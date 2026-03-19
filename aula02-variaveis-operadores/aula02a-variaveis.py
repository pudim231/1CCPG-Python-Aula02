print("ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") #concatenando strings

# comentario de 1 linha
'''
comentarios de
múltiplas
linhas
'''


#variaveis

nome = "Alexandre" # str
idade = 26 #int
peso = 70.2 #float

print("oiiii \n",nome, idade, peso)
print(f"olá, {nome}!!!!")

# INPUT -- simulação de forms no cmd

nome =input("digite o seu nome:")
idade = int(input("digite sua idade:"))
peso = input("digite seu peso:")
print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 1999
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")