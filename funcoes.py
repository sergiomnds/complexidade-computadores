import random
import os
from prettytable import PrettyTable

def gerarDados():
    # cria uma lista com 10 dicionários que representam as pessoas
    if os.path.exists('computadores.txt'):
        os.remove('computadores.txt')
    
    computadores = []
    for i in range(1, 11):
        computador = {'id': i, 'temperatura': round(random.uniform(40.0, 120.0), 1)}
        computadores.append(computador)

    # cria um arquivo de texto e escreve os dados das pessoas nele
    with open('computadores.txt', 'w') as arquivo:
        for computador in computadores:
            arquivo.write(f'COMPUTADOR {computador["id"]}: {computador["temperatura"]} \n')

    print('Temperaturas dos computadores gerados com sucesso!')

def dadosCrescente():
    with open('computadores.txt', 'r') as arquivo:
        computadores = []
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            computadores.append((computador, float(temperatura)))  # adiciona à lista como uma tupla (pessoa, idade)

    computadores_ordem_crescente = sorted(computadores, key=lambda computador: computador[1])  # ordena a lista de pessoas pela temperatura

    # imprime a tabela ordenada
    tabelaCrescente = PrettyTable()
    tabelaCrescente.field_names = ["TEMPERATURA (°C)", "ID - COMPUTADOR"]
    for computador, temperatura in computadores_ordem_crescente:
        tabelaCrescente.add_row([temperatura, computador])
    
    print('Temperaturas dos computadores em ordem crescente: ')
    print(tabelaCrescente)
        
def listaComputadores():
    tabelaComputadores = PrettyTable()
    tabelaComputadores.field_names = ["ID - COMPUTADOR"]
    
    with open('computadores.txt', 'r') as arquivo:
        for linha in arquivo:
            computador = linha.strip().split(': ')[0]
            tabelaComputadores.add_row([computador])
    
    print('Lista de computadores monitorados: ')
    print(tabelaComputadores)

def listaLeitura():
    tabelaLeitura = PrettyTable()
    tabelaLeitura.field_names = ["ID - COMPUTADOR", "TEMPERATURA (°C)"]

    with open('computadores.txt', 'r') as arquivo:
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            tabelaLeitura.add_row([computador, temperatura])

    print('Temperaturas dos computadores: ')
    print(tabelaLeitura)
            
def relatorioTemperatura():
    tabela_temperatura_perigosa = PrettyTable()
    tabela_temperatura_perigosa.field_names = ["ID - COMPUTADOR", "TEMPERATURA PERIGOSA (ACIMA DE 80°C)"]
    
    tabela_temperatura_ideal = PrettyTable()
    tabela_temperatura_ideal.field_names = ["ID - COMPUTADOR", "TEMPERATURA IDEAL (ENTRE 60°C E 80°C)"]
    
    tabela_temperatura_abaixo = PrettyTable()
    tabela_temperatura_abaixo.field_names = ["ID - COMPUTADOR", "TEMPERATURA ABAIXO DO IDEAL (ABAIXO DE 60°C)"]
    
    with open('computadores.txt', 'r') as arquivo:
        for linha in arquivo:
            computador, temperatura = linha.strip().split(': ')
            if float(temperatura) > 80:
                tabela_temperatura_perigosa.add_row([computador, temperatura])
                
            elif float(temperatura) >= 60 and float(temperatura) <= 80:
                tabela_temperatura_ideal.add_row([computador, temperatura])
                
            elif float(temperatura) < 60:
                tabela_temperatura_abaixo.add_row([computador, temperatura])
                
    print('Relatório de temperatura dos computadores: ')
    print('Temperatura perigosa: ')
    print(tabela_temperatura_perigosa)
    print('Temperatura ideal: ')
    print(tabela_temperatura_ideal)
    print('Temperatura abaixo do ideal: ')
    print(tabela_temperatura_abaixo)
