# Proposta de Solução — Priceless Bank
**Mastercard Challenge 2026 | Data: 13/06/2026**

> Documento derivado do diagnóstico em [`analise-exploratoria.md`](analise-exploratoria.md). Converge as ideias exploradas (Autopilot, rendimento até o débito, relacionamento) em **um único produto pé no chão** e fecha com o **plano de ação para recuperar e ganhar market share** — o foco do desafio.
>
> **Este produto (Priceless Pay) é o Motor** — o passo 1 do ecossistema completo do grupo. Ao final do documento, ele se integra às outras duas frentes (Cartões Digitais e PIX no Crédito) na seção **[O Ecossistema Completo — As 3 Frentes](#o-ecossistema-completo--as-3-frentes-motor--expandir--captar)**.

---

## Convergência: de três propostas para um produto

Nas iterações anteriores chegamos a três frentes. Agora elas viram **um produto só**, mais executável:

- **Sem biometria.** A ideia é forte, mas exigiria uma nova onda de maquininhas — não escala no curto prazo. Trocamos por **pagamento pelo celular sobre trilhos que já existem** (Apple Pay, Google Pay e o app), inovando *em cima* deles.
- **Saldo Vivo:** **todo** o dinheiro do cliente rende por padrão (liquidez diária) e **todo** pagamento varre do saldo que rende, até o último segundo — acaba a conta corrente parada.
- **Motor de decisão com três faixas** — à vista que rende, crédito à vista e **crédito parcelado** (à escolha do cliente, inclusive em valores baixos) — para ser uma solução completa.
- **Score Priceless + cashback** que cresce com o relacionamento e **puxa a adoção de cartões que fazem sentido**.
- Valor que **vale a partir de 1 cartão** (ou até zero, via Saldo Vivo), com modo turbo para quem tem portfólio.
- **Cliente no comando:** preferências personalizam o algoritmo e os benefícios, ele escolhe o nível de automação, e cadastra **metas financiadas pelos próprios benefícios**.

O nome do produto: **Priceless Pay** — a evolução com os pés no chão do "Pague com Você". Em vez de pagar com o rosto, a Helena paga com o celular que já tem, e o banco faz todo o resto acontecer por trás.

---

## Nossa Persona — Helena

**Helena, 52 anos, São Paulo. Renda R$90k/ano. Tem cartões de crédito (Platinum, Black) e débito, e guarda dinheiro na Reservinha.** Rotina: café na padaria toda manhã, almoço perto do trabalho, farmácia, mercado no sábado. **~3 pagamentos por dia**, quase tudo à vista, misturando PIX (o miúdo) e cartão (o maior). É cuidadosa, detesta perder dinheiro à toa, mas **não tem tempo para gerenciar vários cartões nem decidir o melhor jeito de pagar a cada compra.** Hoje ela paga no que está à mão e deixa benefício na mesa.

---

## A Solução — Priceless Pay

### Contexto
A Helena já tem tudo de que precisa para pagar: celular, cartões e PIX. O que falta não é um instrumento novo — é **inteligência por cima do pagamento**. Hoje ela decide na correria (e erra), o dinheiro fica parado na conta corrente rendendo zero, e o fluxo do dia a dia escapa do banco como PIX cego: sem dado, sem receita, sem vínculo. O Priceless Pay resolve isso sem hardware novo.

### Objetivo
Transformar o celular da Helena na **carteira inteligente do Priceless**: ela paga uma vez, simples, pelo Apple/Google Pay ou pelo app, e o banco **escolhe a melhor forma de pagar, mantém o dinheiro rendendo até o último segundo e recompensa cada gasto conforme o relacionamento dela** — **sempre sob as regras que ela definiu**, sem que ela precise pensar no dia a dia.

### Como Funciona — Arquitetura

#### 1. Pagamento pelo celular, sobre trilhos que já existem (pé no chão)
- **Nada de maquininha nova.** A Helena provisiona o Priceless Pay no **Apple Pay / Google Pay** (NFC por aproximação, aceito em terminais que já existem) e usa o **app** para QR/PIX. Isso, por si só, ataca um dado gritante: hoje **85,9% das transações não usam carteira digital** — há um oceano de adoção parada na mesa.
- **A inovação está por trás, não no terminal.** Em vez de a Helena escolher um cartão na carteira, ela carrega **uma única credencial Priceless** (tokenizada). Quando ela aproxima o celular, o **Autopilot decide no backend qual fonte real vai pagar** — crédito, débito ou Reservinha. Um toque, sempre o melhor resultado. Trilho conhecido (NFC/Apple Pay), cérebro novo.

#### 2. Autopilot — o cérebro que sempre paga do jeito ótimo
O Autopilot não escolhe só "o melhor cartão". Ele escolhe a melhor **trilha** de pagamento — e é por isso que entrega valor mesmo para quem tem **um único cartão**. A cada compra ele decide, em milissegundos, entre:
- **À vista que rende** (débito / Saldo Vivo) — o dinheiro rende até o débito;
- **Crédito à vista** (crédito pago integral, sem juros) — mais cashback + proteção + intercâmbio, e o dinheiro rende até a fatura;
- **Crédito parcelado** (quando a Helena escolhe dividir — ver faixa 3 abaixo).

Considerando: **benefício/cashback** no setor, **rendimento e por quanto tempo o dinheiro segue rendendo**, **proteção** (entra **só** quando faz sentido — lojista novo, ticket alto, online — nunca no pãozinho) e o **Score** da Helena.

> **Por que vale com 1 cartão:** mesmo com um único cartão de crédito, ainda existe a decisão "pago no crédito à vista pra ganhar cashback ou à vista do Saldo Vivo pra render?". Com 1 cartão, o Autopilot já otimiza **trilhas**; com vários cartões, ele liga o **modo turbo** e otimiza também entre eles. O Saldo Vivo (item 3) entrega valor até com **zero cartão**.

Depois de pagar, um aviso curto faz a Helena **sentir** o ganho: *"Paguei no Black: +R$2,40 para você."* O ganho que antes era invisível vira percepção de cuidado.

#### 3. Saldo Vivo — todo o dinheiro rende, todo pagamento varre
Aqui está o coração da solução. Hoje a Helena deixa dinheiro parado na conta corrente (rende zero) e separa um pouco na Reservinha. No **Saldo Vivo, a conta corrente parada deixa de existir**: por padrão, **todo o saldo do cliente fica rendendo** em produtos de baixo risco e liquidez diária (Reservinha, Tesouro Selic, CDB com FGC). Cada pagamento — PIX, débito, fatura do crédito, parcela — dispara um **resgate automático no último segundo**. O dinheiro só "materializa" no instante de pagar; até lá, trabalha.

- **Não é o "porquinho/caixinha".** Aquilo é manual e parcial. O Saldo Vivo é **automático, total e invisível**: o cliente não move nem resgata nada — simplesmente paga, e o sistema varre.
- **Só liquidez diária (D+0):** baixo risco, resgate imediato, FGC onde se aplica — encaixe na persona avessa a risco. Um pagamento **nunca falha** por "dinheiro investido": o banco fronta a liquidação e reconcilia por trás, com camada-tampão de liquidez.
- **Quanto mais demora para pagar, mais rende:** no PIX agendado e, sobretudo, no **crédito à vista** (em que o dinheiro rende até o vencimento da fatura, ~30–40 dias), o saldo trabalha por mais tempo. Por isso o Autopilot otimiza também a **duração do rendimento** — empurrando naturalmente para o crédito à vista (mais rendimento p/ cliente + mais intercâmbio p/ banco).
- **Resultado:** pagar à vista deixa de ser a opção que menos rende e passa a ser a que mais rende, e **100% do dinheiro do cliente está sempre trabalhando** — não só a parte poupada.

> **Ativação opt-in** ("ative para seu dinheiro nunca parar"), com mensagem clara de capital preservado + FGC — o que reforça a confiança da persona em vez de minar. O antigo "PIX Turbinado" é apenas um caso particular do Saldo Vivo.

#### 4. Crédito × Débito × Parcelado — como lidamos (o ponto-chave)
Aqui mora a tensão central: **a Helena prefere à vista (72% das compras)**, mas o banco **ganha mais no crédito** (intercâmbio de ~1,8% vs ~0,6% no débito) — e, ao mesmo tempo, **uma parte dos clientes quer e precisa parcelar**, inclusive valores baixos. A solução não pode atender só o à vista: tem que ser **completa**. O Autopilot trabalha com **três faixas**, e a escolha é sempre **do cliente** — o banco só sugere a ótima:

| Faixa | Quando é usada | Benefício p/ Helena | Benefício p/ banco |
|-------|----------------|---------------------|--------------------|
| **À vista que rende** (Débito / Saldo Vivo) | Pagamento imediato, sem fatura, dinheiro rendendo | Zero dívida + rendimento até o débito | Retém AUM, dado, mantém o fluxo no ecossistema |
| **Crédito à vista** (crédito pago integral, sem juros) | Cashback/score torna ótima, ou há risco (proteção) | **Mais cashback** + proteção, ainda **sem dívida** | **Recupera intercâmbio** (1,8%) |
| **Crédito parcelado** (o cliente escolhe dividir) | Quando a Helena **quer** parcelar — de qualquer valor, inclusive baixo | Fôlego no orçamento, no controle dela | Intercâmbio **+ receita de juros/IOF** |

**Duas garantias que tornam a solução completa:**
1. **À vista nunca é imposto.** O "crédito à vista" não é parcelamento: a Helena paga o valor cheio, sem juros, sem dívida — respeitando a preferência dela. O Autopilot calibra o cashback para que o crédito à vista seja, na maioria dos casos, o melhor negócio, migrando suavemente o à-vista-PIX (intercâmbio zero) para o crédito à vista (intercâmbio recuperado), **sem forçar nada**.
2. **Parcelar é sempre uma opção visível e livre.** Em **qualquer** compra — não só nas grandes — a Helena pode tocar em "dividir" e parcelar, mesmo um valor baixo. Pode também **lançar um gasto manualmente** ou **inserir/pagar um novo valor** (um boleto, uma cobrança avulsa) e escolher à vista ou parcelado. O parcelamento fica acessível em 1 toque (não escondido), porém **desligado por padrão** para não empurrar dívida em quem não quer. Para quem quer, vira receita de juros/IOF além do intercâmbio.

Resultado: o perfil à-vista é respeitado, o perfil que precisa de crédito é atendido, e o banco ganha em todas as faixas.

#### 5. Priceless Score + Cashback inteligente
Cashback sozinho não fideliza esse público — mas **cashback que cresce com o relacionamento**, sim. O **Score Priceless** mede o quanto a Helena concentra a vida financeira no banco:

**O que sobe o score:** % do gasto pelo Priceless Pay · saldo mantido no Saldo Vivo (AUM) · adesão ao Saldo Vivo · nº de produtos · pagamento da fatura em dia · tempo de relacionamento.

**O que o score destrava (escalonado):**
- **Cashback maior** nos setores da rotina (Varejo, Alimentação, Tecnologia);
- **Bônus de rendimento** na Reservinha;
- **Perks de relacionamento** (tratamento de cliente regular nos parceiros de bairro — a herança do "Círculo");
- Limites melhores, tarifas menores.

**De onde vem o dinheiro do cashback:** do **próprio intercâmbio recuperado** no crédito à vista + de uma rede de comerciantes parceiros. Quanto mais a Helena concentra → mais o banco fatura → mais cashback volta → mais ela concentra. **Um ciclo que se autofinancia** e que transforma cashback de commodity em recompensa de lealdade.

#### 6. Controle e Personalização — o cliente no comando
O maior risco de adesão não é técnico: é o cliente sentir que **entregou as decisões para um algoritmo**. A persona é avessa a risco e valoriza controle. A virada de posicionamento: o Autopilot **dá mais controle, não menos**. Hoje a Helena não consegue calcular o ótimo 3× por dia — então paga no chute e perde. Com o Priceless Pay ela sai de "pagar no chute" para **"ditar a estratégia e tê-la executada sem falha"**. O lema: **"você no comando, o Autopilot no volante."**

**Preferências que personalizam o algoritmo (Minhas Regras).** A Helena configura uma vez, e isso molda tanto o roteamento quanto os benefícios:
- **Prioridade:** "priorize rendimento" / "priorize cashback" / "priorize proteção".
- **Regras por categoria:** "mercado sempre no débito", "o Black só em viagem", "nunca parcele".
- **Categorias que mais importam para ela:** o cashback é **ponderado** para o que ela valoriza (ex.: mais cashback em viagem e saúde, menos em outras), personalizando o benefício ao máximo.

O Autopilot então **opera dentro das regras dela** — a IA não decide *por* ela, executa *a política dela* com perfeição.

**Escada de confiança (três modos, ela escolhe):** **Manual** (eu escolho; ele só sugere) → **Sugestão** (ele pré-seleciona, eu confirmo/troco em 1 toque) → **Piloto automático** (ele executa, eu reviso depois). Entra em **Sugestão** e sobe para automático quando ela quiser. Nada de salto de fé no dia 1.

**Mais salvaguardas:** override sempre (antes e depois, com reversibilidade na janela crédito↔Saldo Vivo) · **guardrails** ("crédito até R$X sozinho; acima, me pergunte") · **prova + garantia**: relatório mensal auditável "o que o Autopilot fez por você" e a promessa — *se ele algum dia escolher pior do que você teria, cobrimos a diferença*. Para o cético, vira "não tenho nada a perder".

#### 7. Metas — seus benefícios viram seus objetivos
A Helena pode cadastrar **metas** (ex.: "Viagem 2027 — R$8.000", "Reserva de emergência — R$20k", "Trocar o carro"). O diferencial: a meta é alimentada **pelos próprios benefícios que a solução gera** — cashback, rendimento do Saldo Vivo e recompensas são canalizados automaticamente para o objetivo escolhido.

- **"Gaste de forma inteligente pelo Priceless e seu objetivo se financia sozinho":** cada compra otimizada pelo Autopilot empurra a barra de progresso da meta.
- **Não é o porquinho/caixinha:** lá o cliente deposita manualmente. Aqui, **o banco abastece a meta com o valor que ele mesmo gera para o cliente** — o esforço é do algoritmo, não da Helena (ela ainda pode reforçar com aportes, se quiser).
- **Gancho emocional + motor de concentração:** a meta dá um *porquê* para concentrar a vida financeira no Priceless. Quanto mais ela usa, mais rápido a viagem chega → mais ela usa. Vínculo que cashback solto não cria, e que realimenta o ciclo econômico.

### Justificativa
- **Atende o consumo real:** atua nas ~3 transações/dia, no café e no almoço, não numa compra rara.
- **Dá ao perfil o que ele mais quer:** certeza de sair sempre no melhor negócio, sem esforço; dinheiro rendendo até pagar; e reconhecimento crescente — não gamificação de fintech jovem.
- **Resolve o risco de adesão pelo controle:** o cliente define as regras, escolhe o nível de automação e vê tudo auditável — sente que comanda, o que constrói a confiança necessária para aderir.
- **Personaliza ao máximo:** preferências moldam o algoritmo e ponderam os benefícios; metas dão um objetivo concreto financiado pelos próprios benefícios.
- **Resolve a tensão crédito × débito** alinhando cliente (à vista, sem dívida) e banco (intercâmbio), sem coerção.
- **Pé no chão:** roda sobre Apple/Google Pay e PIX — sem novo hardware, sem nova rede de aceitação.
- **Para o banco:** recupera o fluxo que vazava como PIX cego (dado + intercâmbio + AUM) e torna o Priceless o **orquestrador indispensável** da rotina financeira da Helena.

### Exemplo de Uso — um dia com a Helena
> **7h — Padaria.** Café R$8. Helena aproxima o celular (Apple Pay, credencial Priceless). O Autopilot vê que o ótimo é à vista do **Saldo Vivo** (ticket baixo) e varre de lá. Aviso: *"Pago do Saldo Vivo, que rendeu até agora."*
> **12h — Restaurante.** Almoço R$48. O Black dá 5% em restaurantes hoje; o Autopilot roteia no **crédito à vista** (sem parcelar). Aviso: *"+R$2,40 de cashback."* Banco fatura intercâmbio.
> **16h — Farmácia.** Remédio contínuo R$120. A farmácia é parceira; o **score Ouro** da Helena destrava 8% + desconto de cliente regular. Autopilot no crédito à vista. Aviso: *"+R$9,60 e você é cliente regular aqui."*
> **20h — PIX para o encanador (PJ).** R$300. O valor rendeu no **Saldo Vivo** até a liquidação e foi varrido no último segundo; como é lojista novo, o Autopilot ativa a **proteção** automaticamente.
>
> **Fim do mês:** Helena pagou exatamente como sempre — no modo **Sugestão**, com a regra "priorize rendimento" que ela mesma definiu. Recebeu ~R$70 a mais em cashback e rendimento, que foram **direto para a meta "Viagem 2027"** (a barra andou sozinha), viu o dinheiro render até cada pagamento, foi tratada como VIP na própria rotina — e tudo isso passou pelo Priceless, sob as regras dela.
> **Para o banco:** recuperou o fluxo que vazava no PIX, faturou intercâmbio no crédito à vista, **reteve todo o saldo dela como AUM no Saldo Vivo (spread)**, subiu o score (mais concentração) e virou o banco principal da Helena.

### Resultados Esperados (produto)
| Indicador | Hoje | Meta |
|-----------|------|------|
| Adoção de carteira digital na base | ~14% | >60% |
| Fluxo diário capturado no ecossistema Priceless | Vaza como PIX cego | Maioria dos ~35 mil PIX/tri |
| Intercâmbio recuperado (crédito à vista) | ~R$95k/tri | Rumo aos R$382k/tri de oportunidade |
| AUM total (Saldo Vivo) | Em fuga (resgate recorde 2025Q4); só a parte poupada rende | Todo o saldo vira AUM; crescente e estável |

---

## Recuperação de Faturamento — A Perda e a Projeção (3 cenários)

> Tradução da tese em números **defensáveis**, calculados sobre os dados reais em `notebooks/main.ipynb` (Seção 14). Primeiro dimensionamos o tamanho da perda; depois projetamos o que a solução recupera em três cenários.

### Premissas (todas ancoradas nos dados)
| Parâmetro | Valor | Fonte |
|-----------|-------|-------|
| Intercâmbio crédito | 1,8% | Benchmark Mastercard Brasil |
| Intercâmbio débito | 0,6% | Teto regulatório BACEN |
| **Taxa ponderada do portfólio** | **1,60%** | Split real de volume: **83,6% crédito / 16,4% débito** |
| Ticket-base normalizado | R$ 614 | Mediana 2023/2025 (neutraliza a anomalia de ticket de 2024) |
| Base de clientes | 1.960 | `Base_clientes` |
| PIX→PJ (run-rate) | R$ 17,91M/tri (2025Q4) | `Base_pix` (dados limpos: Aprovado=1, Valor>0, Data notna) |

### Parte 1 — Dimensão da perda de faturamento

A inversão cartão→PIX corrói o faturamento de intercâmbio por **dois caminhos**:

| Componente | Cálculo | Perda/ano |
|------------|---------|-----------|
| **1. Colapso do intercâmbio de cartão** | 2024Q4 normalizado (R$ 148,8k/tri) → 2025Q4 real (R$ 94,9k/tri) = **−R$ 53,9k/tri** | **R$ 215,7k** |
| **2. Oportunidade não capturada no PIX→PJ** | R$ 17,91M/tri × 1,60% (intercâmbio que seria faturado se fosse cartão; PIX aprovados efetivos) | **R$ 1.149k** |
| **PERDA TOTAL DE FATURAMENTO** | | **≈ R$ 1,36M/ano** |

> O grosso da perda **não é** a queda do cartão (R$ 216k/ano) — é o **R$ 1,15M/ano de intercâmbio que evapora** porque o consumo migrou para o PIX→PJ, onde o intercâmbio é zero. Em 2025Q4, o banco fatura ~R$ 95k de intercâmbio de cartão enquanto deixa ~R$ 287k/tri na mesa no PIX→PJ. Captura apenas **~25%** do intercâmbio de transação que tem ao seu alcance.

![Dimensão da perda](recuperacao_perda.png)

### Parte 2 — Projeção da solução em 3 cenários

Com a **plataforma gratuita**, a receita-**core** vem de três vias que **não são taxa cobrada do cliente**: **intercâmbio recuperado** (lojista paga), **spread sobre AUM** (Saldo Vivo) e **juros/IOF do parcelado** (só se o cliente escolher parcelar). A **assinatura premium é upside opcional** — fora do core, porque a solução repõe a perda **sem depender dela**. Os cenários variam as alavancas de adesão e conversão:

| Alavanca | Pessimista | Neutro | Otimista |
|----------|:----------:|:------:|:--------:|
| Adesão ao Priceless Pay (% base) | 30% | 50% | 70% |
| Captura do fluxo PIX→PJ | 25% | 45% | 65% |
| Conversão p/ crédito à vista | 30% | 50% | 65% |
| Saldo médio capturável/cliente (Saldo Vivo) | R$ 10k | R$ 18k | R$ 28k |
| % dos adotantes que mantém saldo | 60% | 70% | 80% |
| Spread sobre AUM (a.a.) | 1,0% | 1,5% | 2,0% |
| Penetração do parcelado | 5% | 10% | 15% |
| Margem líquida do parcelado | 4% | 5% | 6% |
| *Assinantes premium (% base) — upside opcional* | *5%* | *12%* | *25%* |

#### Resultado — receita incremental anual (plataforma gratuita)

| Fonte (core grátis) | Pessimista | Neutro | Otimista |
|---------------------|-----------:|-------:|---------:|
| Intercâmbio recuperado | R$ 86,2k | R$ 258,5k | R$ 485,4k |
| Spread sobre AUM | R$ 35,3k | R$ 185,2k | R$ 614,7k |
| Juros/IOF parcelado | R$ 10,7k | R$ 80,6k | R$ 272,5k |
| **CORE (grátis) / ano** | **R$ 132k** | **R$ 524k** | **R$ 1,37M** |
| **% da perda reposta (só com o core)** | **10%** | **38%** | **101%** |
| AUM sob gestão (Saldo Vivo) | R$ 3,5M | R$ 12,3M | R$ 30,7M |
| *(+) Premium opcional (upside)* | *+R$ 29,4k* | *+R$ 70,6k* | *+R$ 176,4k* |
| *Total com upside* | *R$ 162k* | *R$ 595k* | *R$ 1,55M* |

![Projeção dos 3 cenários](projecao_cenarios.png)

#### Metodologia — como cheguei em cada número
Cada cenário é a soma de fórmulas simples; todos os parâmetros estão no notebook (Seção 14) e podem ser auditados.

**As fórmulas:**
1. **Intercâmbio recuperado** = PIX→PJ anual × captura × conversão × 1,60%
2. **Spread sobre AUM** = nº de clientes × adesão × % que mantém saldo × saldo médio × spread
3. **Juros/IOF parcelado** = (PIX→PJ anual × captura × conversão) × penetração do parcelado × margem líquida
4. *(upside)* **Premium** = nº de clientes × % assinantes × mensalidade × 12

**Valores-base (extraídos dos dados):**
- **PIX→PJ anual = R$ 71,66M** → run-rate de 2025Q4 (R$ 17,91M, PIX aprovados efetivos) × 4. Usar só o Q4 é conservador: não projeta o crescimento que já vinha acontecendo (Q3→Q4 foi +47%).
- **Intercâmbio = 1,60%** → calculado do split real de volume (83,6% crédito × 1,8% + 16,4% débito × 0,6%).
- **Nº de clientes = 1.960** (`Base_clientes`).

**De onde vem cada premissa (e por que é defensável):**

| Premissa | Pess / Neutro / Otim | Racional |
|----------|----------------------|----------|
| Adesão ao Pay | 30 / 50 / 70% | Hoje a carteira digital é só 14% da base; o pessimista já **dobra** isso, e uma base affluent engajada comporta 70% |
| Captura do PIX→PJ | 25 / 45 / 65% | Fração do fluxo que passa a transitar pelo app (função da adesão + nudge do Autopilot) |
| Conversão p/ crédito à vista | 30 / 50 / 65% | Eficácia do nudge; teto porque parte fica em débito/Saldo Vivo por preferência |
| Saldo médio/cliente | R$ 10k / 18k / 28k | O neutro = saldo de investimento **já observado** (R$ 17,9k/cliente); o Saldo Vivo ainda captura o ocioso da conta |
| % que mantém saldo | 60 / 70 / 80% | Fração dos adotantes que de fato parqueia saldo no Saldo Vivo |
| Spread sobre AUM | 1,0 / 1,5 / 2,0% | Spread líquido típico de AUM de baixo risco/liquidez diária |
| Penetração parcelado | 5 / 10 / 15% | **Baixa de propósito** — a persona prefere à vista |
| Margem líq. parcelado | 4 / 5 / 6% | Juros/IOF líquidos de funding e risco |

**Exemplo completo — cenário Neutro:**
- Intercâmbio: R$ 71,66M × 45% × 50% × 1,60% = **R$ 258,5k**
- Spread AUM: 1.960 × 50% × 70% × R$ 18k = R$ 12,35M sob gestão × 1,5% = **R$ 185,2k**
- Parcelado: (R$ 71,66M × 45% × 50%) × 10% × 5% = R$ 16,12M × 0,5% = **R$ 80,6k**
- **Core = 258,5 + 185,2 + 80,6 = R$ 524,3k/ano** (38% da perda) · *(+ premium opcional R$ 70,6k)*

#### Defesa das premissas e sensibilidade (a pergunta da banca)
Não defendemos um número pontual — defendemos um **intervalo** e a **robustez da conclusão**. Cada premissa tem três camadas: **âncora interna** (nos dados), **âncora externa** (análogos de mercado) e **conservadorismo** explícito. Exemplo da adesão (30/50/70%):

- **Âncora interna:** a carteira digital hoje é **14%** da base → o pessimista (30%) é só **~2× o atual**, um piso quase garantido com provisionamento ativo. E **73% da base já é digitalmente ativa** (transacionam por cartão / usam PIX) → esse é o **teto realista**, por isso o otimista (70%) ≈ quase todo o público ativo, não "todo mundo".
- **Âncora externa:** o brasileiro adota pagamento digital útil muito rápido (o PIX chegou à maioria dos adultos em ~2 anos; mobile banking tem penetração altíssima). E aqui é **adoção de uma feature numa base que já usa o app** — não aquisição fria.
- **Conservadorismo:** usamos o run-rate do Q4 (sem projetar o crescimento que já vinha) e saldo neutro = saldo de investimento já observado.

**A resposta mais forte é a sensibilidade** (Seção 14.1 do notebook): em vez de pedir confiança no 50%, mostramos a curva inteira.

![Sensibilidade](sensibilidade.png)

- **Isolando só a adesão** (demais alavancas no neutro, captura = adesão): 30% → repõe **25%**; 50% → **41%**; 70% → **58%**. Precisaríamos de **~61% de adesão** para repor 50% só com essa alavanca.
- Os **cenários da tabela combinam a adesão com as outras alavancas** (spread, saldo, conversão) — por isso o otimista chega a 98%/110%. O *heatmap* adesão × spread mostra esse efeito conjunto.
- **A conclusão é robusta:** em **qualquer** ponto razoável da faixa a solução gera receita nova relevante que o banco não tinha. A discussão deixa de ser "o 50% está certo?" e vira "você acredita que batemos X% de adesão numa base que já é 73% digital?".

**Em faturamento absoluto (R$/ano) — Seção 14.2:**

![Adesão × Faturamento e Adesão × Spread](adesao_faturamento.png)

- **Adesão × faturamento** (spread neutro 1,5%, captura = adesão): **30% → R$ 337k · 50% → R$ 561k · 70% → R$ 786k** de receita-core nova por ano. Cresce de forma praticamente linear com a adesão — sem teto à vista.
- **Adesão × spread** (a 50% de adesão): cada **+0,5 p.p. de spread adiciona ~R$ 62k/ano** (1,0% → R$ 500k · 1,5% → R$ 561k · 2,0% → R$ 623k · 2,5% → R$ 685k). Confirma que **adesão e spread são as duas alavancas dominantes** — e ambas são gerenciáveis pelo banco.

### Leitura — a virada de jogo em números
- **A plataforma grátis se sustenta sozinha:** mesmo **sem cobrar nada do cliente**, o core repõe **38% da perda no neutro** e **101% no otimista** — só com intercâmbio + AUM + parcelado.
- **O AUM é a alavanca de maior elasticidade.** No neutro o **spread sobre AUM (R$ 185k)** já rivaliza com o intercâmbio recuperado — receita recorrente e pegajosa que o banco **não tinha antes**. Cada R$ 1k de saldo médio e cada 0,5 p.p. de spread movem a agulha → por isso o **Saldo Vivo é o coração da solução**.
- **A gratuidade puxa a adesão para cima**, e adesão alimenta os dois motores invisíveis (intercâmbio + AUM). Como a diferença pessimista→otimista é ~10×, **trocar mensalidade por adesão é o negócio certo**: o resultado esperado tende ao topo da faixa.
- **Com o upside premium opcional**, o otimista chega a R$ 1,55M (**114% da perda**) — o banco sai **mais lucrativo do que era antes da inversão**, com receita diversificada (AUM + intercâmbio), não refém do volume de cartão.

---

## Plano de Ação — Recuperar e Ganhar Market Share
> **O foco do hackathon.** Market share aqui = **share de valor transacionado** entre os 5 players (Priceless caiu de 33% → 19% em 2025).

### A lógica: por que perdemos e como o Priceless Pay reverte
Perdemos share porque o **valor migrou para o PIX** — que tem intercâmbio zero e sai dos nossos trilhos monetizados — e porque **clientes esfriaram** (87 inativos, 1.018 cartões vencidos, 161 em desinvestimento, 469 cartões nunca usados). O Priceless Pay ataca os três vetores:

1. **Reter o valor no ecossistema** transformando todo o saldo em AUM que rende (Saldo Vivo → AUM + dado), mesmo quando o cliente paga por PIX.
2. **Reconverter valor em receita** migrando à-vista-PIX para crédito à vista (recupera intercâmbio).
3. **Reter e adquirir clientes** pela diferenciação (mais valor transacionado por cliente + novos clientes).

### Fase 0 — Fundação (0–3 meses) · *parar de sangrar*
- Provisionar cartões tokenizados em **Apple/Google Pay** (resolver os 14% de adoção de carteira).
- Lançar o **Saldo Vivo** (todo o saldo rende, todo pagamento varre) → estanca a fuga de AUM na raiz (resgate recorde de R$1.632k em 2025Q4) e dispara o crescimento de AUM.
- **Autopilot v1** com a lógica crédito-à-vista × débito/PIX.
- **Score Priceless v1**.
- **KPIs:** % da base ativa no Priceless Pay; volume de PIX→PJ retido no ecossistema; queda nos resgates.

### Fase 1 — Recuperação (3–6 meses) · *recuperar receita e clientes*
- **Cashback por score** + migração suave de à-vista-PIX → crédito à vista → **recuperar intercâmbio** (alvo: dos ~R$95k/tri rumo aos R$382k/tri de oportunidade).
- **Renovação proativa** dos cartões vencendo e **reativação** dos 469 cartões parados (régua + bônus de 1ª compra).
- **Reconquista** dos 87 inativos e conversão das 85 contas-fantasma (onboarding com missões).
- **Escada de adoção** (ver seção dedicada): ofertas de cartão lastreadas no gasto real para o segmento de 1–2 cartões (49% da base).
- **KPIs:** intercâmbio recuperado; redução de churn; share of wallet por cliente; **cartões ativos por cliente** (não emitidos); cartões reativados/renovados.

### Fase 2 — Expansão (6–12 meses) · *ganhar share*
- **Rede de comerciantes de bairro (Círculo)** → fidelidade de dois lados + aquisição via parceiros.
- **Aquisição** pela diferenciação: *"o único banco onde seu dinheiro rende até a hora de pagar e você sempre paga do melhor jeito."*
- **Captar o público jovem** (18-29 é só 5,9% da base — a faixa que mais adota digital), levando o Priceless Pay como porta de entrada.
- **KPIs:** ganho líquido de market share; AUM total; novos clientes; NPS (mirar o topo, benchmark Lux = 82).

### O segmento de 1 cartão e a escada de adoção (cartões que fazem sentido)
A base é dividida quase ao meio: **530 clientes com 4 cartões (27%)** convivem com **520 clientes com 1 cartão (26,5%)** e 439 com 2 cartões. O Autopilot brilha mais com portfólio — então o segmento de poucos cartões precisa de tratamento próprio. A leitura certa: **isso não é fraqueza, é o combustível do crescimento.** ~959 clientes (49% da base) têm espaço para subir de produto, e cada cartão de crédito ativo a mais alimenta direto o motor de intercâmbio (= market share).

**Piso universal (vale para 0–1 cartão):** Saldo Vivo + Score sustentam valor real sem depender de portfólio. Ninguém fica de fora.

**A escada é puxada pelo valor, nunca empurrada.** O Score mostra ao cliente, com o **gasto real dele**, o que está deixando na mesa — e oferece o cartão **que faz sentido** para o consumo dele:
> *"Você gastou R$1.200 em farmácia no mês. Com o cartão Saúde Priceless, o Autopilot teria devolvido R$96. Quer pedir? Aprovação em 1 toque."*

Isso é o oposto do velho "abra mais uma conta": é cross-sell **lastreado em dado**, alinhado ao perfil avesso a risco (ele só pede quando se paga). Os degraus:
- **1 cartão de débito →** upgrade para um crédito à vista (destrava cashback + intercâmbio sem dívida).
- **1 cartão de crédito →** 2º cartão de **categoria** casado com o setor que ele mais gasta (Varejo, Alimentação ou Tecnologia).
- **2–3 cartões →** completar o leque para o Autopilot ligar o modo turbo.

**Cuidado que não podemos repetir:** a base já tem **469 cartões nunca usados e 1.018 vencidos**. Empurrar *quantidade* sem uso ativo refaz esse erro. Por isso a métrica é **cartões ativos por cliente — não cartões emitidos** — e a campanha de adoção anda junto da régua de ativação/renovação da Fase 1.

### O motor econômico (por que isso vira liderança, não só recuperação)
```
Mais gasto pelo Priceless Pay + todo o saldo no Saldo Vivo
      ↓
Mais crédito à vista (intercâmbio) + 100% do saldo como AUM (spread)
      ↓
Mais cashback e rendimento devolvidos (autofinanciados)
      ↓
Score sobe → cliente concentra ainda mais a vida financeira
      ↓
Mais valor transacionado pelo Priceless = mais market share
      ↺ (o ciclo se realimenta)
```
Cada volta do ciclo **aumenta o valor transacionado intermediado pelo Priceless** — que é exatamente a métrica do market share. Não é uma campanha pontual; é uma máquina de composição.

### Modelo de Receita — plataforma 100% gratuita, e ainda assim lucrativa
A decisão central: **a plataforma é grátis para o cliente.** Sem mensalidade obrigatória, sem anuidade, sem tarifa. Isso parece contraditório com "ser lucrativo", mas não é — basta desfazer uma confusão comum: **o intercâmbio não é uma taxa que o cliente paga.** Ele é pago pelo adquirente (a maquininha do lojista) ao banco emissor, embutido no preço — invisível e sem custo para a Helena. **"Grátis para o cliente" não é "de graça para o banco".**

**Por que escolhemos o grátis:** a adesão é a variável-mestra. Como a diferença entre os cenários é ~10× e é puxada pela adesão (que alimenta intercâmbio + AUM), **cobrar mensalidade custaria mais em adesão do que renderia em assinatura** — trocar ouro por troco. A gratuidade maximiza a adesão e, com ela, os dois motores invisíveis.

**As fontes de receita — nenhuma é taxa de plataforma:**

| Fonte | Quem paga | Papel | No core grátis? |
|-------|-----------|-------|:----------------:|
| **Spread sobre AUM** (Saldo Vivo) | Margem da gestão do saldo (cliente só vê o **rendimento**) | **Motor principal:** 100% do saldo vira AUM | ✅ |
| **Intercâmbio** | Lojista (adquirente) — custo zero p/ o cliente | Motor que financia o cashback | ✅ |
| **Juros/IOF** | Só o cliente que **escolhe** parcelar | Receita do parcelamento | ✅ |
| **Premium "Black"** *(opcional)* | Cliente, se quiser perks extras | Upside; **não necessário** para repor a perda | ⬜ upside |

O **Saldo Vivo muda a escala do modelo:** ao transformar *todo* o saldo do cliente em AUM (não só a parte poupada), o **spread sobre AUM** vira a fonte mais estável e recorrente — e, como é invisível e sem custo para o cliente, **sustenta o modelo gratuito**. As projeções acima mostram que **só o core grátis** já repõe 38% (neutro) a 98% (otimista) da perda.

**O premium é puro upside, opcional.** A "Priceless Pay Black" (cashback máximo, bônus de rendimento, proteção estendida, perks do Círculo) existe para quem quiser pagar por mais — vendida com promessa verificável (*"se paga sozinha"*) —, mas **a tese não depende dela**. É a cereja, não o bolo.

**O diferencial de marca — incentivos alinhados:** *"Os outros bancos ganham quando você gasta demais ou se endivida. Nós ganhamos quando você nos acha úteis — e nunca cobramos de você."* O modelo do consultor *fee-only* trazido para o varejo, agora ainda mais limpo porque a plataforma é grátis. Para a persona desconfiada e que valoriza confiança, é um dos argumentos mais fortes da solução.

---

## O Ecossistema Completo — As 3 Frentes (Motor → Expandir → Captar)

> A proposta final do grupo. O Priceless Pay (todo este documento) é o **Motor**; duas frentes se acoplam a ele formando um ecossistema em **três passos**. Fontes: Parte 2 em [`cartao-digital.md`](cartao-digital.md) · Parte 3 em [`proposta_priceless_bank.md`](proposta_priceless_bank.md). Projeções em `main.ipynb` (Seção 15).

A lógica em três passos — **aditivos, em pools distintos** (sem dupla contagem):

| Passo | Frente | Papel | Pool de receita |
|-------|--------|-------|-----------------|
| **1 · FATURAR** | **Motor — Priceless Pay** | Estancar a perda e recuperar o faturamento | Fluxo PIX→PJ recuperado + AUM (Saldo Vivo) |
| **2 · EXPANDIR LEQUE** | **Cartões Digitais** | Crescer o cartão onde o PIX não entra | Online/CNP + recorrência + internacional |
| **3 · CAPTAR NOVA BASE** | **PIX no Crédito + ataque à LuminaPay** | Adquirir base jovem 18-30 | Novos clientes (juros/spread + intercâmbio) |

### Passo 1 — Faturar (o Motor)
Tudo que está acima neste documento. Recupera o faturamento que a inversão cartão→PIX corrói, via Saldo Vivo + Autopilot + Score. **Papel: defensivo** — para de sangrar e repõe a perda. **Projeção: R$ 132k → R$ 524k → R$ 1,37M/ano** (10% → 101% da perda).

### Passo 2 — Expandir o leque (Cartões Digitais)
**Tese:** parar de brigar pelo presencial (que o PIX já venceu — 3,4× o cartão em 2025Q4) e crescer o cartão nos territórios **PIX-proof**: online/CNP (30% do volume, ~R$ 11M/ano), recorrência (9.262 transações), internacional e carteira digital (hoje só **14%**). 
**Como conecta ao Motor:** usa a **mesma credencial tokenizada**, o **Autopilot** (cashback por canal) e o **Score**. A tokenização/wallet é a *alavanca-mãe* que serve as duas frentes ao mesmo tempo. 
**Projeção** (intercâmbio incremental sobre o volume CNP; crescimento 20% / 45% / 80%): **R$ 40k → R$ 89k → R$ 158k/ano**. *Conservador (usa 1,8%; o prêmio de intercâmbio CNP/internacional é upside). Frente prospectiva — exige piloto/A-B.*

### Passo 3 — Captar nova base (PIX no Crédito + ataque à LuminaPay)
**Tese:** o Motor e o Cartão Digital cuidam da base atual (madura, affluent); falta atacar a lacuna onde a **LuminaPay** cresce — o **público jovem 18-30** (hoje só 5,9% da base). PIX no crédito (regulamentado pelo BC em nov/2025) + cashback progressivo (1%→3%) → Reservinha → limite, com onboarding 100% digital. 
**Como conecta ao Motor:** o cashback cai no **Saldo Vivo/Reservinha**, o **Score** vira limite de PIX-crédito — o mesmo ciclo econômico do Motor, agora alimentando **aquisição**. 
**Projeção** (contas novas 5k / 20k / 50k × gasto anual monetizado × take de intercâmbio+juros líquido de risco): **R$ 0,4M → R$ 3,0M → R$ 13,5M/ano**. *Frente de maior incerteza **e** maior potencial — escalonada em fases trimestrais com validação por piloto (roadmap no doc de origem).*

### Resultado do Ecossistema — receita incremental anual

| Frente | Pessimista | Neutro | Otimista |
|--------|-----------:|-------:|---------:|
| 1 · Motor (faturar) | R$ 132k | R$ 524k | R$ 1,37M |
| 2 · Cartões Digitais (expandir) | R$ 40k | R$ 89k | R$ 158k |
| 3 · PIX Crédito + base jovem (captar) | R$ 400k | R$ 3,00M | R$ 13,50M |
| **TOTAL / ano** | **R$ 0,57M** | **R$ 3,61M** | **R$ 15,0M** |
| **vs. perda anual (R$ 1,36M)** | **42%** | **265%** | **1.102%** |

![Projeção do ecossistema](projecao_ecossistema.png)

**Leitura — de recuperação a crescimento:**
- O **Motor sozinho** estanca a hemorragia (passo defensivo).
- **+ Cartões Digitais** diversifica a receita para o território PIX-proof, sem depender do presencial em queda.
- **+ PIX no Crédito + base jovem** vira a chave: o ecossistema deixa de ser recuperação e passa a **crescimento** — no neutro já gera **2,5× a perda**, no otimista **~10×**, porque adquirir uma nova base (até 50k contas vs. 1.960 atuais) é alavanca de outra ordem de grandeza.
- Os três passos compartilham a **mesma infraestrutura** (Saldo Vivo, Score, credencial tokenizada, ciclo econômico). Não são três produtos soltos — são **um ecossistema** em que cada passo alimenta o seguinte.

---

## Por Que Nos Torna Líderes
Os concorrentes disputam o **meio de pagamento** (PIX no crédito, invest→limite). O Priceless Pay disputa algo que ninguém olha: **a inteligência que serve a rotina do cliente e o ciclo econômico que se autofinancia por trás dela.** A Helena não escolhe um meio de pagamento — ela escolhe um banco que cuida do dinheiro dela melhor do que ela mesma cuidaria, em cada um dos ~3 pagamentos do dia.

> **Mensagem para a banca:** "Perdemos share porque o valor fugiu para um cano que não monetizamos e não enxergamos. O Priceless Pay traz esse valor de volta — sem maquininha nova, sobre o Apple Pay e o PIX que já existem — escolhendo sempre o melhor jeito de pagar, fazendo o dinheiro render até o último segundo e recompensando a lealdade num ciclo que se paga sozinho. Não competimos pelo instrumento. Competimos pela rotina do cliente. E quem é dono da rotina recupera o share — e depois lidera."

### Roteiro sugerido para o pitch de 5 min
1. **Diagnóstico (1 min):** valor migrou para o PIX cego → caímos de 33% para 19%.
2. **A virada (1,5 min):** Priceless Pay — pagamento pelo celular + Autopilot (sob as regras do cliente) + Saldo Vivo + Score + metas, com o exemplo da Helena.
3. **Crédito × Débito e o modelo de receita (1 min):** plataforma **100% grátis** e ainda lucrativa — reconvertemos valor em receita **sem forçar dívida e sem cobrar nada do cliente** (intercâmbio invisível + spread de AUM + incentivos alinhados).
4. **Os números e o plano (1,5 min):** a inversão custa **~R$ 1,36M/ano**; a solução repõe **44% (neutro)** a **114% (otimista)** disso — no otimista, o banco sai mais lucrativo do que antes da inversão. Fechar com Fase 0 → 1 → 2 e o ciclo econômico.

---

## Conclusão — Os Ganhos do Ecossistema

O Priceless Bank perdeu 14 p.p. de share porque o valor migrou para um cano que ele não monetizava nem enxergava, custando **~R$ 1,36M/ano** de faturamento. A resposta do grupo não é um produto — é um **ecossistema em três passos** que transforma a perda em plataforma de crescimento.

**O que ganhamos, por ator:**

- **Cliente:** paga sempre do melhor jeito sem esforço (Autopilot), com o dinheiro rendendo até o último segundo (Saldo Vivo), **zero taxa/anuidade**, controle total, metas que se pagam sozinhas e proteção — e, na frente jovem, entra num banco que já o trata como investidor desde o 1º PIX. Para a Helena, ≈ **R$ 70/mês** a mais no bolso.
- **Banco:** recupera **intercâmbio + dado + AUM** (Motor), diversifica para receita PIX-proof e recorrente (Cartões Digitais) e **adquire uma nova base inteira** atacando a LuminaPay onde ela é forte (PIX no Crédito). Tudo sobre a **mesma infraestrutura** e o **mesmo ciclo econômico autofinanciado**.

**Os ganhos, em números (receita incremental/ano):**

| Cenário | Total ecossistema | vs. perda (R$ 1,36M) | Tradução |
|---------|------------------:|:--------------------:|----------|
| Pessimista | **R$ 0,57M** | 42% | já estanca boa parte da sangria, sem cobrar nada do cliente |
| Neutro | **R$ 3,61M** | **265%** | repõe a perda **2,6×** — vira lucro novo |
| Otimista | **R$ 15,0M** | **1.102%** | crescimento de outra ordem (nova base jovem) |

**A trajetória de market share:** o passo 1 **estanca** a queda (33% → 19%), o passo 2 **defende** o terreno que sobra, e o passo 3 **reataca** — recuperando share da base atual e **conquistando** o público jovem da LuminaPay. De *perder share* para *liderar*.

> **Tese final para a banca:** "Não entregamos um produto, entregamos um ecossistema. O Motor para de sangrar e recupera o faturamento; os Cartões Digitais crescem onde o PIX não entra; e o PIX no Crédito captura a base jovem que estávamos perdendo. Três passos, uma infraestrutura, um ciclo que se autofinancia — e que leva o Priceless de *perder share* a *recuperá-lo e voltar a crescer*."

---

*Documento gerado em 13/06/2026 | Atualizado em 14/06/2026 | Base: [`analise-exploratoria.md`](analise-exploratoria.md) e `main.ipynb` (Seções 14–15)*
*Visualizações: `docs/recuperacao_perda.png`, `docs/projecao_cenarios.png`, `docs/sensibilidade.png`, `docs/adesao_faturamento.png`, `docs/projecao_ecossistema.png`*
*Fluxo visual completo (Persona → Problema → Solução → Benefícios → Resultado): [`docs/fluxo-solucao.excalidraw`](fluxo-solucao.excalidraw) — abrir em [excalidraw.com](https://excalidraw.com) ou na extensão Excalidraw do VS Code*
