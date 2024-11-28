from unidecode import unidecode

texto = input("Digite o que você quiser: ")

novoTexto = unidecode(texto)


contadorVogais = 0
for vogal in novoTexto:
    if vogal.lower().strip() in "aeiou":
        print(f'{vogal} é vogal')
        contadorVogais += 1

print(f"Número de vogais: {contadorVogais}")