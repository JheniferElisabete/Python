'''
é possivel criar a prospias funções


'''
#declaramos a função, necessario chamar a função
def mostrarNaTela ():
    print('Ola Mundo')
    print('Fim do programa')
#chamando a função para ser executada
mostrarNaTela()
def somaNumeros(n1, n2):
    print(f'A soma dos numeros é {n1+n2}')
#informas os parametros e executa
somaNumeros(10, 20)
#ou
somaNumeros(n2 = 20, n1 = 10)
#encapsulamento de parametros (quando não sabe qual é a quantidade de parametros) "Pega todos os parametros e faz uma tupla", (apos declarado não pode mudar mais)
def retornaMaior(*list):
    print(max(list))
retornaMaior(1,2,3,4,50,90,30,80)
###### Retornar varores
def retorna():
    return 10
#return joga o 10 para fora da função e dentro de alguma variavel
a = retorna()
print(a)
def retornaSoma(b,c):
    return c+b
#return joga o 10 para fora da função e dentro de alguma variavel
b = retornaSoma(10, 50)
print(b)
#é possivel fazer retonar como uma tupla
def retornaT():
    return 10, 20
d = retornaT()
print(d)
#o primeiro valor do retun correponde a primeira varialvel que estamos jogando para dentro
def retorna():
    return 10,20
e, f = retorna()
print(e)