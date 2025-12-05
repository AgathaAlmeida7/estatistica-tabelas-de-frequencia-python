# tabela.py
def gerar_tabela_frequencia(valores_ordenados, limites_inferiores, limites_superiores, pontos_medios, numero_classes):
    """
    Gera e imprime a tabela de frequência completa no formato do professor,
    com intervalos exibidos como: 10 ┤ 13
    Regras:
      - para intervalos intermediários: li <= x < ls
      - para último intervalo: li <= x <= ls
    Entradas:
      - valores_ordenados: lista de floats (pode estar ordenada)
      - limites_inferiores: lista de floats (len = k)
      - limites_superiores: lista de floats (len = k)
      - pontos_medios: lista de floats (len = k)
      - numero_classes: int (k)
    """

    # segurança: converter listas
    valores = [float(v) for v in valores_ordenados]
    lim_inf = [float(x) for x in limites_inferiores]
    lim_sup = [float(x) for x in limites_superiores]
    pm = [float(x) for x in pontos_medios]
    k = int(numero_classes)

    # 1) Frequência absoluta (fi)
    fi = [0] * k
    for x in valores:
        placed = False
        for i in range(k):
            li = lim_inf[i]
            ls = lim_sup[i]
            if i < k - 1:
                if li <= x < ls:
                    fi[i] += 1
                    placed = True
                    break
            else:
                # último intervalo: incluir ls
                if li <= x <= ls:
                    fi[i] += 1
                    placed = True
                    break
        if not placed:
            fi[-1] += 1  # segurança

    # 2) Frequência acumulada (Fac)
    Fac = []
    acc = 0
    for f in fi:
        acc += f
        Fac.append(acc)

    # 3) Frequência relativa (%)
    n = len(valores)
    if n == 0:
        raise ValueError("Lista de valores está vazia.")

    fr = [(f / n) * 100 for f in fi]

    # 4) Frequência relativa acumulada (Frac%)
    Frac = []
    accp = 0.0
    for p in fr:
        accp += p
        Frac.append(accp)

    # 5) IMPRIMIR TABELA (NOVA VERSÃO CORRIGIDA)
    print("\n" + "─" * 80)
    print("CLASSE(k) | INTERVALO          | F.ABS | F.REL(%) | F.ACUM | F.REL ACUM(%)")
    print("─" * 80)

    for i in range(k):
        classe = i + 1
        li = lim_inf[i]
        ls = lim_sup[i]

        intervalo = f"{li:.2f} ┤ {ls:.2f}"

        fi_val = fi[i]
        fr_val = fr[i]
        fac_val = Fac[i]
        frac_val = Frac[i]

        print(
            f"{classe:^9} | "
            f"{intervalo:<18} | "
            f"{fi_val:^5} | "
            f"{fr_val:>7.2f}% | "
            f"{fac_val:^6} | "
            f"{frac_val:>12.2f}%"
        )

    print("─" * 80)
    print(
        f"{'TOTAL':^9} | "
        f"{'':18} | "
        f"{sum(fi):^5} | "
        f"{'100.00%':>7} | "
        f"{'':6} | "
        f"{'100.00%':>12}"
    )
    print("─" * 80)