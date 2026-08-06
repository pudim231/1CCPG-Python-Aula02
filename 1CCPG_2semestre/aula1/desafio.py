endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

#print(endpoints[0])
#print(status[0])
#função que verifica se um status code http é sucesso
#200-299 = sucesso

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299


print(eh_sucesso(status[0][0]))
