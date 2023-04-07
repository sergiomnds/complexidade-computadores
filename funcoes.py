'''
Arquivo com as funções utilizadas no programa principal.
Cada função possui uma breve descrição de sua funcionalidade e complexidade.

Autor: Sérgio Mendes
'''
import random
import os

def gerarDados(qntComputadores = 10):
    '''
    Função que gera temperatutas aleatórias para os computadores.
    
    :param qtd_computadores: quantidade de computadores que serão gerados. Por padrão são gerados 10 computadores.
    :type qtd_computadores: int
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão gerados. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    Se a entrada de dados for muito grande, a execução do algoritmo pode levar muito tempo e exigir muita memória.
    '''
    
    # Se o arquivo já existir, ele será removido e um novo arquivo será criado.
    if os.path.exists('computadores.txt'):
        os.remove('computadores.txt')
    
    # Cria uma lista de dicionários com os dados dos computadores
    computadores = []
    for i in range(0, qntComputadores):
        computador = {'id': i + 1, 'temperatura': round(random.uniform(40.0, 120.0), 1)}
        computadores.append(computador)

    # Cria um arquivo e escreve os dados dos computadores
    with open('computadores.txt', 'w') as arquivo:
        for computador in computadores:
            arquivo.write(f'COMPUTADOR {computador["id"]}: {computador["temperatura"]} \n')
        
def listaComputadores():
    '''
    Função que imprime uma lista de computadores monitorados, sem mostrar suas temperaturas.
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão impressos. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    Se a entrada de dados for muito grande, a execução do algoritmo pode levar muito tempo e exigir muita memória.
    '''
    # Define o cabeçalho da tabela
    cabecalho = ["ID - COMPUTADOR"]

    # Cria uma lista de linhas da tabela
    linhas = []

    # Lê o arquivo e adiciona os dados à lista de linhas
    with open('computadores.txt', 'r') as arquivo:
        for linha in arquivo:
            computador = linha.split(":")[0].strip()
            linhas.append([computador])

    # Imprime a tabela
    print("Lista de Computadores:")
    print("-" * 20)
    print(f"{cabecalho[0]:^20}")
    print("-" * 20)
    for linha in linhas:
        print(f"{linha[0]:^20}")
    print("-" * 20)

def listaLeitura():
    '''
    Função que imprime uma lista das leituras feitas sobre os computadores monitorados, mostrando suas temperaturas.
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão impressos. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    Se a entrada de dados for muito grande, a execução do algoritmo pode levar muito tempo e exigir muita memória.
    '''
    
    # Cria uma lista de dados e adiciona os dados do arquivo à lista
    dados = []
    with open('computadores.txt', 'r') as arquivo:
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            dados.append((computador, temperatura))

    # Imprime a tabela
    print('Temperaturas dos computadores: ')
    print("-" * 40)
    print(f'{"ID - COMPUTADOR":<20}{"TEMPERATURA (°C)":^20}')
    print("-" * 40)
    for dado in dados:
        print(f'{dado[0]:<20}{dado[1]:^20}')
    print("-" * 40)

def dadosCrescente():
    '''
    Função que retorna os dados em ordem crescente dentro de uma tabela.
    
    :complexidade: O(n²), onde n é a quantidade de computadores a serem ordenados. São dois loops que percorrem a lista, a cada iteração do loop externo, que percorre toda a lista, o loop interno percorre novamente toda a lista, comparando o elemento atual com o próximo e realizando a troca se necessário.
    
    Se a entrada de dados for muito grande, o tempo de execução do algoritmo pode se tornar impraticável, além de exigir uma quantidade significativa de recursos de memória.
    Por exemplo, se o algoritmo leva 1 segundo para classificar uma lista de 1000 itens, ele levaria 16 minutos para classificar uma lista de 10.000 itens, e cerca de 28 horas para classificar uma lista de 100.000 itens.
    '''
    
    # Lê os dados do arquivo e os adiciona à lista
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            computadores.append((computador, float(temperatura)))  # adiciona o computador e a temperatura à lista

    # Ordena a lista de computadores, usando bubble sort
    n = len(computadores)
    for i in range(n):
        for j in range(0, n-i-1):
            if computadores[j][1] > computadores[j+1][1]:
                computadores[j], computadores[j+1] = computadores[j+1], computadores[j]

    # Imprime a tabela ordenada
    print('Temperaturas dos computadores em ordem crescente: ')
    print("-" * 40)
    print(f'{"TEMPERATURA (°C)":<20}{"ID - COMPUTADOR":^20}')
    print("-" * 40)
    for computador in computadores:
        print(f'{computador[1]:^20}{computador[0]:^20}')
         
def trioTemperatura(limiteTemperatura = 80.0):
    '''
    Função que encontrar todos os possíveis trios de computadores com temperatura acima do limite especificado (80°C)
    
    :param limiteTemperatura: temperatura limite para a busca dos trios. Por padrão é 80°C.
    :type limiteTemperatura: float
    
    :complexidade: O(n³), onde n é a quantidade de computadores a serem ordenados. São três loops aninhados que percorrem a lista de computadores; O primeiro loop percorre todos os computadores, o segundo loop percorre todos os computadores restantes após o primeiro loop, e o terceiro loop percorre todos os computadores restantes após o segundo loop.
    
    O tempo de execução do algoritmo aumenta com o cubo do tamanho da entrada de dados. Isso pode levar a problemas de desempenho significativos em conjuntos de dados grandes.
    Por exemplo, para uma entrada com 100 elementos, um algoritmo com complexidade O(n³) pode levar 1.000.000 unidades de tempo.
    
    Assim, é possível que gere uma situação de necessidade de processamento via força bruta, quando por exemplo, quando a lista de computadores for muito grande.
    '''
    
    # Lê os dados do arquivo e os adiciona à lista
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            computadores.append((computador, float(temperatura)))

    # Encontra os trios de computadores com temperatura acima do limite e os imprime
    n = len(computadores)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if computadores[i][1] > limiteTemperatura and computadores[j][1] > limiteTemperatura and computadores[k][1] > limiteTemperatura:
                    print(f"Trio de computadores com temperatura acima de {limiteTemperatura}°C: {computadores[i][0]}, {computadores[j][0]}, {computadores[k][0]}")
