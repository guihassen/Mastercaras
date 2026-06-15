# Relatório final — Priceless Bank

Relatório executivo do desafio (diagnóstico + Priceless Pay + plano de ação), pronto para virar PDF.

## Arquivos
- `relatorio.html` — o relatório (template auto-contido; CSS embutido, otimizado para impressão A4).
- `gerar_pdf.py` — converte o HTML em PDF.
- `relatorio.pdf` — saída gerada.

Os gráficos vêm de `../notebooks/graficos/*.png` (referência relativa). O conteúdo segue
`docs/analise-exploratoria.md`, `docs/proposta-solucao.md` e `docs/plano-de-acao.md`.

## Gerar o PDF
```bash
# na raiz do projeto, com o venv ativo
python relatorio/gerar_pdf.py                 # -> relatorio/relatorio.pdf
python relatorio/gerar_pdf.py relatorio_v2.pdf
```

### Motor de PDF (o script detecta automaticamente)
```bash
pip install playwright && playwright install chromium   # recomendado (fiel ao Chrome)
# ou
pip install weasyprint                                   # alternativa (macOS: brew install pango)
```

## Editar
Mexa no conteúdo/estilo direto no `relatorio.html` (HTML + CSS num único arquivo) e rode o
`gerar_pdf.py` de novo. Para trocar/atualizar um gráfico, regenere o PNG no notebook
correspondente, o relatório aponta para o mesmo caminho.
