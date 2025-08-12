import pandas as pd


def classificar_valor(df: pd.DataFrame) -> pd.DataFrame:
    """Classify books as high or low value based on median price."""
    mediana = df["preco"].median()
    df["categoria_valor"] = df["preco"].apply(lambda x: "Alto Valor" if x > mediana else "Baixo Valor")
    return df


def resumo_estatistico(df: pd.DataFrame) -> dict:
    return {
        "total_livros": len(df),
        "preco_medio": df["preco"].mean(),
        "preco_maximo": df["preco"].max(),
        "preco_minimo": df["preco"].min(),
        "mediana": df["preco"].median(),
        "distribuicao_valor": df["categoria_valor"].value_counts().to_dict(),
    }
