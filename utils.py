#arquivo que guarda funcoes auxiliares, como ler dados do usuario


#ENTRANDO COM DADOS

#GARANTIR QUE O USUARIO DIGITE SOMENTE:

#NUMEROS
#SEPARADOS POR VIRGULAS
#SEM ESPAÇOS DESNECESSARIOS
#SEM LETRAS
#SEM SIMBOLOS INVALIDOS
#SEM LISTA VAZIA
#SEM VIRGULA SOBRANDO
#SEM ERRO DE DIGITAÇÃO 
#SEM TRAVAR O PROGRAMA


def ler_lista_numeros():
    """
    Lê uma entrada do usuário contendo números separados por vírgula.
    Garante:
        - Não estar vazia
        - Apenas números (int ou float)
        - Sem vírgulas sobrando
        - Sem letras
        - Sem símbolos inesperados
    Retorna uma lista de floats.
    """

    while True:
        entrada = input("Digite os valores separados por vírgula: ").strip()

        # 1) Verifica se está vazia
        if not entrada:
            print("❌ Erro: você não digitou nada. Tente novamente.")
            continue

        # 2) Divide pelos separadores
        partes = entrada.split(",")

        numeros = []
        try:
            for p in partes:
                p = p.strip()
                if p == "":
                    raise ValueError("Vírgula sobrando ou sem número entre vírgulas.")
                
                # Aceita inteiros e floats
                numero = float(p)
                numeros.append(numero)

            return numeros  # Sucesso!

        except ValueError as e :
            print(f"❌ Erro:{e} ")
            print("Use o formato:10,20,35,7.5")
            continue
#alternado o except valuerror do arquivo utils.py 
#add nos 2 print essa substituicao ....





























