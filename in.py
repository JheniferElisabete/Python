# verifica o que esta a esuqerda esta dentro da lista ou a direita
# x retorna falso ou verdadeiro se o 2 esta contido dentro da variavel
x = 2 in(1,2,3,4,5)
print(x)

#para criar lista faz a função range
#y =2 de 1 ate 6

y = 2 in range(1, 6)
print(y)

# range pode alterara de quanto em quanto pula exemplo 2, 4, 6...
#11 ate aquele numero / neste caso esta em ordem crescente/ para ordem descrecente coloca -2 ou -1 para contar de 1 em 1 (-1, 11, -1)

z = 2 in range(2, 11,2)
print(z)
# é possivel concatenar
w = (2 or 10) and (3 or 11) in (1,2,3,4,5,6)

print(w)