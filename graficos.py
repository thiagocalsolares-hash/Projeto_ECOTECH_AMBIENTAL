
import matplotlib.pyplot as plt

def gerar_graficos(df):

    # Gráfico de linha: evolução mensal das vendas
    plt.figure(figsize=(10, 5))
    plt.plot(df["mes"], df["vendas"], marker="o")
    plt.title("Evolução Mensal das Vendas")
    plt.xlabel("Meses")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_linha_vendas.png", dpi=300)
    plt.show()
    plt.close()

    # Gráfico de barras: ticket médio mensal
    ticket_medio = df["vendas"] / df["quantidade_vendas"]

    plt.figure(figsize=(10, 5))
    plt.bar(df["mes"], ticket_medio)
    plt.title("Ticket Médio Mensal")
    plt.xlabel("Meses")
    plt.ylabel("Ticket Médio (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_barras_ticket_medio.png", dpi=300)
    plt.show()
    plt.close()

    # Gráfico de pizza: participação por semestre
    primeiro_semestre = df.iloc[:6]["vendas"].sum()
    segundo_semestre = df.iloc[6:]["vendas"].sum()

    plt.figure(figsize=(7, 7))
    plt.pie(
        [primeiro_semestre, segundo_semestre],
        labels=["Primeiro semestre", "Segundo semestre"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Participação das Vendas por Semestre")
    plt.tight_layout()
    plt.savefig("grafico_pizza_semestres.png", dpi=300)
    plt.show()
    plt.close()
