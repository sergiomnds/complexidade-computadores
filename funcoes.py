'''
Arquivo com as funções utilizadas no programa principal.
Cada função possui uma breve descrição de sua funcionalidade e complexidade.

Autor: Sérgio Mendes
'''
import random
import os
import threading
from pydub import AudioSegment
from Crypto.Cipher import AES
import hashlib

def gerarDados(qntComputadores=10, nome_arquivo_audio='floresta.wav'):
    '''
    Função que gera temperaturas aleatórias para os computadores e armazena os dados encriptados em um arquivo.
    
    :param qntComputadores: quantidade de computadores que serão gerados. Por padrão são gerados 10 computadores.
    :type qntComputadores: int
    :param nome_arquivo_audio: nome do arquivo de áudio no formato WAV para gerar as chaves de encriptação.
    :type nome_arquivo_audio: arquivo WAV
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão gerados. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    Se a entrada de dados for muito grande, a execução do algoritmo pode levar muito tempo e exigir muita memória.
    '''
    
    # Se o arquivo já existir, ele será removido e um novo arquivo será criado.
    if os.path.exists('computadores.txt'):
        os.remove('computadores.txt')

    # Carrega o arquivo de áudio e obtém as chaves de encriptação
    chave1, chave2, chave3 = gerar_chaves_audio(nome_arquivo_audio)

    # Gera a chave de encriptação fixa
    chave_encriptacao = gerar_chave_encriptacao(chave1, chave2, chave3)

    # Função auxiliar para encriptar os dados de um computador
    def encriptarDadosComputador(computador):
        temperatura_encriptada = encrypt(computador['temperatura'], chave_encriptacao)
        with open('computadores.txt', 'a') as arquivo:
            arquivo.write(f'COMPUTADOR {computador["id"]}: {temperatura_encriptada}\n')

    # Cria uma lista de dicionários com os dados dos computadores
    computadores = []
    threads = []
    for i in range(qntComputadores):
        computador = {'id': i + 1}
        computador['temperatura'] = round(random.uniform(40.0, 120.0), 1)
        computadores.append(computador)
        thread = threading.Thread(target=encriptarDadosComputador, args=(computador,))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

def gerar_chaves_audio(nome_arquivo):
    '''
    Função que gera as chaves de encriptação a partir de um arquivo de áudio no formato WAV.
    
    :param nome_arquivo: nome do arquivo de áudio no formato WAV.
    :type nome_arquivo: str
    '''
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_wav(nome_arquivo)

    # Obtém os dados brutos do áudio
    dados_audio = audio.raw_data

    # Gera as chaves a partir dos dados brutos do áudio
    chave1 = sum(dados_audio) % 256
    chave2 = sum([dados_audio[i] for i in range(0, len(dados_audio), 2)]) % 256
    chave3 = sum([dados_audio[i] for i in range(1, len(dados_audio), 2)]) % 256

    # Retorna as chaves geradas
    return chave1, chave2, chave3

def gerar_chave_encriptacao(chave1, chave2, chave3):
    '''
    Função que gera uma chave de encriptação a partir de três chaves geradas a partir de um arquivo de áudio no formato WAV.
    
    :param chave1: primeira chave gerada a partir do arquivo de áudio.
    :param chave2: segunda chave gerada a partir do arquivo de áudio.
    :param chave3: terceira chave gerada a partir do arquivo de áudio.
    '''
    # Concatena as chaves em uma única string
    chaves_concatenadas = f'{chave1}{chave2}{chave3}'

    # Converte as chaves em bytes
    chaves_bytes = chaves_concatenadas.encode()

    # Gera uma chave de encriptação de tamanho fixo usando hashlib
    chave_encriptacao = hashlib.sha256(chaves_bytes).digest()

    # Retorna a chave de encriptação
    return chave_encriptacao

def encrypt(dado, chave_encriptacao):
    '''
    Função que encripta um dado utilizando uma chave de encriptação.
    
    :param dado: dado a ser encriptado.
    :param chave_encriptacao: chave de encriptação.
    '''
    # Cria o objeto de cifra AES
    cipher = AES.new(chave_encriptacao, AES.MODE_ECB)

    # Converte o dado para uma string e preenche com zeros à direita para ter um tamanho múltiplo de 16
    dado_str = str(dado).ljust(16, '0')

    # Encripta o dado
    dado_encriptado = cipher.encrypt(dado_str.encode())

    # Retorna o dado encriptado como uma string hexadecimal
    return dado_encriptado.hex()

chave1, chave2, chave3 = gerar_chaves_audio('floresta.wav')
chave_encriptacao = gerar_chave_encriptacao(chave1, chave2, chave3)

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

    # Função auxiliar para processar uma linha do arquivo em uma thread
    def processarLinha(linha):
        computador = linha.split(":")[0].strip()
        linhas.append([computador])
    
    # Lê o arquivo e adiciona os dados à lista de linhas
    with open('computadores.txt', 'r') as arquivo:
        threads = []
        for linha in arquivo:
            thread = threading.Thread(target=processarLinha, args=(linha,))
            threads.append(thread)
            thread.start()
            
        # Aguarda o término de todas as threads
        for thread in threads:
            thread.join()

    # Imprime a tabela
    print("Lista de Computadores:")
    print("-" * 20)
    print(f"{cabecalho[0]:^20}")
    print("-" * 20)
    for linha in linhas:
        print(f"{linha[0]:^20}")
    print("-" * 20)

def listaLeitura(chave_encriptacao=chave_encriptacao):
    '''
    Função que imprime uma lista das leituras feitas sobre os computadores monitorados, mostrando suas temperaturas desencriptadas.
    
    :param chave_encriptacao: chave de encriptação utilizada para desencriptar as temperaturas.
    :type chave_encriptacao: bytes
    
    :complexidade: O(n), onde n é a quantidade de computadores que serão impressos. A medida que a lista cresce, o algoritmo cresce de forma linear quanto a suas operações.
    Se a entrada de dados for muito grande, a execução do algoritmo pode levar muito tempo e exigir muita memória.
    '''
    
    # Cria uma lista de dados e adiciona os dados do arquivo à lista
    dados = []
    
    # Cria um semáforo binário
    semaforo = threading.Semaphore(value=1)
    
    # Função auxiliar para processar uma linha do arquivo em uma thread
    def processarLinha(linha):
        computador, temperatura_encriptada = linha.strip().split(': ')
        
        # Desencripta a temperatura
        temperatura_desencriptada = decrypt(temperatura_encriptada, chave_encriptacao)
        
        # Adquire o semáforo antes de adicionar à lista
        semaforo.acquire()
        dados.append((computador, temperatura_desencriptada))
        semaforo.release()
    
    with open('computadores.txt', 'r') as arquivo:
        threads = []
        for linha in arquivo:
            thread = threading.Thread(target=processarLinha, args=(linha,))
            threads.append(thread)
            thread.start()

        # Aguarda o término de todas as threads
        for thread in threads:
            thread.join()

    # Imprime a tabela
    print('Temperaturas dos computadores: ')
    print("-" * 40)
    print(f'{"ID - COMPUTADOR":<20}{"TEMPERATURA (°C)":^20}')
    print("-" * 40)
    for dado in dados:
        print(f'{dado[0]:<20}{dado[1]:^20}')
    print("-" * 40)

def decrypt(dado_encriptado, chave_encriptacao):
    '''
    Função que desencripta um dado utilizando uma chave de encriptação.
    
    :param dado_encriptado: dado a ser desencriptado.
    :param chave_encriptacao: chave de encriptação.
    '''
    # Cria o objeto de cifra AES
    cipher = AES.new(chave_encriptacao, AES.MODE_ECB)

    # Decifra o dado encriptado
    dado_decifrado = cipher.decrypt(bytes.fromhex(dado_encriptado))

    # Remove o preenchimento de zeros à direita e converte para float
    dado_desencriptado = float(dado_decifrado.rstrip(b'\x00'))

    # Retorna o dado desencriptado
    return dado_desencriptado

def dadosCrescente(chave_encriptacao=chave_encriptacao):
    '''
    Função que retorna os dados desencriptados em ordem crescente dentro de uma tabela.
    
    :param chave_encriptacao: chave de encriptação utilizada para desencriptar as temperaturas.
    :type chave_encriptacao: bytes
    
    :complexidade: O(n²), onde n é a quantidade de computadores a serem ordenados. São dois loops que percorrem a lista, a cada iteração do loop externo, que percorre toda a lista, o loop interno percorre novamente toda a lista, comparando o elemento atual com o próximo e realizando a troca se necessário.
    
    Se a entrada de dados for muito grande, o tempo de execução do algoritmo pode se tornar impraticável, além de exigir uma quantidade significativa de recursos de memória.
    Por exemplo, se o algoritmo leva 1 segundo para classificar uma lista de 1000 itens, ele levaria 16 minutos para classificar uma lista de 10.000 itens, e cerca de 28 horas para classificar uma lista de 100.000 itens.
    '''
    
    # Lê os dados do arquivo e os adiciona à lista
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura_encriptada = linha.strip().split(': ')
            temperatura_desencriptada = decrypt(temperatura_encriptada, chave_encriptacao)
            computadores.append((computador, temperatura_desencriptada))  # adiciona o computador e a temperatura à lista

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

def trioTemperatura(chave_encriptacao=chave_encriptacao, limiteTemperatura=80.0):
    '''
    Função que encontrar todos os possíveis trios de computadores com temperatura acima do limite especificado (80°C)
    
    :param chave_encriptacao: chave de encriptação utilizada para desencriptar as temperaturas.
    :type chave_encriptacao: bytes
    
    :param limiteTemperatura: temperatura limite para a busca dos trios. Por padrão é 80°C.
    :type limiteTemperatura: float
    
    :complexidade: O(n³), onde n é a quantidade de computadores a serem ordenados. São três loops aninhados que percorrem a lista de computadores; O primeiro loop percorre todos os computadores, o segundo loop percorre todos os computadores restantes após o primeiro loop, e o terceiro loop percorre todos os computadores restantes após o segundo loop.
    
    O tempo de execução do algoritmo aumenta com o cubo do tamanho da entrada de dados. Isso pode levar a problemas de desempenho significativos em conjuntos de dados grandes.
    Por exemplo, para uma entrada com 100 elementos, um algoritmo com complexidade O(n³) pode levar 1.000.000 unidades de tempo.
    
    Assim, é possível que gere uma situação de necessidade de processamento via força bruta, quando por exemplo, quando a lista de computadores for muito grande.
    '''
    
    def processar_trios(indices):
        for i, j, k in indices:
            if computadores[i][1] > limiteTemperatura and computadores[j][1] > limiteTemperatura and computadores[k][1] > limiteTemperatura:
                print(f"Trio de computadores com temperatura acima de {limiteTemperatura}°C: {computadores[i][0]}, {computadores[j][0]}, {computadores[k][0]}")
                
    # Lê os dados do arquivo e os adiciona à lista
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura_encriptada = linha.strip().split(': ')
            temperatura_desencriptada = decrypt(temperatura_encriptada, chave_encriptacao)
            computadores.append((computador, temperatura_desencriptada))

    n = len(computadores)
    trios = []
    
    # Gera os índices dos trios a serem processados
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                trios.append((i, j, k))
                
    # Divide os trios entre as threads
    num_threads = min(4, len(trios))  # Defina o número de threads desejado (exemplo: 4)
    tamanho_bloco = len(trios) // num_threads
    blocos = [trios[i:i + tamanho_bloco] for i in range(0, len(trios), tamanho_bloco)]
    
    # Cria as threads e inicia o processamento
    threads = []
    for bloco in blocos:
        t = threading.Thread(target=processar_trios, args=(bloco,))
        t.start()
        threads.append(t)

    # Aguarda a conclusão de todas as threads
    for t in threads:
        t.join()
