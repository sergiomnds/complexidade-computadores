![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

[![Status](https://img.shields.io/badge/Status-Concluído-blue)]()

<h1 align="center">🌡️ Monitoramento de Temperatura de Computadores</h1>

Repositório dedicado ao programa desenvolvido para a Avaliação da disciplina Complexidade de Algoritmos.

O programa gera uma temperatura aleatória de 10 computadores diferentes e os guarda em arquivo de texto. Com base nisso, ela possue as seguintes funcionalidades:
- Gerar NOVOS dados para os computadores;
- Listar os computadores monitorados;
- Listar as leituras de todos os computadores que foram monitorados;
- Listar os computadores em ordem crescente, pela temperatura;
- Mostrar os trio de computadores que possuem temperatura perigosa (acima de 80°C).

<h2>👋🏼 Dependências para rodar o programa: </h2>

<h3>🐍 Python</h3>
O programa foi desenvolvido inteiramente em Python, e deve está instalado na máquina do usuário para funcionar corretamente.

IMPORTANTE: O Interpretor deve está atualizado! Para o desenvolvimento deste programa foi utilizado o Python 3.11.2 64-bit. Recomendo usar esta versão ou superior!

<h3>📚 Bibliotecas Utilizadas: </h3>
As bibliotecas listadas abaixo, exceto 'pydub' e 'pycryptodome', fazem parte da biblioteca padrão do Python, portanto não precisam serem instaladas separadamente, já estão disponíveis assim que o Python é instalado.

Para instalar as bibliotecas 'pydub' e 'pycryptodome', basta executar os seguintes comandos no terminal:

```bash
pip install pydub
```

```bash
pip install pycryptodome
```

<h4>🎲 random</h4>
A biblioteca 'random' em Python fornece funções para gerar números aleatórios e realizar operações relacionadas a probabilidade e estatística.

Neste programa, foi utilizada para gerar as temperaturas aleatórias para os computadores.

<h4>📂 os</h4>
A biblioteca 'os' fornece uma maneira de interagir com o sistema operacional subjacente. Com ela, podemos manipular arquivos e diretórios, executar comandos do sistema, acessar variáveis de ambiente e muito mais.

Neste programa, foi utilizada para manipular o arquivo de texto onde os dados sobre os computadores estão armazenados.

<h4>🧵 threading</h4>
A biblioteca 'threading' é uma biblioteca do Python que fornece suporte para programação concorrente por meio de threads. Além disso, oferece recursos para sincronização e comunicação entre threads.

Neste programa, foi utilizada para dividir as funções em threads, para que elas possam ser executadas simultaneamente.

<h4>#️⃣ hashlib</h4>
A biblioteca hashlib é uma biblioteca padrão do Python que fornece uma interface para cálculos de funções de hash criptográficas.

Neste programa, foi utilizada para gerar a chave de encriptação.

<h4>🎶 pydub</h4>
O PyDub é uma biblioteca Python projetada para simplificar a manipulação e processamento de arquivos de áudio.

Neste programa, foi utilizada para manipular o arquivo de áudio .WAV.

<h4>🙈 pycryptodome</h4>
O pycryptodome é uma biblioteca de criptografia em Python que fornece uma ampla gama de algoritmos criptográficos e ferramentas relacionadas.

Neste programa, foi utilizada para encriptar e decriptar o arquivo de áudio .WAV.

<h2>📷 Galeria</h2>

![menu](https://user-images.githubusercontent.com/85349959/230675288-2280f127-1d05-4e95-9e31-074c83994f57.png)
![opcao-4](https://user-images.githubusercontent.com/85349959/230675350-a1391143-48d7-46d8-b35a-041c86fb8aa5.png)
![opcao-5](https://user-images.githubusercontent.com/85349959/230675465-025717d4-dad1-40d5-8285-c982646462ab.png)
