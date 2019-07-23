
print('Bienvenido a la solución al problema TSP con el algoritmo de Kruskal!')
print('Por favor ingres si deseas concetar capitales regionales o provinciales')
print('Escribe R para regionales o P para provinciales:')

tipocapital = input()
if tipocapital == 'R':
    print('genial seran regionales')
elif tipocapital == 'P':
    print('genial seran provinciales')
else:
    print('ingresa un valor P o R, por favor:')

while(tipocapital != 'R' or tipocapital !='P'):
    tipocapital = input()
    if tipocapital == 'R':
        print('genial seran regionales')
        break
    elif tipocapital == 'P':
        print('genial seran provinciales')
        break
    else:
        print('ingresa un valor P o R, por favor:')

print('comencemos')