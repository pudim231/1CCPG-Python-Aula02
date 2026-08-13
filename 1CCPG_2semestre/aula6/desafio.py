endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 404, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

#print(endpoints[0])
#print(status[0])
#função que verifica se um status code http é sucesso
#200-299 = sucesso -> True

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299


##print(eh_sucesso(200))

#função que detecta 2 erros seguidos nos codigos HTTP de um
#ENDPOINT
#[200, 200, 401, 200, 500] --> /login >> False
#[201, 500, 502, 201, 500] --> /pedidos >>True

def erros_seguidos(codigos_http):
    for i in range (len(codigos_http) - 1):
        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

#print(erros_seguidos(status[2]))

#[200, 200, 401, 200, 500] --> /login
#[201, 500, 502, 201, 500] --> /pedidos

def analisar_endpoint(codigos_http):
    qtd_sucessos = 0
    for codigo in codigos_http:
        if eh_sucesso(codigo):
            qtd_sucessos += 1
    qtd_requisicoes = len(codigos_http)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucesso > 80:
        classificacao = "ESTAVEL"
    else:
        classificacao = "INSTAVEL"
    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

#print(analisar_endpoint(status[2]))

#percorrendo toda a MATRIZ

maior_qtd_erros = -1
endpoints_maior_erro =""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_endpoint)

    print(f"endpoint: {nome_endpoint}")
    print(f"codigo: {codigos_endpoint}")
    print(f"sucessos: {sucessos}")
    print(f"erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"classificação: {classificacao}")
    print("-"* 30)
    print()


    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoints_maior_erro = nome_endpoint
    elif erros == maior_qtd_erros:
        endpoints_maior_erro += " " + nome_endpoint

print(f"Endpoint(s) com + erros: {endpoints_maior_erro} ({maior_qtd_erros})")