#funções responsaveis pela logica estatistica

#O BLOCO 02 VAI SER AQUI

#A PARTIR DAQUI JA ESTAMOS LIDANDO COM ESTATISTICA


def preparar_dados(valores):
    #pq valores que recebeu aquela funcao veio como parametro para essa funcao de preparar dados?
    #ESTOU ORDENANDO OS VALORES QUE ESSA FUNCAO PREPARAR DADOS ACABOU DE RECEBER

    valores_ordenados=sorted(valores)
    #2)EXTREMOS

    v_min=min(valores_ordenados)
    v_max=max(valores_ordenados)
    #EU PEGUEI OS VALORES DA LISTA,E BOTEI EM ORDEM CRESCENTE 
    #COM BASE NISSO AGORA EU POSSO DENTRO DESSA LISTA PEGAR QUAL É O MENOR VALOR E O MAIOR VALOR, E NISSO UTILIZANDO A FUNCAO MIN() E MAX()

    #AGORA EU VOU CALCULAR A AMPLITUDE

    #3)CALCULANDO AMPLITUDE TOTAL

    amplitude = (v_max-v_min)

    return valores_ordenados,v_min,v_max,amplitude


#EXPLICANDO CADA PASSO A PASSO FEITO AQUI 

#TABELAS DE FREQUENCIA TRABALHAM COM INTERVALOS CRESCENTES

#A GENTE PEGA O MIN E O MAX , POIS ELES VAO LIMITAR AS CLASSES

#O RESULTADO DA AMPLITUDE DIZ O QUAO ESPALHADO OS DADOS ESTAO. E SEM ISSO NAO TEM COMO ENXERGAR :


#DESCOBRIR QUANTAS CLASSES PRECISA 
#DESCOBRIR O TAMANHO DAS CLASSES
#MONTAR A TABELA


#SABER A AMPLITUDE É UM DOS PRIMEIROS PASSOS EM QUALQUER ANALISE DESCRITIVA

#DPS DE TUDO ISSO, O TESTE SERA FEITO NA FUNCAO MAIN()

#BLOCO 02-PROCESSANDO ESTATISTICAMENTE

def ler_numero_classes():
    while True:
        try:
            n=int(input('digite o numero de classes:\n'))
            if n<=0:
                print('o numero de classes deve ser maior que zero:\n')
                continue
            return n
        except ValueError:
            print('Digite apenas numeros inteiros:\n')

#o que essa funcao esta fazendo:
#1-pergunta o numero de classes
#try/except:
#garante que:nao tenha letras,nao tenha ponto,nao tenha coisa invalida
#3-so aceita numeros positivos=
#pq classe=intervalo, e intervalo nunca pode ser zero ou negativo

#4-retorna um numero total seguro
#so sai do loop quando o numero é certo
#essa funcao, sera testada no arquivo main.py

