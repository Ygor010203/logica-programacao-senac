# exercicio 17-soma numero pares
soma = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero

        print("a soma dos numeros pares entre 1 e 100 e: ",soma)