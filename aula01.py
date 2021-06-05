#o arquivo principal é necessario ser mais limpo, é necessario importar os demais arquivos para a pagina principal
##import modulos
#para não ter que ficar escrevendo modulos.printa() toda hora, é possivel definir que modulo vai ser m:
##import modulos as m
#chamando a função(dentro de modulos eu pego a função printa)
##modulos.printa()
##m.printa()
#ou pode importar uma função ou uma variavel no valor
from modulos import printa
from modulos import valorPadrao
printa()
print(valorPadrao)
# é possivel jolocar o valor padrão dentro de uma variavel
v1 = valorPadrao
print(v1)
# é possivel importar clases ou metodos (passando com classes)
from modulos import teste
teste(50)