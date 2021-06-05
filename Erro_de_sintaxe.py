# para evitar mensagem de erro de sintaxe quando vc perguntar a idedade e o cliente digitar letras, é usado o xomando try
#comando obrigatorios
try:
    x = int(input('Digite sua idade'))
except:
    print('Voce não digitou sua idade')
#comando opcional
else:
    print(f'sua idade é {x}')

#sempre é executado dando erro ou não
finally:
    print('Muito obrigada por acessar nosso site')