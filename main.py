
from kpis import calcular_kpis
from analise_temporal import analisar_periodos
from estruturas import PilhaHistorico, FilaIndicadores, ArvoreBinaria
from graficos import gerar_graficos


def main():

    # Cálculo dos indicadores
    df, resumo = calcular_kpis("dados.csv")

    # Análise temporal
    analise = analisar_periodos(df)

    # Organização com pilha e fila
    pilha = PilhaHistorico()
    fila = FilaIndicadores()

    for nome, valor in resumo.items():
        pilha.empilhar(nome)
        fila.adicionar(nome)

    # Organização das vendas em árvore binária
    arvore = ArvoreBinaria()

    for valor in df["vendas"]:
        arvore.inserir(float(valor))

    # Geração dos gráficos
    gerar_graficos(df)

    # Exibição dos resultados
    print("\n===== INDICADORES DE DESEMPENHO =====")
    for nome, valor in resumo.items():
        print(f"{nome}: {valor}")

    print("\n===== ANÁLISE TEMPORAL =====")
    for nome, valor in analise.items():
        print(f"{nome}: {valor:.2f}")

    print("\n===== ÁRVORE BINÁRIA =====")
    print("Vendas em ordem:", arvore.em_ordem())

    print("\nProjeto executado com sucesso!")


if __name__ == "__main__":
    main()
