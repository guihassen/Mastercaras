#!/usr/bin/env python3
"""
Gera o relatório em PDF a partir de relatorio.html.

Uso:
    python gerar_pdf.py                 # gera relatorio/relatorio.pdf
    python gerar_pdf.py meu_nome.pdf    # nome de saída customizado

Dois motores são suportados, nesta ordem de preferência:
  1. Playwright  (renderização fiel ao Chrome — recomendado)
       pip install playwright && playwright install chromium
  2. WeasyPrint  (alternativa em Python puro)
       pip install weasyprint        (macOS também precisa de: brew install pango)

O script detecta automaticamente o que estiver instalado.
"""
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
HTML = AQUI / "relatorio.html"


def saida() -> Path:
    nome = sys.argv[1] if len(sys.argv) > 1 else "relatorio.pdf"
    return (AQUI / nome).resolve()


def via_playwright(html: Path, pdf: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    print("→ Motor: Playwright (Chromium)")
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page()
        # file:// garante que as imagens em ../notebooks/graficos resolvam
        pagina.goto(html.as_uri(), wait_until="networkidle")
        pagina.pdf(
            path=str(pdf),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
        )
        navegador.close()
    return True


def via_weasyprint(html: Path, pdf: Path) -> bool:
    try:
        from weasyprint import HTML as WHTML
    except (ImportError, OSError):
        return False
    print("→ Motor: WeasyPrint")
    WHTML(filename=str(html)).write_pdf(str(pdf))
    return True


def main() -> int:
    if not HTML.exists():
        print(f"ERRO: não encontrei {HTML}")
        return 1

    pdf = saida()
    for motor in (via_playwright, via_weasyprint):
        try:
            if motor(HTML, pdf):
                print(f"✓ PDF gerado: {pdf}")
                return 0
        except Exception as e:  # noqa: BLE001
            print(f"  (falhou em {motor.__name__}: {e})")

    print(
        "\nNenhum motor de PDF disponível. Instale um deles:\n"
        "  pip install playwright && playwright install chromium   (recomendado)\n"
        "  pip install weasyprint                                  (alternativa)"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
