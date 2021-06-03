#FOR
#Criando uma lista dentro de uma lista
# x = [1,2,3,4,5,6,7,8,9,10,11]
# z = 0
for x in range (0, 11, +1):
    print('##########')
    for z in range(0, 11, +1):
        y = x * z
        print(f'{z} x {x} = {y}')

