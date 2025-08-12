import pandas as pd


def processar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for data cleaning/processing."""
    print("Processando dados...")
    # Aqui poderia haver etapas de limpeza e transformação
    print("Processamento concluído.")
    return df


def salvar_csv(df: pd.DataFrame, caminho: str) -> None:
    print(f"Salvando dados em {caminho}...")
    df.to_csv(caminho, index=False)
    print("Arquivo CSV salvo.")
