#aqui é o meu ponto de entrada para o projeto 

from utils import ler_lista_numeros
from tabela_frequencia import preparar_dados
from tabela import gerar_tabela_frequencia
from tabela_frequencia import preparar_dados,ler_numero_classes
import math



# o que isso aqui significa?
#R->'VA ATE O ARQUIVO UTILS.PY E TRAGA PARA CA A FUNCAO LER_LISTA_NUMEROS
#AQUI EU TOU DIZENDO QUE EU SOU TOU PEGANDO A FUNCAO LER_LISTA_NUMEROS DO ARQUIVO UTILS
#EU QUERO USAR ESSA FERRAMENTA QUE ESTA GUARDADA NAQUELE ARQUIVO




def main():
    #FUNCAO PRINCIPAL DO PROGRAMA
    #EM PROJETOS PROFISSIONAIS SEMPRE EXISTE UMA FUNCAO CHAMADA MAIN()
    #SERVE COMO UM PONTO DE PARTIDA ORGANIZADO


    valores = ler_lista_numeros()
    #TA CHAMANDO A FUNCAO QUE VEIO LA DO UTILS.PY
    #ESSA FUNCAO ELA JA FOI ESTRUTURADA PARA O QUE ELA DEVE FAZER

    #PERGUNTA VALORES AO USUARIO//VALIDA//CORRIGE//CONVERTE//RETORNA UMA LISTA DE NUMEROS
    #O RESULTADO DE TUDO QUE ESSA FUNCAO FAZ, ELA FICA DENTRO DA VARAIVEL VALORES

    # UTILS.PY->EXECUTA A FUNCAO
    #MAIN.PY->RECEBE O RESULTADO
    print("Valores digitados:", valores)
    #SIMPLESMENTE, EXIBE O QUE A FUNCAO RETORNOU 
#if __name__ == "__main__":
    #main()#SE O ARQUIVO TA SENDO EXECUTADO DIRETAMENTO(O CASO AO RODAR PYTHON MAIN.PY), ENTAO CHAMA A FUNCAO PRINCIPAL

    

#PARTE MAIS IMPORTANTE PROFISSIONALMENTE 
#ELA VERIFICA SE ESSE ARQUIVO ESTA SENDO EXECUTADO DIRETAMENTE
#SE SIM, RODA A FUNCAO MAIN()
#SE NAO , NAO RODA

#TESTANDO A FUNCAO RESPONSAVEL DO BLOCO 02
#PROCESSANDO ESTATISTICAMENTE

#NAO PRECISA APAGAR A FUNCAO ANTERIOR,SO IREMOS SUBSTITUIR ELA NA CHAMADA NO MOMENTO DO TESTE
#PQ NAO APAGAR?
#O CODIGO DA ETAPA 01 CONTINUA UTIL PARA TESTAR PARTES ESPECIFICAS
#É NORMAL UM PROJETO TER VARIAS FUNCOES DE TESTE DURANTE O DESENVOLVIMENTO
#VOCE SO VAI ESCOLHER QUAL ETAPA QUER TESTAR NO MOMENTO, CHAMANDO A FUNCAO CERTA NO MAIN()

def main_etapa02():
    # Função principal da etapa 02

    valores = ler_lista_numeros()

    # AQUI é onde você realmente chama o bloco 02
    valores_ordenados, v_min, v_max, amplitude = preparar_dados(valores)

    print('\n---- RESULTADOS DO BLOCO 02 ----')
    print('Valores Ordenados:', valores_ordenados)
    print('Valor Mínimo:', v_min)
    print('Valor Máximo:', v_max)
    print('Amplitude:', amplitude)
    print('-------------------------------')

#CHAMANDO A ETAPA 02 PARA TESTAR

#if __name__ == "__main__":
    #main_etapa02()

#ETAPA BLOCO 03

#CRIANDO UMA NOVA FUNCAO CHAMADA MAIN_ETAPA03()


#VAI LER OS VALORES
#LER O NUMERO DE CLASSES
#GERAR INTERVALOS(USANDO SUA PROPRIA FUNCAO OU IMPORTACAO)
#CHAMAR GERAR_TABELA_FREQUENCIA()
#EXIBIR A TABELA


def main_etapa03():
    print("---- BLOCO 03: TABELA DE FREQUÊNCIAS ----")

    # 1. Ler valores
    valores = ler_lista_numeros()

    # 2. Ler número de classes (k)
    k = ler_numero_classes()

    # 3. Preparar dados do bloco 02
    valores_ordenados, v_min, v_max, amplitude = preparar_dados(valores)

    # 4. Calcular tamanho da classe (h)
    h_raw = amplitude / k
    h = math.ceil(h_raw)

    # 5. Gerar intervalos e pontos médios
    limites_inferiores = []
    limites_superiores = []
    pontos_medios = []

    inicio = v_min
    for i in range(k):
        fim = inicio + h
        limites_inferiores.append(inicio)
        limites_superiores.append(fim)
        pontos_medios.append((inicio + fim) / 2)
        inicio = fim

    # 6. Chamar a tabela (BLOCO 03)
    gerar_tabela_frequencia(
        valores_ordenados,
        limites_inferiores,
        limites_superiores,
        pontos_medios,
        k
    )

if __name__=="__main__":
    main_etapa03()

























