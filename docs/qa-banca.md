# Q&A da Banca — respostas de uma linha
**Priceless Bank · Mastercard Challenge 2026 · preparação para os 3 minutos de perguntas**

Cada número citado abaixo é reproduzível no `notebooks/main.ipynb` (célula indicada).

---

**1. "O Pix 3× maior que o cartão inclui transações não aprovadas?"**
Não — usamos **envios aprovados** em todo o trabalho (R$ 17,9M de Pix→PJ vs R$ 5,9M de cartão = **3,0×**); com os não aprovados seria 3,4×, mas aprovado é o universo honesto para falar de volume efetivo. *(Parte 2, célula A.2)*

**2. "A queda de 75% do cartão não é efeito do ticket inflado de 2024?"**
Exato — por isso a nossa manchete é a queda **intra-2025: −50%** (R$ 11,8M → 5,9M), imune ao artefato; contra 2024Q4 a queda é 75% em valor e **−36% em quantidade**, e nós mesmos normalizamos o ticket de 2024 no cálculo de intercâmbio. *(Seções 9 e 9.2)*

**3. "Vocês mostraram a migração cartão→Pix no nível do cliente?"**
A evidência é agregada — e testamos o nível individual: a correlação por cliente entre Δcartão e ΔPix é ~0, o que indica migração **uniforme da base inteira** (todas as faixas crescem +34–54% em Pix), não um segmento trocando de trilho. É por isso que a solução ataca a base toda, não um nicho. *(Seção 9.3)*

**4. "De onde vem o saldo capturável de R$ 18 mil por cliente do cenário neutro?"**
Da distribuição real da Reservinha: o último saldo por cliente tem mediana de **R$ 15,0 mil** (p25 R$ 3,8 mil, p75 R$ 49,5 mil) — os três cenários (10/18/28k) cobrem exatamente essa faixa. *(Célula "Âncora 2")*

**5. "A conversão de 20–50% do Pix→PJ para crédito é realista? Tem limite para isso?"**
Tem: **89% do volume de Pix→PJ de 2025Q4 caberia nos limites de crédito já aprovados** dos clientes — a conversão é restrita por adoção, não por capacidade de crédito. *(Célula "Âncora 1")*

**6. "Por que a meta de carteira digital (14% → 70%) se o campo Wallet é constante no dataset?"**
Porque declaramos isso: o Radar 2 do notebook mostra que os campos de canal são constantes do gerador — usamos o **nível atual** (14%) como ponto de partida de uma **meta de produto**, nunca como tendência observada; a tese do Cartão Digital é prospectiva, por desenho estrutural do Pix.

**7. "Quem investe não é mais fiel? Isso não sustenta o Saldo Vivo?"**
Testamos: hoje **não** — retenção de 95,2% vs 95,6% e gasto idêntico. É o argumento a favor: o lock-in de investimento **não existe** na base, e é exatamente o laço (cashback → Reservinha → limite) que a solução constrói. *(Célula "Teste de fidelidade")*

**8. "E se a banca perguntar da perda de R$ 1,51M/ano?"**
R$ 216k é o colapso do intercâmbio de cartão (baseline 2024Q4 em quantidade; com 2023Q4, ~R$ 89k — declaramos a sensibilidade) + R$ 1,29M de intercâmbio que evapora no Pix→PJ (17,9M × 4 × 1,8%, run-rate do Q4). É custo de oportunidade sob o run-rate corrente, com premissas explícitas. *(Seção 14)*

**9. "Mas a Mastercard não sai perdendo com uma solução centrada em Pix?"**
Resposta em duas camadas, nesta ordem: **(a) o princípio** — como advisors, nosso mandato é o resultado do banco, mesmo que custasse algo à Mastercard no curto prazo: um emissor forte é o que sustenta o ecossistema e o volume de todos no longo prazo; **(b) dissolver a premissa** — mas aqui o trade-off nem se coloca: o Pix no Crédito **liquida como transação de crédito nos trilhos do cartão** (é daí que vêm os 1,8% do nosso modelo de receita), o Cartão Digital é agenda pura de tokenização e wallet, e o motor devolve ao cartão o volume que hoje vaza como Pix cego. O banco recupera share **e** os trilhos recuperam volume — e até o Pix que continuar Pix passa a ser visto pelo banco (o dado volta, mesmo quando o intercâmbio não). *Nunca afirmar espontaneamente que "a Mastercard perde" — a concessão é sempre condicional ("mesmo se custasse...").*
