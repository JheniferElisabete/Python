'''
listas são variaveis compostas que armazena de 1 a x valores
append
insert(0, 'x')
pop(1)
remove('x')
len()
sort()
reverse

max()
min()
sum()
'''
#é possivel declarar de 2 modos
#x = []
#y = list()
idade = [18, 20, 30, 40, 15,16,17]
#vai ser adicionado no final da lista
idade.append(24)
#se quiser incluir em uma posição 3 é necessario ter essa posição primeiro / pode incluir string, numeros flutuantes...
idade.insert(3, 7)
#remove a ultima posição se não colocar o paremetro (exemplo: idade.pop())
idade.pop(5)
#remover pelo valor
idade.remove(20)
#retoena a quantidade de elementos dentro da lista
print(len(idade))
#ordena a lista em ordem crescente
idade.sort()
print(idade)
#ordena a lista em ordem decrescente
idade.sort(reverse=True)
print(idade)
#inverte a ordem que esta na lista
idade.reverse()
print(idade)
#Identifica o valor maximo e minimo
print(max(idade))
print(min(idade))
#soma de valores
print(sum(idade))