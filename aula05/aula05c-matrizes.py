from numba.core.cgutils import printf

musicas = [
    ["Dias de luta, dias de glória", "CBJR"],
    ["Só os loucos sabem", "CBJR"],
    ["Nego drama", "Racionais "]
]

#print(musicas[0][1])

for musicas in musicas:
    for info in musicas:
        print(info)
    print()