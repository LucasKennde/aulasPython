numerosPares= 0
for numero in range(1,51):
    if numero % 2 == 0:
        numerosPares = numerosPares + numero
        print(f"o número {numero} é par")

print(f'Soma dos numeros pares: {numerosPares}')