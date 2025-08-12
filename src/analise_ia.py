import pandas as pd


def classificar_valor(df: pd.DataFrame) -> pd.DataFrame:
    """Classify books as high or low value based on median price."""
    mediana = df["preco"].median()
    print(f"Classificando livros com base na mediana de preço {mediana:.2f}...")
    df["categoria_valor"] = df["preco"].apply(
        lambda x: "Alto Valor" if x > mediana else "Baixo Valor"
    )
    print("Classificação concluída.")
    return df


def resumo_estatistico(df: pd.DataFrame) -> dict:
    print("Gerando resumo estatístico...")
    return {
        "total_livros": len(df),
        "preco_medio": df["preco"].mean(),
        "preco_maximo": df["preco"].max(),
        "preco_minimo": df["preco"].min(),
        "mediana": df["preco"].median(),
        "distribuicao_valor": df["categoria_valor"].value_counts().to_dict(),
    }
