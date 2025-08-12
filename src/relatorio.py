from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd


def gerar_relatorio(df: pd.DataFrame, resumo: dict, caminho_pdf: str) -> None:
    """Generate a simple PDF report with summary information."""
    with PdfPages(caminho_pdf) as pdf:
        fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 size
        ax.axis("off")
        lines = [
            "Relatório de Livros",
            "", 
            f"Total de livros: {resumo['total_livros']}",
            f"Preço médio: {resumo['preco_medio']:.2f}",
            f"Preço máximo: {resumo['preco_maximo']:.2f}",
            f"Preço mínimo: {resumo['preco_minimo']:.2f}",
            f"Mediana: {resumo['mediana']:.2f}",
            "",
            "Distribuição de Categorias:",
        ]
        for categoria, qtd in resumo["distribuicao_valor"].items():
            lines.append(f"- {categoria}: {qtd}")
        ax.text(0.1, 0.9, "\n".join(lines), va="top", fontsize=12)
        pdf.savefig(fig)
        plt.close(fig)
