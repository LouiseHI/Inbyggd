# 2Author: Louise Harms
# Date: 2024-09-25

print('Hej, välkommen till gångertabell-kalkulatorn!')
tal_val = int(input('vilken tabell vill du beräkna?: '))

if tal_val >= 0:
    faktorer = list(range(1, 11))
    for i in faktorer:
        print(f'{tal_val} * {i} = {tal_val*i}')