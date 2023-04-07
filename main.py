from funcoes import *

gerarDados()
print('Bem vindo ao Sistema de Monitoramento de Temperatura de Computadores!!')
print('O total de 10 computadores já foram gerados com sucesso! Se desejar gerar NOVOS dados, escolha a opção 1 no menu. \n')

try:
    while True:
        print("Escolha uma opção:")
        print("1 - Gerar dados aleatórios")
        print("2 - Imprimir lista de computadores monitorados")
        print("3 - Imprimir as leituras por computador monitorado")
        print("4 - Ordenar os dados em ordem crescente")
        print("5 - Imprimir trio de computadores com temperatura perigosa (acima de 80°C)")
        print("6 - Sair")
        try:
            opcao = int(input("Opção escolhida: "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == 1:
            gerarDados()
            print("Dados gerados com sucesso! \n")
        elif opcao == 2:
            listaComputadores()
        elif opcao == 3:
            listaLeitura()
        elif opcao == 4:
            dadosCrescente()
        elif opcao == 5:
            trioTemperatura()
        elif opcao == 6:
            print('\nObrigado por utilizar o Sistema de Monitoramento de Temperatura de Computadores!!')
            break
        else:
            print("Opção inválida. Tente novamente. \n")
except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário. Encerrando...')
