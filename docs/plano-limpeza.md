# Plano de Limpeza das Bases — Priceless Bank
**Mastercard Challenge 2026 | Base: `docs/analise-exploratoria.md` + `notebooks/main.ipynb`**

---

## Princípios

1. **Nunca sobrescrever o raw.** Os 5 CSVs em `data/` ficam intactos. A limpeza gera bases tratadas (ex.: `data/clean/*.parquet` ou DataFrames `*_clean` no notebook).
2. **Flag em vez de exclusão sempre que possível.** Excluir só quando o registro é operacionalmente impossível ou inútil. Para o resto, criar coluna-flag e decidir filtro por análise.
3. **Distinguir "anomalia" de "comportamento esperado".** Nulos por design (Crossborder, Contactless, Wallet, Qtd_Parcelas, vencimento da Reservinha) **não são erros** — não tratar como sujeira.
4. **Rastreabilidade.** Cada exclusão registrada em um log de limpeza (qtd antes/depois + motivo), para defender as decisões na apresentação.
5. **Ordem:** tratar tipos → tratar chaves/integridade → tratar valores → derivar colunas → validar.

---

## Ordem de execução recomendada

```
1. Carregar raw + corrigir dtypes (datas, inteiros, categóricos)
2. Validar chaves (PK únicas) e integridade referencial (FKs)
3. Tratar anomalias por base (flag/exclusão)
4. Derivar colunas de apoio (Idade, Faixa, YQ, is_estorno, etc.)
5. Persistir bases limpas + log de limpeza
6. Validar resultado (asserts de sanidade)
```

---

## Base CLIENTES (1.960 × 8) — PK: `Cliente_ID`

| # | Item | Ação | Justificativa |
|---|------|------|---------------|
| C1 | `Renda_Anual` — 255 nulos (13%) | **Manter nulo + criar flag `Renda_Informada` (bool).** Para modelos que exigem valor, imputar mediana (R$85k) em coluna separada `Renda_Anual_Imp`. **Não** imputar na coluna original. | Dado declaratório; a ausência pode ser informativa (cliente menos engajado). Imputar direto destrói o sinal. |
| C2 | `Data_Nascimento` → `Idade` / `Faixa_Etaria` | Derivar com data de referência fixa (`2026-06-13`). Validar Idade ∈ [18, 76]. | Já feito no notebook; padronizar a data de referência em uma constante única. |
| C3 | `Possui_Conta_Adicional` | Normalizar para booleano (`Sim`/`Não` → `True`/`False`). | Facilita cruzamentos. |
| C4 | PK `Cliente_ID` | Assert de unicidade (esperado: 0 duplicatas). | Garantia de integridade da tabela mestre. |

---

## Base CARTÕES (4.006 × 7) — PK: `ID_Cartao`

| # | Item | Ação | Justificativa |
|---|------|------|---------------|
| K1 | 450 cartões com `Data_Ativacao < Data_Emissao` (11,2%) | **Flag `data_invalida` + excluir de qualquer análise temporal** (lead time de ativação, coortes). Manter para análises de portfólio (produto, limite). | Fisicamente impossível; erro de geração. São exatamente os mesmos 450 com `Data_Validade` nula. |
| K2 | `Data_Validade` — 450 nulos | Mesma flag K1 (são os mesmos registros). Não imputar. | Correlação 1:1 com o erro de ativação. |
| K3 | Cartões vencidos (1.017, validade < hoje) | **Flag `cartao_vencido`** — NÃO excluir. | Não é erro: pode indicar churn/não-renovação, é sinal analítico. |
| K4 | 469 cartões sem nenhuma transação (11,7%) | **Flag `cartao_inativo`** (derivada via anti-join com Transações). Não excluir. | Preditor de churn/baixo engajamento — é achado, não sujeira. |
| K5 | `Limite_Cartao` = 0 em débito | Manter. Garantir que análises de limite filtrem `Tipo_Cartao == 'Crédito'`. | Esperado: débito não tem limite de crédito. |
| K6 | Datas como string | Converter `Data_Emissao`/`Data_Ativacao` (datetime) e `Data_Validade` (`errors='coerce'`). | Já no notebook; consolidar no passo de dtypes. |

---

## Base TRANSAÇÕES (156.826 × 13) — PK: `ID_Transacao` ⭐ base mais crítica

| # | Item | Ação | Justificativa |
|---|------|------|---------------|
| T1 | 165 valores `Valor_Compra` ≤ 0 (estornos) | **Criar flag `is_estorno` (Valor_Compra < 0).** Excluir de somas de volume/ticket; manter em contagem de eventos se necessário. | Estorno é evento real, mas distorce volume/ticket. Flag preserva a opção. |
| T2 | Outliers (84 acima de R$10k, 7 acima de R$50k; máx R$107.777) | **Não excluir. Flag `outlier_valor`** (ex.: > P99.5 ou > R$10k). Reportar métricas com mediana além da média. | Podem ser legítimos (educação, equipamentos). Mediana já é robusta. |
| T3 | `Crossborder` — 95,6% nulo | **Não tratar como nulo a corrigir.** Nas análises de crossborder, filtrar `notna()`. Opcional: criar `Crossborder_aplicavel`. | Por design: só preenchido em CNP online. |
| T4 | `Contactless` — 82,5% nulo | Idem T3 (filtrar `notna()` quando for o foco). | Por design: só em transações físicas. |
| T5 | `Wallet` — 85,9% nulo | Preencher como categoria `'Nenhuma'` para contagens; manter nulo onde for medir penetração de wallet. | Null = cliente não usou carteira digital — é informação. |
| T6 | `Qtd_Parcelas` — 72% nulo | **Null = à vista.** Criar `is_parcelado` e `Qtd_Parcelas_norm` (null→1). Não excluir. | Comportamento correto, não erro. |
| T7 | Anomalia de ticket 2024 (~2,5× maior) | **Não alterar dados.** Documentar e usar **intercâmbio normalizado** (qtd × ticket-base × taxa) em comparações intertemporais, como já feito na seção 9.2. | Artefato de geração sintética; corrigir o valor seria inventar dado. Tratar na camada de análise, não na de limpeza. |
| T8 | Integridade referencial | Validar `Cliente_ID` ⊂ Clientes e `ID_Cartao` ⊂ Cartões. Registrar órfãos (se houver) com flag. | Garante que joins não dropem linhas silenciosamente. |
| T9 | `Data` | Converter para datetime; derivar `YQ` (período trimestral). | Eixo de toda análise temporal. |

---

## Base PIX (278.940 × 8) — sem PK formal ⭐ 2ª mais crítica

| # | Item | Ação | Justificativa |
|---|------|------|---------------|
| P1 | 917 valores negativos (0,3%) | **Flag `valor_invalido` + excluir** de análises de volume. Isolar para investigação de risco. | PIX negativo não tem sentido operacional. |
| P2 | 591 valores zero (0,2%) | **Excluir** (mesma flag `valor_invalido`). | PIX de R$0 é operação vazia. |
| P3 | 418 registros com `Data` **e** `Tipo_transacao` nulos | **Excluir da análise temporal.** Registrar no log. | Registros incompletos — não dá para alocar no tempo nem classificar envio/recebimento. |
| P4 | 24.644 envios não aprovados (~10%) | **Manter + flag `nao_aprovado`.** Separar `Aprovado==1` para volume efetivo; manter base total para medir taxa de fricção/reprovação. | A reprovação é um achado (fricção/fraude), não sujeira. |
| P5 | 3.392 recebimentos negados (10,3%) | Manter com flag (P4). Marcar para investigação de regra de negócio. | Comportamento incomum, vale como insight. |
| P6 | Tipo de destinatário `PF_PJ` | Normalizar categoria; garante o cálculo de PIX→PJ (canibalização do cartão). | Variável central do diagnóstico. |
| P7 | Ausência de PIX 2025Q1/Q2 | **Documentar como gap conhecido.** Não imputar. Análises de 2025 devem anotar a lacuna. | Dado simplesmente não existe no dataset. |
| P8 | Duplicatas de linha inteira | Verificar e, se existirem, remover exatas. Sem PK, dedup por todas as colunas. | Evita dupla contagem de volume. |

> **Volume "limpo" de PIX para análises** = `Valor > 0` **e** `Data.notna()` **e** (`Aprovado==1` quando o foco for volume efetivo).

---

## Base INVESTIMENTOS (21.200 × 7) — sem PK formal

| # | Item | Ação | Justificativa |
|---|------|------|---------------|
| I1 | `Data` e `Data_Abertura_Conta_Inv` em formato `YYYYMM` (int) | **Converter para datetime** (`pd.to_datetime(col, format='%Y%m')`). Coluna nova, preservar a original se útil. | Formato diverge das outras bases; impede análise temporal sem conversão. |
| I2 | `Data_de_vencimento == 299901` (7.864 = toda a Reservinha) | **Não converter como data.** Tratar como sentinela "sem vencimento" → `NaT` + flag `sem_vencimento`. | Reservinha é liquidez diária sem vencimento — esperado. Converter `299901` quebra. |
| I3 | `Valor_Aplicado < 0` (1.566 = resgates) | **Não corrigir.** Criar `Tipo_Operacao` (`Aporte` se >0, `Resgate` se <0). Separar nas somas. | Resgate é comportamento normal de carteira. |
| I4 | `Saldo_Atual == 0` (2.551) | Manter; flag `produto_encerrado`. | Produto vencido/resgatado — esperado. |
| I5 | 14 nulos em `Valor_Aplicado`/`Saldo_Atual` | Investigar as 14 linhas; provavelmente excluir (registro incompleto). | Volume pequeno; decisão registrada no log. |
| I6 | Integridade referencial | Validar `Cliente_ID` ⊂ Clientes. | Base de retenção; joins consistentes. |

---

## Erro já corrigido (manter atenção)

- **`base_investimentos` carregava `Base_clientes.csv`** no notebook original — já corrigido na célula 2. Manter o comentário/assert garantindo que `Produto_Investimento` existe após o load, para não regredir.

---

## Entregáveis da limpeza

1. **`notebooks/02_limpeza.ipynb`** (ou seção no `main.ipynb`): pipeline reproduzível raw → limpo.
2. **Bases tratadas** em `data/clean/` (parquet preserva dtypes e é mais rápido).
3. **Log de limpeza** (`docs/log-limpeza.md` ou DataFrame impresso): base, regra, qtd removida/flagada, motivo.
4. **Asserts de validação final**, ex.:
   - PKs únicas (Clientes, Cartões, Transações)
   - Sem `Valor` ≤ 0 nas bases de volume "limpo"
   - Todas as FKs resolvem
   - Datas dentro do período Jan/2023–Dez/2025

---

## Resumo de decisões (excluir × flag)

| Tratamento | Casos |
|------------|-------|
| **Excluir** (impossível/vazio) | PIX valor ≤ 0 (1.508), PIX data+tipo nulos (418), INV 14 nulos, duplicatas exatas |
| **Flag e manter** | Cartões data inválida (450), inativos (469), vencidos (1.017); Trans estorno (165), outliers (84); PIX não aprovado (~28k) |
| **Derivar/normalizar** | Idade/Faixa, YQ, is_parcelado, Tipo_Operacao (inv), datas YYYYMM, booleanos |
| **Não mexer (design)** | Crossborder, Contactless, Wallet, Qtd_Parcelas, vencimento Reservinha, Valor_Aplicado negativo |
| **Tratar na análise, não na limpeza** | Anomalia de ticket 2024 (normalização), gap PIX 2025 Q1/Q2 |

---

*Plano gerado em 13/06/2026 · base para a etapa de limpeza antes do aprofundamento analítico.*
