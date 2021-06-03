#estrutura de condição x

x = 6
y = 9

# se variavel igual a valor:
if x == 10:
    print("Vc tirou nota 10")
    #senãose
elif x == 9:
    print("Vc tirou 9")
elif x > 11:
    print("Vc tirou mais de 11")
    #quando as duas são verdadeiras
elif x ==9 and y == 9:
    print("Vc tirou 9 nas duas")
    #quando uma das duas for verdadeira
elif x == 9 or y == 9:
    print("Vc tirou 9 em uma")

print("Fim da condição")

'''
#senão por identação
print("Vc não tirou nota 10")
'''
'''
#ou por forta da identação
else:
    print("Vc não tirou nota 10")
    #####################
    operadores:
    != diferente
    < menor
    > maior    
    
'''
