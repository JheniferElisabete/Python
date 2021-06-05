#criar lista grande
x = []
for i in range (1, 1001):
    x.append(i)
print(x)
#ou der uma maneira mais facil
y = list(range (1, 1001))
print(y)
#precisa verificar a lista antes de remover um numero, para não dar erro

z = [1, 2, 3, 4, 5]
print(z)
a = int(input('Digite um numero para apagar da lista'))
if a in z:
    z.remove(a)
    print('removido com sucesso')
print(z)
#Criação de listas de listas
w = [['jhenifer', 24], ['camila', 20]]
#printa lista na posição *
print(w[0])
#printa apenas o nome (printa o que esta na posição 0 das listas e 0 da lista selecionada
print(w[0][0])