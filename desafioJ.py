nome = input('Digite seu nome')
idade = int(input("Digite sua idade"))
n1 = int(input("Digite a primeira nota"))
n2 = int(input("Digite a segunda nota"))

media = (n1+n2)/2

print(nome.lower().title())
if media>=6 and idade >=18:
    print("aluno Aprovado")
else:
    print("Aluno reprovado")