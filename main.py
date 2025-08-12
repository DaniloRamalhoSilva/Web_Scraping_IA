from pathlib import Path

from src.coleta_dados import scrape_books
from src.processamento import processar_dados, salvar_csv
from src.analise_ia import classificar_valor, resumo_estatistico
from src.relatorio import gerar_relatorio


def main() -> None:
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

    print("Coleta e análise concluídas.")
    print(f"Dados salvos em: {csv_path}")
    print(f"Relatório gerado em: {relatorio_path}")


if __name__ == "__main__":
    main()
