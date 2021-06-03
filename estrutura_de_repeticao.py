#\n no print quebra linha
#enquanto a condição for verdadeira vai executar o codigo
# para rodar infinitasvezes é so colocar (while True:)

x = 0
while x < 10:
    print(1)
    x = x+1
    #possivel usar x +=1
print('fim do laço')

#pulando o nuemro 5
k = -1
while k < 11:
    k +=1
    if k ==5:
        continue
    print(k)

decisao = 0
while True:
    decisao = int(input('Digite 1 para logar, 2 para cadastrar, 3 sair \n'))
    if decisao ==3:
        #força a saida da aplicação
        print('saindo da aplicação')
        break
    if decisao == 1:
        print('Logando')
    elif decisao == 2:
        print('cadastrando')