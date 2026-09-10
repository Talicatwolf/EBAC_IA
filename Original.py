import random
import time

# Inicia a contagem do tempo
inicio = time.time()

def gerar_lista_aleatoria(tamanho, limite):
    lista = []
    for _ in range(tamanho):
        lista.append(random.randint(0, limite))
    return lista

def calcular_media(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    return soma / len(lista_numeros)

def encontrar_maximo(lista_numeros):
    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
    return maximo

def encontrar_minimo(lista_numeros):
    minimo = lista_numeros[0]
    for numero in lista_numeros:
        if numero < minimo:
            minimo = numero
    return minimo

def ordenar_lista(lista_numeros):
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] > lista_numeros[j]:
                lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]
    return lista_numeros

# Gerar lista aleatória
tamanho = 10
limite = 100
numeros = gerar_lista_aleatoria(tamanho, limite)

# Aplicar funções e exibir resultados
print(f'Lista gerada: {numeros}')
print(f'Média: {calcular_media(numeros)}')
print(f'Máximo: {encontrar_maximo(numeros)}')
print(f'Mínimo: {encontrar_minimo(numeros)}')
print(f'Lista ordenada: {ordenar_lista(numeros)}')

# Finaliza a contagem do tempo e exibe o resultado
fim = time.time()
tempo_execucao = fim - inicio
print(f'Tempo de execução: {tempo_execucao:.6f} segundos')