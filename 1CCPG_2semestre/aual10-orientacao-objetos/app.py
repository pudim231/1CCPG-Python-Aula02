from aluno import Aluno
from disciplina import Disciplina

#criar / instanciar 1 aluno

aluno1 = Aluno("joão", "123456", "cinência da computação")

#criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renovaveis", "André")
dsa = Disciplina("Data Stuctures", "Erick")

#matricular o aluno nas disciplinas
aluno1.matricular(sers)
aluno1.matricular(dsa)
#print(aluno1.disciplinas[0].nome)

#atribuir a(s) nota(s) de cada disciplina ao aluno
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 5)
aluno1.adicionar_nota(dsa, 2)
aluno1.adicionar_nota(dsa, 10)
print(aluno1.calcular_media_d(dsa))
