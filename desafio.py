nome = input("Digite seu nome")
print(nome.title())
idade = int(input("Digite sua idade"))
print(idade)

prova1 = 5
prova2 = 5
media = prova1 + prova2
dividindo = media/2
print(dividindo)
if dividindo >= 6 and idade >= 18:
    print('Aprovado')
else:
    print('Reprovado')
