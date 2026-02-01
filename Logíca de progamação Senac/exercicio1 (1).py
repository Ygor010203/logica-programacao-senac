def somar_lista(lista):
 soma = 0
 for i in range(len(lista)):
    soma += lista[i]
 return soma
li = [1,2,3,4,5,6,7,8,9]
resultado = somar_lista(li)
print("resultado: ",resultado)
