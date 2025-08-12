import pandas as pd


def processar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for data cleaning/processing."""
    return df


def salvar_csv(df: pd.DataFrame, caminho: str) -> None:
    df.to_csv(caminho, index=False)
