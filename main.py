def mais_um_meio(nota):
    return nota +1.5

notas = [6.5, 7.8, 8.7]
notas_finais = map(mais_um_meio, notas)

print(notas_finais)