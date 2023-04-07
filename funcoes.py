import random
import os

def gerarDados():
    '''
    Função que gera temperatutas aleatórias para os computadores.
    
    :param qtd_computadores: quantidade de computadores que serão gerados. Por padrão são gerados 10 computadores.
    :type qtd_computadores: int
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão gerados. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    '''
    
    # Se o arquivo já existir, ele será removido e um novo arquivo será criado.
    if os.path.exists('computadores.txt'):
        os.remove('computadores.txt')
    
    # Cria uma lista de dicionários com os dados dos computadores
    computadores = []
    for i in range(0, 10):
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

    # Cria a tabela
    # Imprime a tabela ordenada
    print('Temperaturas dos computadores em ordem crescente: ')
    print("-" * 40)
    print(f'{"TEMPERATURA (°C)":<20}{"ID - COMPUTADOR":^20}')
    print("-" * 40)
    for computador in computadores:
        print(f'{computador[1]:^20}{computador[0]:^20}')
         
def trioTemperatura():
    '''
    Função que encontrar todos os possíveis trios de computadores com temperatura acima do limite especificado (80°C)
    
    :complexidade: O(n³), onde n é a quantidade de computadores a serem ordenados. São três loops aninhados que percorrem a lista de computadores; O primeiro loop percorre todos os computadores, o segundo loop percorre todos os computadores restantes após o primeiro loop, e o terceiro loop percorre todos os computadores restantes após o segundo loop.
    '''
    
    # Lê os dados do arquivo e os adiciona à lista
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            computadores.append((computador, float(temperatura)))

    # Encontra os trios de computadores com temperatura acima do limite e os imprime
    limite_temperatura = 80
    n = len(computadores)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if computadores[i][1] > limite_temperatura and computadores[j][1] > limite_temperatura and computadores[k][1] > limite_temperatura:
                    print(f"Trio de computadores com temperatura acima de {limite_temperatura}°C: {computadores[i][0]}, {computadores[j][0]}, {computadores[k][0]}")
