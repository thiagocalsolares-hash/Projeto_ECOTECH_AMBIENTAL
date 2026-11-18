
import pandas as pd
import json

def calcular_kpis(arquivo="dados.csv"):
    df = pd.read_csv(arquivo)

    faturamento = df["vendas"].sum()
    quantidade = df["quantidade_vendas"].sum()
    ticket_medio = faturamento / quantidade

    satisfacao = (
        df["clientes_satisfeitos"].sum()
        / df["total_clientes"].sum()
    ) * 100

    df["variacao_mensal"] = df["vendas"].pct_change() * 100

    resumo = {
        "faturamento_total": float(faturamento),
        "quantidade_vendas": int(quantidade),
        "ticket_medio": float(ticket_medio),
        "taxa_satisfacao": float(satisfacao)
    }

    pd.DataFrame([resumo]).to_csv(
        "resultados_kpis.csv", index=False
    )

    with open("resumo_kpis.json", "w", encoding="utf-8") as f:
        json.dump(resumo, f, indent=4, ensure_ascii=False)

    return df, resumo
