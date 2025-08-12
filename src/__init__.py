from pathlib import Path

from .coleta_dados import scrape_books
from .processamento import processar_dados, salvar_csv
from .analise_ia import classificar_valor, resumo_estatistico
from .relatorio import gerar_relatorio

__all__ = [
    "scrape_books",
    "processar_dados",
    "salvar_csv",
    "classificar_valor",
    "resumo_estatistico",
    "gerar_relatorio",
    "executar_pipeline",
]


def executar_pipeline() -> dict:
    """Executa o fluxo completo de scraping, processamento e geração de relatório.

    Returns
    -------
    dict
        Caminhos dos arquivos gerados: CSV dos dados e PDF do relatório.
    """
    df = scrape_books()
    df = processar_dados(df)
    df = classificar_valor(df)

    dados_dir = Path("dados")
    dados_dir.mkdir(exist_ok=True)
    csv_path = dados_dir / "livros.csv"
    salvar_csv(df, str(csv_path))

    resumo = resumo_estatistico(df)

    relatorios_dir = Path("relatorios")
    relatorios_dir.mkdir(exist_ok=True)
    relatorio_path = relatorios_dir / "relatorio_final.pdf"
    gerar_relatorio(df, resumo, str(relatorio_path))

    return {"dados": str(csv_path), "relatorio": str(relatorio_path)}
