from model import model_lead

def add_lead():
    name = input("nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")

    # validar as entradas do usuário
    #depois de validar, vamos modelar os dados

    print(model_lead(name, email, company, step))

    #depois de modelado, vamos enciar esse dict(lead) para o leads.json
    #para salvar, vamos usar módulo control


    print("lead adicionado (func)")

    ##def list_leads():
       ## leads = control.read_leads()
       ## if not leads:
       ##     print("nenhuma lead ainda")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")


        opt = input("escolha uma opção:")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("até mais...")
            break
        else:
            print("opção invalida")

if __name__ == "__main__":
    main()