# Análise Exploratória de Dados — Priceless Bank
**Mastercard Challenge 2026 | Data: 12/06/2026**

---

## Contexto do Problema

O Priceless Bank está enfrentando queda significativa de participação de mercado nos últimos trimestres de 2025, passando de **33% para 19% de market share** (em valor transacionado) ao longo de apenas quatro trimestres. Os concorrentes que mais avançaram foram **LuminaPay** (17% → 30%) e **Aurora Bank** (8% → 14%).

O time de Advisors da Mastercard foi contratado para diagnosticar os principais pontos críticos que impactam negativamente os resultados do banco e apresentar recomendações estratégicas acompanhadas de uma proposta de solução.

### Evolução de Market Share — 2025 (valor transacionado)

| Player | 2025 Q1 | 2025 Q2 | 2025 Q3 | 2025 Q4 | Δ |
|--------|---------|---------|---------|---------|---|
| **Priceless Bank** | **33%** | **28%** | **23%** | **19%** | **-14 p.p.** |
| LuminaPay | 17% | 23% | 28% | 30% | +13 p.p. |
| Papaya Bank | 33% | 31% | 30% | 28% | -5 p.p. |
| Aurora Bank | 8% | 9% | 11% | 14% | +6 p.p. |
| Lux Bank | 6% | 7% | 8% | 9% | +3 p.p. |

> **Leitura crítica:** O Priceless Bank perdeu share a cada trimestre, enquanto LuminaPay ultrapassou o banco em Q2/Q3 e hoje detém mais do dobro do share que tinha no início do ano. Aurora Bank quase dobrou sua participação. Apenas Papaya Bank também recua, mas a um ritmo muito menor.

---

### Benchmarking dos Concorrentes Diretos

O time de Strategy & Transformation da Mastercard conduziu estudo de benchmarking com instituições de proposta de valor semelhante ao Priceless Bank. Os dados abaixo são fundamentais para orientar as hipóteses sobre a perda de share.

#### LuminaPay — **Principal ameaça | Nativo digital**

| Atributo | Detalhe |
|----------|---------|
| **Perfil** | Fintech nativa digital, poucos anos de operação |
| **Público-alvo** | Jovens adultos, early adopters |
| **Diferenciais** | Programa de cashback · Sem taxa de cartão · **PIX no crédito** |
| **Principais gastos dos clientes** | 1º Restaurantes · 2º Mercados · 3º Transporte |
| **Maturidade digital** | Alta |
| **Canal de abertura/atendimento** | 100% digital |
| **Banco principal para % de clientes** | 37,4% |
| **Aceita Open Finance** | Sim |
| **% clientes que exportaram via Open Finance** | 62% |
| **NPS** | 76 |

**Correlação com o problema:** O diferencial "PIX no crédito" é provavelmente o principal vetor da canibalização do cartão no Priceless Bank. Com essa feature, o cliente do LuminaPay faz PIX para qualquer estabelecimento (incluindo aqueles sem maquininha) e parcela o valor como se fosse cartão de crédito — combinando a conveniência do PIX com o poder de compra do crédito. O Priceless Bank não possui equivalente, o que explica tanto a migração de clientes como o crescimento de PIX para PJ na base de dados.

---

#### Papaya Bank — **Concorrente tradicional | Estável**

| Atributo | Detalhe |
|----------|---------|
| **Perfil** | Banco tradicional, bem consolidado no mercado |
| **Público-alvo** | Adultos de meia-idade e idosos |
| **Diferenciais** | Programa de pontos · Financiamentos · Cartão adicional sem anuidade |
| **Principais gastos dos clientes** | 1º Mercados · 2º Automotivo · 3º Saúde |
| **Maturidade digital** | Baixa |
| **Canal de abertura/atendimento** | Digital + Físico (agência) |
| **Banco principal para % de clientes** | 42,7% |
| **Aceita Open Finance** | Sim |
| **% clientes que exportaram via Open Finance** | 44% |
| **NPS** | 64 |

**Correlação com o problema:** O Papaya Bank atende exatamente o mesmo perfil demográfico do Priceless Bank (adultos de meia-idade), o que indica sobreposição de público. Sua leve queda de share (-5 p.p.) sugere que ambos os bancos tradicionais estão perdendo para os nativos digitais. Contudo, o Papaya mantém o maior índice de "banco principal" (42,7%), indicando maior engajamento e fidelidade da sua base.

---

#### Aurora Bank — **Crescimento acelerado | Foco em investimentos**

| Atributo | Detalhe |
|----------|---------|
| **Perfil** | Nativo digital, com forte foco em investimentos |
| **Público-alvo** | Jovens adultos de alta renda |
| **Diferenciais** | Produtos de investimentos exclusivos · Home Broker · **Investimento convertido em limite de crédito** |
| **Principais gastos dos clientes** | 1º Restaurantes · 2º Lazer · 3º Automotivo |
| **Maturidade digital** | Média |
| **Canal de abertura/atendimento** | Físico (agência) + Digital |
| **Banco principal para % de clientes** | 13,6% |
| **Aceita Open Finance** | Sim |
| **% clientes que exportaram via Open Finance** | 79% |
| **NPS** | 55 |

**Correlação com o problema:** O Aurora Bank quase dobrou seu share em 2025. Seu diferencial de converter saldo de investimentos em limite de crédito cria um mecanismo de retenção muito poderoso — clientes que investem não vão embora porque perderiam limite. Dado que o Priceless Bank possui a **Reservinha** (liquidez diária) como produto de investimento, existe uma oportunidade não explorada de criar mecanismo similar.

---

#### Lux Bank — **Nicho premium | Menor relevância para o diagnóstico**

| Atributo | Detalhe |
|----------|---------|
| **Perfil** | Banco Affluent, carteira de clientes selecionada |
| **Público-alvo** | Adultos de meia-idade com alta renda |
| **Diferenciais** | Concierge · Sala VIP exclusiva · Programa de fidelidade premium |
| **Principais gastos dos clientes** | 1º Viagem · 2º Restaurantes · 3º Automotivo |
| **Maturidade digital** | Baixa |
| **Canal de abertura/atendimento** | Físico (agência) + Digital |
| **Banco principal para % de clientes** | 6,4% |
| **Aceita Open Finance** | Não |
| **% clientes que exportaram via Open Finance** | 82% |
| **NPS** | 82 |

**Correlação com o problema:** O Lux Bank cresce modestamente (+3 p.p.) e atua em nicho premium distinto. Seu NPS de 82 é o mais alto do mercado — resultado de um portfólio de benefícios exclusivos que gera percepção de valor muito alta nos clientes. Embora não seja a ameaça principal, mostra que benefícios de lifestyle (viagem, concierge) são altamente valorizados no segmento de alta renda, faixa onde o Priceless Bank também tem clientes com cartões Black e Platinum.

---

### Mapa Competitivo Consolidado

| | Priceless Bank | LuminaPay | Papaya Bank | Aurora Bank | Lux Bank |
|--|--|--|--|--|--|
| Posição Q4/2025 | 19% | 30% | 28% | 14% | 9% |
| Perfil do cliente | Adulto / renda média-alta | Jovem digital | Adulto / idoso | Jovem / alta renda | Adulto / alta renda |
| Diferencial central | — | PIX no crédito | Pontos + financiamento | Invest. → limite | Lifestyle premium |
| Maturidade digital | ? | Alta | Baixa | Média | Baixa |
| NPS | ? | 76 | 64 | 55 | 82 |
| Banco principal | ? | 37,4% | 42,7% | 13,6% | 6,4% |

> **Gap estratégico evidente:** O Priceless Bank não possui diferencial claro em nenhuma das dimensões acima. A ausência de PIX no crédito é a lacuna mais urgente; a ausência de NPS e dados de engajamento conhecidos é uma limitação analítica para o diagnóstico completo.

---

## 1. Visão Geral das Bases

| Base | Registros | Colunas | Nulos | % Nulos | Chave |
|------|-----------|---------|-------|---------|-------|
| Clientes | 1.960 | 8 | 255 | 1,6% | Cliente_ID (PK) |
| Cartões | 4.006 | 7 | 450 | 16,1% | ID_Cartao (PK) |
| Transações | 156.826 | 13 | 393.244 | 19,3% | ID_Transacao (PK) |
| PIX | 278.940 | 8 | 836 | 0,04% | — |
| Investimentos | 21.200 | 7 | 28 | 0,02% | — |

**Período coberto:** Janeiro 2023 — Dezembro 2025

**Chave de integração central:** `Cliente_ID` presente em todas as bases. `ID_Cartao` liga cartões às transações.

---

## 2. Schema Visual — Relacionamento entre Bases

```mermaid
erDiagram
    CLIENTES ||--o{ CARTOES : "Cliente_ID (1:N)"
    CLIENTES ||--o{ PIX : "Cliente_ID (1:N)"
    CLIENTES ||--o{ TRANSACOES : "Cliente_ID (1:N)"
    CLIENTES ||--o{ INVESTIMENTOS : "Cliente_ID (1:N)"
    CARTOES  ||--o{ TRANSACOES : "ID_Cartao (1:N)"

    CLIENTES {
        int Cliente_ID PK "1.960 registros"
        date Data_Nascimento
        float Renda_Anual "255 nulls"
        int Numero_Cartoes
        string Cidade
        string Estado
        bool Possui_Conta_Adicional
    }

    CARTOES {
        int ID_Cartao PK "4.006 registros"
        int Cliente_ID FK
        string Produto_Mastercard
        string Tipo_Cartao
        date Data_Emissao "qualidade"
        float Limite_Cartao
    }

    PIX {
        int Cliente_ID FK "278.940 registros"
        float Valor "917 negativos"
        string Tipo_transacao
        bool Aprovado
        string PF_PJ
        bool Agendado
    }

    TRANSACOES {
        int ID_Transacao PK "156.826 registros"
        int Cliente_ID FK
        int ID_Cartao FK
        float Valor_Compra "165 negativos"
        string Industria
        string Tipo_Compra
        string Input_Mode
        string Wallet
        string Crossborder "95.6% null (design)"
        string Contactless "82.5% null (design)"
    }

    INVESTIMENTOS {
        int Cliente_ID FK "21.200 registros"
        string Produto_Investimento
        float Valor_Aplicado "1566 negativos"
        float Saldo_Atual
        date Data_de_vencimento
    }
```

**Notas:** ⚠️ = anomalia detectada | "design" = comportamento esperado do sistema

---

## 3. Cobertura dos Clientes por Base

| Cobertura | Qtd Clientes | % do Total |
|-----------|-------------|------------|
| Total na base clientes | 1.960 | 100% |
| Com transações por cartão | 1.431 | 73% |
| Com atividade PIX | 1.430 | 73% |
| Com investimentos | 1.003 | 51% |
| Trans + PIX (simultaneamente) | 1.056 | 54% |
| Trans + PIX + Investimentos | 534 | 27% |
| Sem nenhuma atividade registrada | ~529 | ~27% |

**Achado relevante:** 27% dos clientes não aparecem em nenhuma base transacional. Podem ser clientes novos, inativos ou com dados ausentes — requerem investigação.

---

## 4. Base Clientes — Perfil Demográfico

### Dicionário de Colunas

| Campo | Tipo | Descrição (fonte: dicionário oficial) | Observações |
|-------|------|---------------------------------------|-------------|
| `Cliente_ID` | INT | Identificador único do cliente. | **Chave primária** — presente em todas as bases |
| `Data_Nascimento` | DATE | Data de nascimento do cliente. | Formato DD/MM/AAAA |
| `Renda_Anual` | FLOAT | Renda anual informada pelo cliente (em Reais). | **255 nulos (13%)** — dado declaratório |
| `Data_Criacao_Conta` | DATE | Data de criação da conta do cliente. | Cobre Jan/2023 a Dez/2025 |
| `Numero_Cartoes` | INT | Número total de cartões que o cliente possui. | Varia de 1 a 4 |
| `Cidade` | STR | Cidade de residência do cliente. | — |
| `Estado` | STR | Estado de residência do cliente. | 6 estados: SP, MG, RS, BA, PR, RJ |
| `Possui_Conta_Adicional` | STR | Flag se o cliente possui conta adicional (Sim/Não). | 21,2% possuem |

### Dados-chave
- **1.960 clientes únicos** com conta criada entre Jan/2023 e Dez/2025
- **Idade média:** 49,5 anos | Mediana: 50 | Mín: 18 | Máx: 76
- **Renda anual média:** R$ 85.020 | Mediana: R$ 85.000 | Mín: R$ 20k | Máx: R$ 150k
- **255 clientes (13%)** sem Renda_Anual declarada
- **Distribuição geográfica uniforme** entre 6 estados (SP, MG, RS, BA, PR, RJ — ~320 clientes cada)
- **21,2% possuem conta adicional**

### Distribuição por faixa etária
| Faixa | Clientes |
|-------|----------|
| 18-29 | ~170 |
| 30-39 | ~290 |
| 40-49 | ~380 |
| 50-59 | ~400 |
| 60-69 | ~420 |
| 70+ | ~300 |

### Distribuição de cartões por cliente
- 1 cartão: 520 clientes (26,5%)
- 2 cartões: 439 clientes (22,4%)
- 3 cartões: 471 clientes (24%)
- 4 cartões: 530 clientes (27%)

### Interpretação para o diagnóstico
O perfil demográfico revela um **cliente de meia-idade com renda média-alta**. Comparando com o benchmarking dos concorrentes, o LuminaPay (principal ganhador de share) foca em **jovens adultos e early adopters** — uma lacuna que o Priceless Bank não está cobrindo. A base tende ao envelhecimento sem renovação pelo público digital-first.

---

## 5. Base Cartões — Portfólio e Anomalias

### Dicionário de Colunas

| Campo | Tipo | Descrição (fonte: dicionário oficial) | Observações |
|-------|------|---------------------------------------|-------------|
| `ID_Cartao` | INT | Identificador único do cartão. | **Chave primária** — FK em Base_transacoes |
| `Produto_Mastercard` | STR | Categoria/variante do cartão Mastercard (Gold, Platinum, Black, Maestro/Debit, Standard). | Platinum = 30,7%, Black = 23,7% |
| `Tipo_Cartao` | STR | Tipo do cartão: Crédito ou Débito. | 85% Crédito, 15% Débito |
| `Data_Emissao` | DATETIME | Data e hora em que o cartão foi emitido. | — |
| `Data_Ativacao` | DATETIME | Data e hora em que o cartão foi ativado. | **⚠️ 450 registros com ativação < emissão** |
| `Data_Validade` | DATE | Data de validade do cartão. | **⚠️ 450 nulos** (mesmos 450 com erro de ativação) |
| `Limite_Cartao` | FLOAT | Limite de crédito concedido no cartão (em Reais). | Débito tem limite = 0 |

### Composição do portfólio
| Produto | Qtd | % |
|---------|-----|---|
| Platinum | 1.229 | 30,7% |
| Black | 949 | 23,7% |
| Gold | 804 | 20,1% |
| Maestro/Debit | 606 | 15,1% |
| Standard | 418 | 10,4% |

- **85% crédito, 15% débito**
- Limite médio de crédito: **R$ 16.146**
- Limite mediano: R$ 16.000

### Limites por produto (crédito)
- Standard: R$ 1k–5k
- Gold: R$ 5k–15k
- Platinum: R$ 15k–30k
- Black: R$ 30k–52k

### ⚠️ Anomalias Identificadas

**1. 450 cartões ativados ANTES da data de emissão (11,2%)**
- Data_Ativacao < Data_Emissao — fisicamente impossível
- Esses exatamente 450 cartões também têm Data_Validade = nula
- **Causa provável:** erro na geração/importação dos dados de simulação
- **Ação:** excluir ou isolar esses 450 cartões de análises temporais

**2. 469 cartões sem nenhuma transação (11,7%)**
- Cartões emitidos e na base mas que nunca foram usados
- Distribuição entre produtos: Black (124), Gold (118), Platinum (114), Standard (110)
- **Interpretação:** alto índice de não-ativação/não-engajamento pós-emissão
- **Sinal de alerta:** preditor de churn e baixo engajamento

**3. 1.017 cartões vencidos (28,5% dos cartões com validade)**
- Cartões cuja Data_Validade já passou em relação a Jun/2026
- Não indicam erro; podem representar cartões não renovados (possível churn)

---

## 6. Base Transações — Comportamento de Consumo

> **Esta é a base mais crítica para o diagnóstico.** Contém o histórico de uso do cartão e revela diretamente o desempenho transacional do banco.

### Dicionário de Colunas

| Campo | Tipo | Descrição (fonte: dicionário oficial) | Observações |
|-------|------|---------------------------------------|-------------|
| `ID_Transacao` | INT | Identificador único da transação. | **Chave primária** |
| `Data` | DATETIME | Data e hora em que a transação foi realizada. | Jan/2023 a Dez/2025 |
| `Valor_Compra` | FLOAT | Valor monetário da compra realizada. | **⚠️ 165 valores negativos** (estornos); outlier max R$107.777 |
| `Industria` | STR | Setor da indústria onde a compra foi realizada (Alimentação, Varejo, Saúde, etc.). | 6 setores; Varejo = 35% |
| `Tipo_Compra` | STR | Tipo de compra: CP (Cartão Presente – presencial) ou CNP (Cartão Não Presente – online). | 70% CP, 30% CNP |
| `Qtd_Parcelas` | INT | Quantidade de parcelas da compra, se aplicável. | **72% nulo = à vista** (comportamento correto) |
| `Wallet` | STR | Carteira digital utilizada (Apple Pay, Google Pay, Samsung Pay). | **85,9% nulo** — correto: só quando wallet foi usada |
| `Cliente_ID` | INT | Identificador único do cliente que realizou a transação. | **FK → Base_clientes** |
| `ID_Cartao` | INT | Identificador único do cartão utilizado na transação. | **FK → Base_cartoes** |
| `Input_Mode` | STR | Modo de entrada da transação (Chip, Swiped, PayPass, eCommerce, MasterPass, etc.). | 8 modalidades |
| `Input_Mode_Code` | INT | Código numérico associado ao modo de entrada. | Equivalente codificado do Input_Mode |
| `Crossborder` | INT | Indica se a transação foi internacional (1 = Internacional; 0 = Nacional). | **⚠️ 95,6% nulo — por design:** só preenchido em CNP online |
| `Contactless` | INT | Indica se a transação foi por aproximação (1 = Sim; 0 = Não). | **⚠️ 82,5% nulo — por design:** só preenchido em transações físicas |

### Dados-chave
- **156.826 transações** | 1.431 clientes | 3.537 cartões únicos usados
- Período: Jan/2023 – Dez/2025
- **Ticket médio:** R$ 913 | **Ticket mediano:** R$ 690

### Distribuição por indústria
| Indústria | Transações | % |
|-----------|-----------|---|
| Varejo | 54.849 | 35% |
| Alimentação | 39.259 | 25% |
| Tecnologia | 31.429 | 20% |
| Entretenimento | 12.765 | 8% |
| Saúde | 10.943 | 7% |
| Educação | 7.581 | 5% |

### Ticket médio por indústria
- Educação e Tecnologia: maiores tickets médios (~R$1.200+)
- Alimentação: ticket mais baixo (~R$600)

### Canais de pagamento (Input Mode)
- PayPass (contactless físico): 23,3%
- Chip: 23,3%
- Swiped (tarja): 23,3%
- Phone Order: 6,1%
- eCommerce: 6,1%
- MasterPass: 6,0%
- Recurring: 5,9%
- Mail Order: 5,9%

### Tipo de compra
- CP (presencial): 70%
- CNP (não presencial/online): 30%

### Parcelamento
- 72% das transações são à vista (Qtd_Parcelas nula)
- 28% parceladas — média de 6,5 parcelas, máximo de 12

### ⚠️ Anomalias e Cuidados

**1. Crossborder: 95,6% nulo**
- Não é erro: o campo só é preenchido para transações CNP online (eCommerce, MasterPass, etc.)
- Para análise: usar apenas as linhas onde Crossborder não é nulo

**2. Contactless: 82,5% nulo**
- Também por design: só preenchido para transações físicas (Chip, Swiped, PayPass)

**3. 165 valores negativos (0,1%)**
- Possíveis estornos ou chargebacks
- Recomendação: excluir ou criar flag `is_estorno`

**4. Wallet: 134.716 nulos (85,9%)**
- Correto: wallet só aparece quando o cliente usa Apple Pay, Google Pay ou Samsung Pay
- 22.110 transações com wallet — divididas igualmente entre os três

**5. Outliers: 84 transações acima de R$10k, 7 acima de R$50k**
- Máximo detectado: R$107.777 em Educação via PayPass — merece investigação
- Podem ser legítimas (pagamentos de cursos, equipamentos) mas distorcem médias

---

## 7. Base PIX — Comportamento de Transferências

> **Segunda base mais importante.** Com 278.940 registros é a maior base disponível e revela um padrão crítico de migração de meios de pagamento.

### Dicionário de Colunas

| Campo | Tipo | Descrição (fonte: dicionário oficial) | Observações |
|-------|------|---------------------------------------|-------------|
| `Cliente_ID` | INT | Identificador único do cliente que realizou a transação. | **FK → Base_clientes** |
| `Valor` | FLOAT | Valor monetário do PIX realizado. | **⚠️ 917 negativos e 591 zeros** — incoerentes |
| `Data` | DATETIME | Data e hora em que o PIX foi realizado. | **⚠️ 418 nulos** — registros incompletos |
| `Pix_para_si_mesmo` | INT | Indica se a transferência é entre contas de mesma titularidade (1 = Sim; 0 = Não). | 11,6% são para si mesmo (transferências internas) |
| `Tipo_transacao` | STR | Indica se o PIX foi um "Envio" ou um "Recebimento". | 88% Envios, 12% Recebimentos |
| `Aprovado` | INT | Indica se o PIX foi aprovado (1 = Sim; 0 = Não). | **⚠️ 10% dos envios não aprovados** — taxa elevada |
| `PF_PJ` | STR | Indica se o destinatário é conta PF (Pessoa Física) ou PJ (Pessoa Jurídica). | **62% PJ** — clientes pagando em estabelecimentos |
| `Agendado` | STR | Indica se o PIX foi agendado ("Sim") ou não ("Não"). | Apenas 2% agendados |

### Dados-chave
- **278.940 registros** | 1.430 clientes únicos
- Média de **195 transações PIX por cliente**
- Valor mediano do PIX (envios positivos): **R$ 195**

### Distribuição dos PIX
| Dimensão | Valor | % |
|----------|-------|---|
| Envios | 245.665 | 88% |
| Recebimentos | 32.857 | 12% |
| Aprovados | 250.855 | 89,9% |
| Não aprovados | 28.085 | 10,1% |
| Para PJ | 172.564 | 61,9% |
| Para PF | 106.376 | 38,1% |
| Para si mesmo | 32.305 | 11,6% |
| Agendados | 5.531 | 2% |

### ⚠️ Anomalias Identificadas

**1. 917 valores negativos (0,3%) — ALERTA**
- PIX com valor negativo não faz sentido operacionalmente
- Pode ser: estorno de PIX, erro de sinal, ou fraude
- Recomendação: investigar com a equipe de risco

**2. 591 valores zero (0,2%) — ALERTA**
- PIX de R$ 0,00 — operação sem sentido
- Recomendação: excluir da análise

**3. 418 registros com Data e Tipo_transacao nulos**
- Registros incompletos — excluir da análise temporal

**4. 3.392 recebimentos com Aprovado=0 (10,3% dos recebimentos) — SUSPEITO**
- Um "recebimento negado" é incomum — o destinatário recusa um PIX?
- Pode indicar problema no sistema, fraude ou regra de negócio não documentada

**5. 24.644 envios não aprovados (10% dos envios)**
- Taxa elevada — média de mercado é ~1-3%
- Possíveis causas: limites excedidos, suspeita de fraude, saldo insuficiente

### Interpretação crítica: PIX para PJ
**62% dos envios PIX têm como destinatário PJ (empresas)**. Isso significa que clientes estão usando PIX para pagar em estabelecimentos comerciais — diretamente substituindo o cartão de crédito/débito. Este é um dos fatores mais prováveis da queda de market share transacional.

---

## 8. Base Investimentos — Carteira do Banco

### Dicionário de Colunas

| Campo | Tipo | Descrição (fonte: dicionário oficial) | Observações |
|-------|------|---------------------------------------|-------------|
| `Cliente_ID` | INT | Identificador único do cliente que realizou a operação na conta de investimento. | **FK → Base_clientes** |
| `Data_Abertura_Conta_Inv` | INT | Data de abertura da conta de investimento. | **⚠️ Formato YYYYMM** — inteiro, requer conversão |
| `Data` | INT | Data em que a operação de investimento foi realizada. | **⚠️ Formato YYYYMM** — diferente das outras bases |
| `Valor_Aplicado` | FLOAT | Valor monetário da operação de investimento realizada. | **1.566 valores negativos = resgates** (comportamento normal) |
| `Saldo_Atual` | FLOAT | Valor monetário que o produto apresenta na data analisada. | 2.551 registros com saldo = 0 (produto vencido/resgatado) |
| `Produto_Investimento` | STR | Nome do produto de investimento. | Reservinha, Renda Variável, Tesouro Direto, Renda Fixa |
| `Data_de_vencimento` | INT | Data de vencimento do produto de investimento. | **⚠️ 299901 para toda a Reservinha** — sem vencimento (esperado, produto de liquidez diária) |

### Dados-chave
- **21.200 registros** | 1.003 clientes únicos (51% da base)
- Média de 21 registros por cliente (múltiplas operações ao longo do tempo)
- Saldo médio atual: **R$ 20.740**

### Distribuição por produto
| Produto | Registros | % | Característica |
|---------|-----------|---|----------------|
| Reservinha | 7.864 | 37,1% | Liquidez diária, sem vencimento |
| Renda Variável | 4.534 | 21,4% | Risco maior, maior retorno |
| Tesouro Direto | 4.471 | 21,1% | Renda fixa pública |
| Renda Fixa | 4.331 | 20,4% | Renda fixa privada |

### Comportamentos esperados (não são erros)

**Valor_Aplicado negativo (1.566 registros):** São **resgates** (saída de dinheiro). Comportamento normal de uma carteira de investimentos. Separar aportes (>0) de resgates (<0) nas análises.

**Data_de_vencimento = 299901 (7.864 registros):** Todos são "Reservinha" — produto de liquidez diária sem data de vencimento definida. Comportamento esperado do produto.

**Saldo_Atual = 0 (2.551 registros):** Produto vencido ou totalmente resgatado. Não é erro.

**Datas no formato YYYYMM (inteiro):** Diferente das outras bases — requer conversão para análises temporais.

### Interpretação para o diagnóstico
A **Reservinha** (37% dos registros) funciona como uma "conta cofre" de liquidez diária — possivelmente substituindo poupança. Clientes com investimentos tendem a ser mais engajados e fiéis ao banco. Pode ser alavancada como **diferencial de retenção** frente ao LuminaPay.

---

## 9. Análise Temporal — O Sinal Mais Crítico

### Volume transacional por cartão (trimestral)
| Trimestre | Volume Cartão | Qtd Trans |
|-----------|--------------|-----------|
| 2023Q1 | R$ 7,4M | 12.244 |
| 2023Q2 | R$ 6,6M | 10.805 |
| 2023Q3 | R$ 7,1M | 11.588 |
| 2023Q4 | R$ 7,4M | 11.930 |
| **2024Q1** | **R$ 16,5M** | **10.651** |
| **2024Q2** | **R$ 17,2M** | **10.936** |
| **2024Q3** | **R$ 20,7M** | **13.193** |
| **2024Q4** | **R$ 23,4M** | **15.131** |
| 2025Q1 | R$ 11,8M | 19.145 |
| 2025Q2 | R$ 11,5M | 18.732 |
| 2025Q3 | R$ 7,8M | 12.811 |
| 2025Q4 | R$ 5,9M | 9.660 |

### Volume PIX enviado (trimestral)
| Trimestre | Volume PIX | Qtd PIX |
|-----------|-----------|---------|
| 2023Q1 | R$ 5,5M | 26.504 |
| 2023Q2 | R$ 5,7M | 26.850 |
| 2023Q3 | R$ 5,6M | 27.116 |
| 2023Q4 | R$ 5,4M | 26.732 |
| 2024Q1 | R$ 5,3M | 26.868 |
| 2024Q2 | R$ 5,1M | 26.545 |
| 2024Q3 | R$ 5,8M | 27.195 |
| 2024Q4 | R$ 5,5M | 27.005 |
| **2025Q3** | **R$ 20,1M** | **25.669** |
| **2025Q4** | **R$ 31,4M** | **38.038** |

### 🔴 Achado Crítico: Inversão Cartão-PIX em 2025

Em 2025, ocorre uma inversão dramática:
- Cartão: pico de **R$23,4M em 2024Q4** → queda para **R$5,9M em 2025Q4** (-75%)
- PIX: estável em ~R$5,5M/trimestre até 2024 → explosão para **R$31,4M em 2025Q4** (+470%)

A razão PIX/Cartão (em quantidade de transações) cresce consistentemente ao longo dos trimestres, indicando **substituição sistemática** do cartão pelo PIX como meio de pagamento.

**Nota metodológica importante:** A queda no número de transações de 2025 pode ser parcialmente explicada pelo fato de os dados de 2025 serem mais recentes e incompletos, mas a magnitude da inversão é demasiado expressiva para ser apenas um artefato de dados.

### 9.2 Estimativa de Receita de Intercâmbio Perdida

> O **intercâmbio** é a tarifa que o banco emissor (Priceless Bank) recebe do adquirente em cada transação aprovada no cartão. PIX tem **intercâmbio zero** por regulação do Banco Central — toda transação migrada para PIX representa receita zerada para o emissor.

#### Metodologia

| Parâmetro | Valor | Fonte |
|-----------|-------|-------|
| Taxa de intercâmbio — Crédito | **1,8%** | Benchmark Mastercard Brasil (média doméstica) |
| Taxa de intercâmbio — Débito | **0,6%** | Teto regulatório BACEN |
| Taxa média ponderada do portfólio | **~1,65%** | (83% crédito × 1,8% + 17% débito × 0,6%) |
| Ticket-base normalizado | **R$ 615** | Mediana 2023 e 2025 (excluindo anomalia 2024) |
| Baseline de referência | **2023Q4 normalizado** | Último trimestre antes da anomalia de ticket de 2024 |

**⚠️ Nota metodológica sobre o ticket de 2024:** O ticket médio das transações em 2024 é ~R$1.550/tx — exatamente 2,5x maior que 2023 e 2025 (~R$615/tx). Esse padrão é um artefato na geração dos dados sintéticos do challenge (mesma quantidade de transações, mas volume 2,5x maior). Para comparações intertemporais, a análise usa o **intercâmbio normalizado** (quantidade real × ticket-base × taxa média), que elimina esse distorção.

**⚠️ Dado ausente:** Os registros de PIX de 2025Q1 e Q2 estão completamente ausentes do dataset. A análise de custo de oportunidade PIX cobre apenas os trimestres disponíveis.

#### Intercâmbio Estimado por Trimestre

| Trimestre | Vol. Cartão | Qtd. Tx | Ticket Médio | Intercâmbio Real | Intercâmbio Norm. | Perda vs 2023Q4 |
|-----------|-------------|---------|-------------|-----------------|------------------|----------------|
| 2023Q1 | R$ 7,4M | 12.233 | R$ 607 | R$ 126k | R$ 126k | — |
| 2023Q2 | R$ 6,6M | 10.792 | R$ 615 | R$ 113k | R$ 111k | — |
| 2023Q3 | R$ 7,1M | 11.579 | R$ 612 | R$ 120k | R$ 119k | — |
| 2023Q4 | R$ 7,4M | 11.921 | R$ 618 | R$ 125k | **R$ 123k ← ref.** | — |
| ⚠️ 2024Q1 | R$ 16,5M | 10.642 | **R$ 1.550** | R$ 280k | R$ 110k | R$ 13k |
| ⚠️ 2024Q2 | R$ 17,2M | 10.921 | **R$ 1.579** | R$ 293k | R$ 113k | R$ 10k |
| ⚠️ 2024Q3 | R$ 20,7M | 13.180 | **R$ 1.573** | R$ 352k | R$ 136k | — |
| ⚠️ 2024Q4 | R$ 23,5M | 15.118 | **R$ 1.552** | R$ 398k | R$ 156k | — |
| 🔴 2025Q1 | R$ 11,8M | 19.117 | R$ 617 | R$ 200k | R$ 197k | — |
| 🔴 2025Q2 | R$ 11,5M | 18.713 | R$ 613 | R$ 195k | R$ 193k | — |
| 🔴 2025Q3 | R$ 7,8M | 12.793 | R$ 610 | R$ 133k | R$ 132k | **R$ 0** |
| 🔴 2025Q4 | R$ 5,9M | 9.652 | R$ 613 | R$ 100k | R$ 100k | **R$ 23k/tri** |

> **Observação sobre 2025Q1/Q2:** Embora o ticket seja normal (R$615), a quantidade de transações em Q1 (19.117) e Q2 (18.713) é anormalmente alta comparada ao padrão histórico (~11-13k/tri), gerando intercâmbio elevado. Em Q3 e Q4 o volume de transações despenca de volta (~10-13k), com intercâmbio caindo para R$100-133k.

#### Custo de Oportunidade — PIX para PJ

| Trimestre | Vol. PIX→PJ | Qtd. PIX | Oport. Intercâmbio (1,8%) |
|-----------|-------------|---------|--------------------------|
| 2023Q1–Q4 | ~R$ 3,6M/tri | ~14.700/tri | ~R$ 65k/tri |
| 2024Q1–Q4 | ~R$ 3,5M/tri | ~14.500/tri | ~R$ 63k/tri |
| 2025Q3 | **R$ 13,5M** | 13.273 | **R$ 243k** |
| 2025Q4 | **R$ 19,9M** | 19.645 | **R$ 358k** |

#### KPIs de Impacto

| Métrica | Valor |
|---------|-------|
| Intercâmbio em 2025Q4 (normalizado) | R$ 100k/trimestre |
| Custo de oportunidade PIX→PJ em 2025Q4 | **R$ 358k/trimestre** |
| Razão PIX-PJ / Vol. Cartão em 2025Q4 | **3,4×** (PIX PJ supera o cartão) |
| Se banco recuperasse 50% do PIX PJ para cartão | +R$ 179k/tri ≈ 179% da receita atual |
| Intercâmbio anualizado em risco (extrapolando Q4 2025) | **~R$ 400k/ano** |

#### Interpretação

Em 2025Q4, o volume de PIX para estabelecimentos (R$19,9M) é **3,4× maior** que o volume total de cartão (R$5,9M). Se apenas **30% desse PIX PJ** fosse convertido em transação de cartão de crédito, o banco praticamente dobraria sua receita de intercâmbio trimestral.

O custo de oportunidade não é apenas contábil: cada transação PIX PJ representa também **perda de dados de consumo** (setor, ticket, recorrência) que alimentam scoring, ofertas e cross-sell — ativos intangíveis que se degradam junto com o volume de cartão.

### 9.3 Distribuição de Idades e Uso do PIX

Cruzamento entre `Base_clientes` e `Base_pix` para entender **quem usa PIX**, com que **intensidade** e quanto **volume movimenta** por faixa etária.

#### Penetração do PIX por Faixa Etária

| Faixa | Clientes | Usa PIX | % Penetração | Sem PIX |
|-------|----------|---------|-------------|---------|
| 18-29 | 115 | 77 | 67% | 38 |
| 30-39 | 279 | 203 | 73% | 76 |
| 40-49 | 578 | 442 | **76%** | 136 |
| 50-59 | 562 | 409 | 73% | 153 |
| 60-69 | 336 | 233 | 69% | 103 |
| 70+   | 90  | 66  | 73% | 24 |

> A faixa 40-49 tem a maior penetração (76%), não a mais jovem. A faixa 18-29 tem a menor (67%) — mas isso é enganoso: ela é a **menor faixa** do banco, um sinal de que o banco não está captando o público jovem.

#### Intensidade de Uso e Volume por Cliente

| Faixa | PIX tx/cli | Cartão tx/cli | **Razão PIX÷Cartão** | Vol PIX/cli | Vol Cartão/cli | Mediana PIX |
|-------|-----------|--------------|----------------------|------------|----------------|-------------|
| **18-29** | **438** | **119** | **🔴 3,7×** | **R$ 153k** | R$ 107k | R$ 188 |
| 30-39 | 181 | 107 | 1,7× | R$ 76k | R$ 98k | R$ 191 |
| 40-49 | 180 | 107 | 1,7× | R$ 78k | R$ 97k | R$ 192 |
| 50-59 | 181 | 112 | 1,6× | R$ 79k | R$ 104k | R$ 203 |
| 60-69 | 171 | 114 | 1,5× | R$ 74k | R$ 103k | R$ 197 |
| **70+** | **194** | **97** | **🟡 2,0×** | **R$ 95k** | R$ 88k | **R$ 252** |

**Achados críticos:**

**🔴 Faixa 18-29 — O alerta mais urgente:**
- Fazem **3,7× mais transações PIX do que cartão** por cliente — a maior razão de todas as faixas
- Volume PIX por cliente (R$153k) é **2× maior** que nas faixas intermediárias (R$76-79k)
- Esses jovens *têm* cartão, *têm* limite — e **escolhem PIX ativamente**
- São apenas 115 clientes: o banco não está captando o público jovem que, quando existe, já prefere PIX ao cartão
- PIX para PJ: R$5,3M (14.996 transações) — proporcionalmente relevante dado o tamanho do grupo

**🟡 Faixa 70+ — Surpresa:**
- Segunda maior razão PIX÷Cartão (2,0×)
- Mediana de ticket PIX mais alta (R$252 vs R$188-203 nas outras faixas): fazem menos PIX, mas de valores maiores
- Volume por cliente via PIX (R$95k) supera o cartão (R$88k)

**🟢 Faixas 40-59 — O core atual do banco:**
- Menor razão PIX/Cartão (1,5-1,7×) — ainda usam cartão de forma equilibrada
- Respondem pelo maior volume absoluto de PIX (R$34M e R$32M) por serem os maiores grupos
- Mas a tendência de crescimento do PIX em 2025 está acelerando também nessas faixas

#### Volume PIX Total e Breakdown PJ por Faixa

| Faixa | Vol Total PIX | Vol PIX→PJ | % PJ | Qtd PIX→PJ |
|-------|--------------|------------|------|-----------|
| 18-29 | R$ 11,8M | R$ 5,3M | 45% | 14.996 |
| 30-39 | R$ 15,5M | R$ 7,5M | 48% | 18.161 |
| 40-49 | R$ 34,4M | R$ 16,7M | 49% | 39.718 |
| 50-59 | R$ 32,4M | R$ 15,8M | 49% | 36.833 |
| 60-69 | R$ 17,1M | R$ 8,3M | 48% | 19.884 |
| 70+   | R$ 6,3M  | R$ 3,0M  | 47% | 6.357 |

> A proporção PIX→PJ é uniforme entre todas as faixas (~47-49%), indicando que a canibalização do cartão é um comportamento **transversal a toda a base**, não concentrado em um grupo específico. Todas as idades estão usando PIX para pagar em estabelecimentos comerciais.

#### Evolução Temporal 2025 — Crescimento por Faixa

Volume de PIX enviado (Q3 → Q4 2025):

| Faixa | 2025Q3 | 2025Q4 | Crescimento |
|-------|--------|--------|-------------|
| 18-29 | R$ 1,23M | R$ 1,83M | +49% |
| 30-39 | R$ 3,11M | R$ 4,81M | +55% |
| 40-49 | R$ 7,26M | R$ 10,59M | **+46%** |
| 50-59 | R$ 6,62M | R$ 9,84M | **+49%** |
| 60-69 | R$ 3,66M | R$ 5,30M | +45% |
| 70+   | R$ 1,29M | R$ 1,71M | +33% |

> O crescimento do PIX em Q4 2025 é forte e **uniforme** em todas as faixas (+33% a +55%). Nenhuma faixa está revertendo a tendência — a migração para PIX está acelerando em toda a base simultaneamente.

#### Interpretação para o Diagnóstico

A análise de faixa etária revela **três dimensões do problema**:

1. **Captação:** O banco tem pouquíssimos clientes jovens (18-29 = 5,9% da base). O público que *mais adota* PIX e que o LuminaPay conquista está sub-representado.

2. **Comportamento:** Dentro de cada faixa, o PIX já supera o cartão em frequência de uso. Não é um problema "só dos jovens" — é um problema estrutural de toda a base.

3. **Aceleração:** O crescimento de Q3→Q4 2025 é robusto em todas as faixas, sinalizando que a janela de intervenção está se fechando. O Priceless Bank precisa agir antes que o padrão de preferência por PIX se consolide irreversivelmente.

### 9.4 Análise de Churn — Diagnóstico de Risco de Abandono

Churn em banco emissor tem **cinco manifestações distintas**. Os dados suportam a quantificação direta de quatro delas:

#### Taxonomia dos Cenários

| Tipo | Nome | Evidência | Urgência |
|------|------|-----------|---------|
| **A** | Churn Silencioso (PIX) | Volume cartão -75%, PIX→PJ +470% em 2025 | 🔴 Crítica |
| **B** | Conta Fantasma | 85 clientes sem registro em nenhuma base | 🟠 Alta |
| **C** | Inatividade 2025 | 87 clientes sem atividade alguma em 2025 | 🔴 Alta |
| **D** | Desinvestimento | Resgates acelerando — 2025Q4 recorde histórico | 🟡 Antecipada |
| **E** | Cartão Vencido | 1.018 cartões expirados, 56% premium | 🟠 Estrutural |

> **Limitação metodológica:** Os dados de PIX de 2025 cobrem apenas Q3 e Q4. O score de risco usa critérios de cartão e investimentos para evitar falsos positivos causados por essa lacuna.

#### [A] Churn Silencioso — PIX Substitui Cartão

Já documentado nas seções 9 e 9.2. Resumo dos indicadores-chave:
- Volume de cartão caiu de R$23,4M (2024Q4) para R$5,9M (2025Q4): **-75%**
- PIX→PJ no mesmo período: de R$3,3M para R$19,9M: **+470%**
- Em 2025Q4, o volume PIX→PJ supera o volume de cartão em **3,4×**
- **Motivação:** LuminaPay oferece "PIX no crédito" — o cliente faz PIX e parcela como cartão. O Priceless Bank não tem equivalente.

#### [B] Contas Fantasma

| Métrica | Valor |
|---------|-------|
| Clientes sem nenhuma atividade histórica | **85 (4,3%)** |
| Distribuição etária | 40-49: 20 · 50-59: 25 · 60-69: 18 · demais: 22 |
| Antiguidade média | 26 meses |
| Renda média | R$ 86.917 |
| Período de abertura | Jan/2023 – Dez/2025 |

**Motivação provável:** Falha crítica de onboarding. O cliente abriu a conta — possivelmente atraído por uma campanha — mas o produto não entregou valor suficiente para gerar a primeira transação. Em 26 meses, nunca fez um PIX, nunca usou o cartão, nunca investiu. Esse padrão é típico de bancos sem experiência digital fluida na jornada de ativação.

#### [C] Inatividade em 2025

| Métrica | Valor |
|---------|-------|
| Clientes inativos em 2025 (sem tx/PIX/inv) | **87 (4,4%)** |
| Antiguidade média | 27 meses |
| Renda média | R$ 86.245 |

Sub-cenários dentro dos 87 inativos:

| Sub-cenário | Clientes | Motivação provável |
|-------------|---------|-------------------|
| C.1 – Pararam cartão, ainda usam PIX | alguns | Migração funcional — PIX atende a necessidade diária |
| C.2 – Desapareceram completamente | alguns | Migração para banco concorrente |
| C.3 – Sumiram entre Q3→Q4 2025 | **39** | Deterioração recente — janela de intervenção ainda aberta |

**Concentração etária:** Faixas 50-59 (25) e 40-49 (20) — exatamente o público-alvo do Papaya Bank, que está crescendo. Hipótese: esses clientes migraram para o Papaya Bank ou estão em processo de abandono gradual.

**Alerta específico sobre Q3→Q4 2025:** 39 clientes usaram o cartão em Q3 mas não em Q4. A queda não é de ticket (mediana estável em R$597-598) mas de **frequência** (-25% em transações). Os clientes estão fazendo menos compras pelo cartão, não compras menores.

#### [D] Desinvestimento Acelerado

| Trimestre | Operações de Resgate | Volume Resgatado |
|-----------|---------------------|-----------------|
| 2023Q1–Q4 | 23–36/tri | ~R$ 25k/tri |
| 2024Q1 | 138 | R$ 677k |
| 2024Q2 | 154 | R$ 614k |
| 2024Q3 | 208 | R$ 1.302k |
| 2024Q4 | 210 | R$ 1.210k |
| 2025Q1 | 98 | R$ 862k |
| 2025Q2 | 105 | R$ 681k |
| 2025Q3 | 243 | R$ 1.593k |
| **2025Q4** | **284** | **R$ 1.632k ← RECORDE** |

**161 clientes** tiveram saldo líquido negativo em investimentos em 2025 (mais resgates do que aportes).

**Motivação provável:** Rentabilidade dos produtos de investimento inferior à concorrência. O Aurora Bank, que quase dobrou seu market share em 2025, tem como diferencial "produtos de investimentos exclusivos" e Home Broker. Clientes com perfil investidor tendem a comparar rentabilidade ativamente e mover o dinheiro para onde rende mais. A Reservinha (liquidez diária) é o produto mais popular do Priceless Bank — pode estar perdendo para equivalentes com maior rendimento.

#### [E] Cartões Vencidos Sem Renovação

| Produto | Cartões vencidos |
|---------|----------------|
| Platinum | 340 (33%) |
| Black | 241 (24%) |
| Gold | 195 (19%) |
| Maestro/Debit | 159 (16%) |
| Standard | 83 (8%) |
| **Total** | **1.018 (28,5% do portfólio válido)** |

Desses 1.018, apenas 4 nunca tiveram transação — a grande maioria estava em uso ativo até meados de 2025. O vencimento do cartão é um **momento de decisão**: o cliente precisa solicitar a renovação ativamente, e se o banco não facilita o processo ou não oferece incentivo, a probabilidade de churn aumenta drasticamente.

**Motivação provável:** Ausência de renovação automática ou de contato proativo do banco na aproximação do vencimento. Com 56% de cartões premium (Platinum + Black) na lista, o risco financeiro é alto — esses clientes têm limites de R$15k–52k.

#### Score de Risco Consolidado

| Nível | Clientes | Características |
|-------|---------|----------------|
| Baixo | ~884 | Ativos em Q3 e Q4 2025, sem resgates |
| Médio | ~32 | Algum sinal de fraqueza recente |
| Alto | ~533 | Sem cartão nos últimos trimestres + outros sinais |

**Achado sobre antiguidade:** O score alto não se concentra nos clientes mais novos — a relação entre antiguidade e risco é fraca. Clientes com 2-3 anos de conta aparecem em todas as faixas de risco, o que indica que o problema não é de retenção de recém-chegados, mas de **proposta de valor insuficiente para toda a base**.

#### Síntese — O Que os Dados Revelam Sobre as Motivações

| Motivação | Cenário | Evidência nos dados |
|-----------|---------|-------------------|
| Substituto funcional (PIX é mais fácil) | A | PIX→PJ 3,4× o cartão em Q4 2025 |
| Onboarding falho | B | 85 clientes, 26 meses de conta, zero atividade |
| Migração para concorrente | C | 87 inativos em 2025, perfil = público Papaya/LuminaPay |
| Rentabilidade de investimentos inferior | D | Resgates recordes em Q4 2025, Aurora crescendo |
| Falta de gestão de vencimento | E | 1.018 cartões expirados sem renovação registrada |

---

## 10. Radar de Qualidade dos Dados — Pegadinhas

### ⛔ CRÍTICO (impacto direto na análise)
| Problema | Base | Detalhe | Ação |
|----------|------|---------|------|
| Bug no código original | Notebook | `base_investimentos` carregava `Base_clientes.csv` — dados completamente errados | **Corrigido** |

### 🔴 Alto Impacto
| Problema | Base | Qtd | Ação |
|----------|------|-----|------|
| Cartões inativos (sem transação) | Cartões | 469 (11,7%) | Investigar engajamento |
| PIX com valor negativo | PIX | 917 (0,3%) | Excluir ou investigar |
| PIX com valor zero | PIX | 591 (0,2%) | Excluir |
| Recebimentos PIX negados | PIX | 3.392 (10,3%) | Investigar regra de negócio |

### 🟡 Médio Impacto
| Problema | Base | Qtd | Ação |
|----------|------|-----|------|
| Ativados antes da emissão | Cartões | 450 (11,2%) | Excluir da análise temporal |
| Data_Validade nula (mesmos 450) | Cartões | 450 | Excluir |
| Renda_Anual nula | Clientes | 255 (13%) | Imputar mediana ou flag |
| Valores negativos em transações | Transações | 165 (0,1%) | Excluir ou flag estorno |
| Outliers extremos (>R$10k) | Transações | 84 (0,05%) | Tratar separado |
| Data + Tipo nulos em PIX | PIX | 418 (0,15%) | Excluir |

### 🟢 Baixo Impacto (comportamento esperado)
| Aparente problema | Base | Explicação |
|-------------------|------|------------|
| Crossborder: 95,6% nulo | Transações | Por design: só preenchido em CNP |
| Contactless: 82,5% nulo | Transações | Por design: só preenchido em físico |
| Wallet: 85,9% nulo | Transações | Correto: só quando wallet é usado |
| Qtd_Parcelas: 72% nulo | Transações | Correto: null = pagamento à vista |
| Valor_Aplicado negativo | Investimentos | Resgates — comportamento normal |
| Data_vencimento 299901 | Investimentos | Reservinha sem vencimento — esperado |
| Saldo_Atual = 0 | Investimentos | Produto vencido ou resgatado |

---

## 11. Ranking das Bases — Criticidade para o Diagnóstico

### 🥇 1º — Base Transações (Score: 10/10)

**Por quê é a mais importante:**
- Registra diretamente o uso do cartão — o produto central do Priceless Bank
- Permite calcular: volume por período, ticket médio, taxa de utilização por cliente, comportamento por indústria e canal
- Evidência direta: volume trimestral caiu **~75%** de 2024Q4 para 2025Q4
- Cruzada com clientes: permite identificar **quem está comprando menos** e **em que segmento**
- Única base com informação de parcelamento — diferencial competitivo do cartão vs PIX

**Análises prioritárias:** Volume temporal · Ticket por indústria · Uso de canais · Taxa de parcelamento · Clientes que reduziram uso

---

### 🥈 2º — Base PIX (Score: 9/10)

**Por quê é a segunda mais importante:**
- A maior base em volume (278.940 registros) — comportamento frequente
- **62% dos envios vão para PJ** = pagamentos de consumo via PIX, direto concorrente do cartão
- O crescimento explosivo em 2025 (6x) é o espelho da queda do cartão
- Permite medir a **canibalização** do cartão pelo PIX dentro da própria base de clientes
- Taxa de reprovação de 10% nos envios é sinal de fricção ou fraude

**Análises prioritárias:** PIX para PJ vs volume cartão · Crescimento 2025 · Clientes que migraram · Taxa de aprovação

---

### 🥉 3º — Base Clientes (Score: 8/10)

**Por quê é a terceira mais importante:**
- Tabela mestre de segmentação — sem ela, não há como perfilar os outros achados
- Permite cruzar qualquer análise por: **faixa etária, renda, região, número de cartões**
- Idade média de 49 anos + renda de R$85k = perfil não alinhado com o público do LuminaPay
- Serve de eixo para identificar **qual segmento de cliente está mais em risco**

**Análises prioritárias:** Segmentação por renda/idade · Cruzamento com churn transacional · Correlação renda x limite x gasto

---

### 4º — Base Cartões (Score: 6/10)

**Por quê é a quarta:**
- Revela portfólio e limites — importante para calcular taxa de utilização do crédito
- 469 cartões inativos (11,7%) é um sinal claro de problema de engajamento
- Não tem volume temporal próprio — depende das transações para ganhar vida
- Importante para análise de renovação e vencimento

**Análises prioritárias:** Taxa de ativação · Limite vs gasto real · Cartões vencidos sem renovação

---

### 5º — Base Investimentos (Score: 5/10)

**Por quê é a menos urgente:**
- Presente em apenas 51% dos clientes — cobertura limitada
- Não revela diretamente o problema de market share transacional
- Pode ser estratégica como **âncora de retenção** (clientes com investimento tendem a ser mais fiéis)
- Reservinha pode ser diferencial competitivo não explorado

**Análises prioritárias:** Correlação investimento x uso cartão · Taxa de resgate (sinal de saída?) · Saldo médio por segmento

---

## 12. Key Insights — Diagnóstico Preliminar

### 🔴 Insight 1 — Canibalização do Cartão pelo PIX
O volume de transações por cartão **caiu ~75%** de 2024Q4 (R$23,4M) para 2025Q4 (R$5,9M), enquanto o volume de PIX **multiplicou por 6x** no mesmo período (R$5,5M → R$31,4M). Com **62% dos PIX enviados para PJ**, os clientes estão efetivamente pagando em estabelecimentos via PIX em vez do cartão. Este é o principal mecanismo explicativo da perda de share.

**Hipótese:** O LuminaPay oferece "PIX no crédito" como diferencial — o cliente faz o PIX e parcela como se fosse cartão. O Priceless Bank não tem equivalente.

---

### 🔴 Insight 2 — Cartões Não Ativados e Não Renovados
- **469 cartões (11,7%)** nunca fizeram uma única transação
- **1.017 cartões (28,5%)** já estão vencidos
- A não-ativação é um forte preditor de churn. Falha no onboarding ou ausência de estímulo pós-emissão

---

### 🟡 Insight 3 — Perfil Demográfico Não Alinhado com o Mercado em Crescimento
A base tem **idade média de 49 anos** e **renda média de R$85k**. O LuminaPay, principal ganhador, foca em jovens adultos e early adopters. O Priceless Bank está concentrado em um público que, embora tenha renda, é menos propenso à migração digital agressiva — mas isso não está protegendo o banco, pois o share ainda está caindo.

---

### 🟡 Insight 4 — Taxa de Reprovação de PIX Elevada
**24.644 envios não aprovados (10% dos envios)** e **3.392 recebimentos negados (10,3%)** são taxas incomuns. Podem indicar problemas de fraude, limites muito restritivos ou fricção no processo de pagamento digital — deteriorando a experiência do cliente.

---

### 🟢 Insight 5 — Investimentos como Âncora de Retenção Subutilizada
A **Reservinha** (liquidez diária) é o produto de investimento mais popular com 37% dos registros. Clientes com investimentos ativos tendem a ter maior LTV e menor propensão ao churn. Este produto pode ser alavancado como diferencial competitivo frente ao LuminaPay (que não tem oferta de investimentos).

---

## 13. Próximos Passos Analíticos

1. **Mapa de clientes fugitivos:** Cruzar redução de transações por cartão + aumento de PIX por cliente → identificar quem está migrando e qual o perfil
2. **Análise de segmento em risco:** Faixa etária + renda dos clientes com maior queda de uso de cartão em 2025
3. **Hipótese de fidelidade via investimento:** Clientes com saldo em investimentos têm maior gasto no cartão? Menor taxa de redução em 2025?
4. **Análise de cartões inativos:** Quais segmentos e produtos concentram mais cartões sem uso?
5. **Benchmarking interno:** O ticket médio do Priceless Bank está acima ou abaixo do padrão do setor? Qual indústria está perdendo mais transações?

---

*Documento gerado em 12/06/2026 | Atualizado em 12/06/2026 | Análise realizada em `main.ipynb`*
*Visualizações salvas em `docs/schema_banco_dados.png`, `docs/analise_temporal_cartao_pix.png`, `docs/ranking_bases.png`*
*Dicionário de dados: `data/Dicionário de Dados - Priceless Bank.xlsx` | Benchmarking: `data/20260608_MC_Challenge_Inteli.pdf`*
