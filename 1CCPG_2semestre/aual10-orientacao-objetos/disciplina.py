class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina:{self.nome} | Professor: {self.professor}")





# TEMPORÁRIO
# prompt_ia = Disciplina("prompt & IA", "Jorge")
# cs = Disciplina("Computer Science", "Mauricio")
# cs.exibir_infos()