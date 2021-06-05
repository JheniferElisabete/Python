
#No dicionario são indices personalizados exemplo inves de usar 0,1,2,3 pode usar nome,idade,endereço...
#indices no dicionario são chamados de chaves
#declaração de dicionario x ou Y
x = {}
y = dict()
#escrevendo os valores: Variavel = indice : valor
z = {'nome': 'Jhenifer', 'idade': 24, 'telefone':'19999999999'}
print(z)
#printando os valores( eu posso acessar o valor pelo indice, mas não o indice pelo valor
print(z['telefone'])
#retornando a quantidade de elementos (conta a quantidade de elementos)
print(len(z))
#removendo a informação pelo pop
z.pop('idade')
print(z)
#fazendo uma lista de dicionario ( nesse caso estou usando 2 dicionarios
cadastroPessoas = [{'nome': 'Jhenifer', 'idade': 24, 'telefone':'19999999999'}, {'nome': 'Camila', 'idade': 20, 'telefone':'9999999999'}]
print(cadastroPessoas)
#mostrando o a estrutura na posição 1
print(cadastroPessoas[1])
#mostrando o telefone que esta na estrutura 0
print(cadastroPessoas[0]['telefone'])