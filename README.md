# 📊 Projeto: Tabela de Distribuição de Frequência em Python

Este projeto implementa, em **Python puro**, a construção de uma **tabela de distribuição de frequências** utilizada em estatística descritiva.  
O usuário informa N valores numéricos e o número de classes desejado, e o programa:

- Ordena os valores  
- Calcula a amplitude total  
- Determina o tamanho de cada classe  
- Monta faixas de classe  
- Calcula:
  - Frequência absoluta (fi)
  - Frequência relativa (fr)
  - Frequência acumulada (Fac)
- Exibe uma tabela formatada diretamente no terminal, sem bibliotecas automáticas.

---

## 🚀 Objetivo do Projeto

Este projeto tem finalidade acadêmica e prática, unindo:

- lógica de programação  
- fundamentos de estatística  
- manipulação de listas  
- cálculos manuais  
- formatação de saída no terminal  

Sem utilizar bibliotecas como `pandas` ou ferramentas prontas de estatística — **todo cálculo é feito manualmente**.

---

## 📂 Estrutura do Projeto

estatistica-tabelas-de-frequencia-python/
│
├── main.py # Ponto de entrada do programa
├── tabela_frequencia.py # Lógica de cálculo e construção da tabela
└── README.md # Documentação do projeto

## 🛠️REQUISITOS

- Python **3.x** instalado  
- Nenhuma biblioteca adicional é necessária  

-----

##    ▶️ COMO EXECUTAR O PROJETO

### 1) CLONAR O REPOSITORIO

#```bash
git clone https://github.com/AgathaAlmeida7/estatistica-tabelas-de-frequencia-python.git

## COMO ACESSAR A PASTA DO PROJETO

CD estatistica-tabelas-de-frequencia-python

## COMO EXECUTAR O PROGRAMA

python main.py

## EXEMPLOS  DO RESULTADO DE USO DO PROGRAMA

AO RODAR O PROGRAMA, O  USUARIO ELE DIGITA:

- A QUANTIDADE DE VALORES;
- OS VALORES NUMERICOS;
- O NUMERO DE CLASSES DA TABELA;

O PROGRAMA ELE VAI PROCESSAR OS DADOS E EXIBIR ELES NO TERMINAL COM UMA TABELA SEMELHENTE A :

Classe             Intervalo     fi     fr (%)     Fac
1 ─────────►       10 |-- 20      4      13.3       4
2 ─────────►       20 |-- 30      7      23.3      11
3 ─────────►       30 |-- 40      9      30.0      20
...

OBS: ESTE É APENAS UM EXEPLO VISUAL. OS VALORES REAIS SAO CALCULADOS DINAMICAMENTE.

## OBS SOBRE CONTRIBUIÇÕES: 

## voce pode:

- abrir uma issue;
- criar um pull request;
- sugerir melhorias;

## LICENÇA

Este projeto está sob a licença MIT. 
Sinta-se livre para usar e estudar.





























