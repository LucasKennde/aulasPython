numerosPositivos = 0
numerosNegativos = 0
for numero in range(1,11):
    numeroSolicitado = float(input("Digite um número: "))
    if numeroSolicitado > 0:
        numerosPositivos +=1
    else:
        numerosNegativos +=1
    if numeroSolicitado == 0:
        break

print(f'Numeros positivos: {numerosPositivos}')
print('---------------------------------------')
print(f'Numeros negativos: {numerosNegativos}')