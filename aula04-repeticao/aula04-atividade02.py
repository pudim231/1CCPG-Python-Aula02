#um programa que dada as duas notas de 0 a 10 e calcula a média aritmética entre elas.

def validar_nota(nota):
    nota_temp = nota
    while nota < 0 or nota > 10:
        print("a nota deve estar entre 0 a 10")
        return float(input("digite novamente a nota:"))
    return nota_temp

#solicitar e validar a primeira nota
notaA = float(input("digite a primeira nota:"))
notaB = float(input("digite a segunda nota:"))
notaA = validar_nota(notaA)
notaB = validar_nota(notaB)
#while notaA < 0 or notaA >10:
    #print("a nota deve estar entre 0 a 10")
    #notaA = float(input("digite novamente a primeira nota:"))

#while notaB < 0 or notaB >10:
    #print("a nota deve estar entre 0 a 10")
    #notaB = float(input("digite novamente a segunda nota:"))


#calculando a média

media = (notaA + notaB) / 2
print("a média é", media)
