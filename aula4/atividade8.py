notasSomadas = 0
for notas in (1, 6):
    nota = float(input(f"Digite a {notas}º nota"))
    notasSomadas =+ nota

media = notasSomadas/5
if media >= 6:
    print("Parabéns, aprovado!")
else:
    print("Sorry, Estudo mais!")