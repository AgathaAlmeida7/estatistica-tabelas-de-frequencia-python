#arquivo que serve so para testar funcoes isoladamente enquanto se aprende
# testes.py — verificação rápida do que existe para o BLOCO 03
from utils import ler_lista_numeros
from tabela_frequencia import preparar_dados, ler_numero_classes  # usar o que já tem

import math

def gerar_intervalos_simples(valores, k):
    # usa preparar_dados para obter extremos
    ordenados, v_min, v_max, amplitude = preparar_dados(valores)

    # tamanho da classe (arredondar para cima seguindo o padrão do professor)
    h_raw = amplitude / k
    h = math.ceil(h_raw)

    lim_inf = []
    lim_sup = []
    pontos_medios = []

    inicio = v_min
    for i in range(k):
        fim = inicio + h
        lim_inf.append(inicio)
        lim_sup.append(fim)
        pontos_medios.append((inicio + fim) / 2)
        inicio = fim

    return lim_inf, lim_sup, pontos_medios, h, amplitude

def main():
    print("Teste BLOCO 03 — verificação de dados necessários")
    valores = ler_lista_numeros()
    k = ler_numero_classes()
    lim_inf, lim_sup, pm, h, amplitude = gerar_intervalos_simples(valores, k)

    print("\nAmplitude total:", amplitude)
    print("Tamanho da classe (h):", h)
    print("\nLimites inferiores:", lim_inf)
    print("Limites superiores:", lim_sup)
    print("Pontos médios:", pm)

if __name__ == "__main__":
    main()
