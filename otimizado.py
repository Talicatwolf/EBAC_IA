# ==============================================================================
# 1. IMPORTAÇÃO DE MÓDULOS
# ==============================================================================
import random
import time

# Inicia a contagem do tempo
inicio = time.time()

# ==============================================================================
# 2. DEFINIÇÃO DE FUNÇÕES UTILITÁRIAS
# ==============================================================================

def gerar_lista_aleatoria(tamanho: int, limite: int) -> list[int]:
    """
    Gera uma lista com números inteiros aleatórios entre 0 e o limite informado.
    
    Usa 'list comprehension' para construir a lista de forma direta e legível.
    """
    return [random.randint(0, limite) for _ in range(tamanho)]


def calcular_media(lista_numeros: list[number]) -> float:
    """
    Calcula a média aritmética dos valores de uma lista.
    
    Usa a função nativa sum() para performance otimizada.
    """
    if not lista_numeros:
        return 0.0  # Proteção contra ZeroDivisionError se a lista estiver vazia
        
    return sum(lista_numeros) / len(lista_numeros)


def encontrar_maximo(lista_numeros: list[number]) -> number:
    """Retorna o maior elemento utilizando a função nativa max()."""
    if not lista_numeros:
        return None
    return max(lista_numeros)


def encontrar_minimo(lista_numeros: list[number]) -> number:
    """Retorna o menor elemento utilizando a função nativa min()."""
    if not lista_numeros:
        return None
    return min(lista_numeros)


def ordenar_lista(lista_numeros: list[number]) -> list[number]:
    """
    Retorna uma NOVA lista com os elementos ordenados em ordem crescente.
    
    A função nativa sorted() utiliza o Timsort (O(n log n)), muito mais eficiente 
    que o Bubble Sort manual O(n²) e previne a mutação da lista original.
    """
    return sorted(lista_numeros)


# ==============================================================================
# 3. EXECUÇÃO PRINCIPAL (Script de Teste)
# ==============================================================================
if __name__ == "__main__":
    # Configurações de entrada
    TAMANHO_LISTA = 10
    LIMITE_SUPERIOR = 100

    # 1. Geração dos dados
    numeros = gerar_lista_aleatoria(TAMANHO_LISTA, LIMITE_SUPERIOR)

    # 2. Execução dos cálculos
    media = calcular_media(numeros)
    valor_maximo = encontrar_maximo(numeros)
    valor_minimo = encontrar_minimo(numeros)
    numeros_ordenados = ordenar_lista(numeros)

    # 3. Exibição formatada dos resultados
    print(f"Lista gerada:   {numeros}")
    print(f"Média:          {media:.2f}")  # Formata para 2 casas decimais
    print(f"Valor Máximo:   {valor_maximo}")
    print(f"Valor Mínimo:   {valor_minimo}")
    print(f"Lista Ordenada: {numeros_ordenados}")

# Finaliza a contagem do tempo e exibe o resultado
fim = time.time()
tempo_execucao = fim - inicio
print(f'Tempo de execução: {tempo_execucao:.6f} segundos')