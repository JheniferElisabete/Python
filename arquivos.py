'''
dentro de um arquivo de texto com o py de maneira automatica
w -> Escrever
a -> Alterar
r -> Ler
\n -> pula linha
'''
#declara um nome para o arquivo, se existir ele vai trabalhar em cima daquele arquivo, senão ele cria um novo (dentro da pasta que o arquivo principal esta)
#cria uma variavel e usa a função reservada open, na função é necessariuos passar 2 parametros (nome, como vou abrir o arquivo)
arquivo = open('aulaPython.txt','w')
# escrevendo dentro
##arquivo.write('Oi, tudo bem com vcs?')
#é possivel criar uma variavel texto
texto = '''
Oie tudo bem com voces
sou a jhenny

'''
#passando a variavel texto
arquivo.write(texto)
# sempre que abrir arquivo fechar
arquivo.close()
#alterar
arquivo = open('aulaPython.txt','a')
texto = '''Oie tudo bem com voces
sou a jhenny

'''
arquivo.write(texto)
arquivo.close()
#Ler
arquivo = open('aulaPython.txt','r')
##texto = arquivo.read()
##print(texto)
#cria uma lista com cada linhaque ele ler
texto = arquivo.readlines()
print(texto)
#mostra linha por linha
for i in texto:
    print(i)
arquivo.close()
