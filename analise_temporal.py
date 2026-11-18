
def analisar_periodos(df):
    primeiro_semestre = df.iloc[:6]["vendas"].sum()
    segundo_semestre = df.iloc[6:]["vendas"].sum()

    variacao = (
        (segundo_semestre - primeiro_semestre)
        / primeiro_semestre
    ) * 100 if primeiro_semestre else 0

    resultado = {
        "primeiro_semestre": float(primeiro_semestre),
        "segundo_semestre": float(segundo_semestre),
        "variacao_percentual": float(variacao)
    }

    return resultado
