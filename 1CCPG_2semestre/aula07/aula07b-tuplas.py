t = ('a', 'b', 'c')
print(t)

t1 = 'a',
print(t1)

print(t[0])

t = tuple("fiap")
print(t)

#atribuição de tuplas

a=5
b=10
print(f"a:{a}, b:{b}")

a,b = b, a
print(f"a:{a}, b:{b}")

email = "fulano@gmail.com"
username, domain = email.split("@")

print(username)
print(domain)