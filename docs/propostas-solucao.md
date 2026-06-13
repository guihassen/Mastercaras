# Proposta de Solução — Priceless Bank
**Mastercard Challenge 2026 | Data: 13/06/2026**

> Documento derivado do diagnóstico em [`analise-exploratoria.md`](analise-exploratoria.md). Converge as ideias exploradas (Autopilot, rendimento até o débito, relacionamento) em **um único produto pé no chão** e fecha com o **plano de ação para recuperar e ganhar market share** — o foco do desafio.

---

## Convergência: de três propostas para um produto

Nas iterações anteriores chegamos a três frentes. Agora elas viram **um produto só**, mais executável:

- **Sem biometria.** A ideia é forte, mas exigiria uma nova onda de maquininhas — não escala no curto prazo. Trocamos por **pagamento pelo celular sobre trilhos que já existem** (Apple Pay, Google Pay e o app), inovando *em cima* deles.
- **Saldo Vivo:** **todo** o dinheiro do cliente rende por padrão (liquidez diária) e **todo** pagamento varre do saldo que rende, até o último segundo — acaba a conta corrente parada.
- **Motor de decisão com três faixas** — à vista que rende, crédito à vista e **crédito parcelado** (à escolha do cliente, inclusive em valores baixos) — para ser uma solução completa.
- **Score Priceless + cashback** que cresce com o relacionamento e **puxa a adoção de cartões que fazem sentido**.
- Valor que **vale a partir de 1 cartão** (ou até zero, via Saldo Vivo), com modo turbo para quem tem portfólio.

O nome do produto: **Priceless Pay** — a evolução com os pés no chão do "Pague com Você". Em vez de pagar com o rosto, a Helena paga com o celular que já tem, e o banco faz todo o resto acontecer por trás.

---

## Nossa Persona — Helena

**Helena, 52 anos, São Paulo. Renda R$90k/ano. Tem cartões de crédito (Platinum, Black) e débito, e guarda dinheiro na Reservinha.** Rotina: café na padaria toda manhã, almoço perto do trabalho, farmácia, mercado no sábado. **~3 pagamentos por dia**, quase tudo à vista, misturando PIX (o miúdo) e cartão (o maior). É cuidadosa, detesta perder dinheiro à toa, mas **não tem tempo para gerenciar vários cartões nem decidir o melhor jeito de pagar a cada compra.** Hoje ela paga no que está à mão e deixa benefício na mesa.

---

## A Solução — Priceless Pay

### Contexto
A Helena já tem tudo de que precisa para pagar: celular, cartões e PIX. O que falta não é um instrumento novo — é **inteligência por cima do pagamento**. Hoje ela decide na correria (e erra), o dinheiro fica parado na conta corrente rendendo zero, e o fluxo do dia a dia escapa do banco como PIX cego: sem dado, sem receita, sem vínculo. O Priceless Pay resolve isso sem hardware novo.

### Objetivo
Transformar o celular da Helena na **carteira inteligente do Priceless**: ela paga uma vez, simples, pelo Apple/Google Pay ou pelo app, e o banco **escolhe automaticamente a melhor forma de pagar, mantém o dinheiro rendendo até o último segundo e recompensa cada gasto conforme o relacionamento dela** — sem que ela precise pensar.

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

### Justificativa
- **Atende o consumo real:** atua nas ~3 transações/dia, no café e no almoço, não numa compra rara.
- **Dá ao perfil o que ele mais quer:** certeza de sair sempre no melhor negócio, sem esforço; dinheiro rendendo até pagar; e reconhecimento crescente — não gamificação de fintech jovem.
- **Resolve a tensão crédito × débito** alinhando cliente (à vista, sem dívida) e banco (intercâmbio), sem coerção.
- **Pé no chão:** roda sobre Apple/Google Pay e PIX — sem novo hardware, sem nova rede de aceitação.
- **Para o banco:** recupera o fluxo que vazava como PIX cego (dado + intercâmbio + AUM) e torna o Priceless o **orquestrador indispensável** da rotina financeira da Helena.

### Exemplo de Uso — um dia com a Helena
> **7h — Padaria.** Café R$8. Helena aproxima o celular (Apple Pay, credencial Priceless). O Autopilot vê que o ótimo é à vista do **Saldo Vivo** (ticket baixo) e varre de lá. Aviso: *"Pago do Saldo Vivo, que rendeu até agora."*
> **12h — Restaurante.** Almoço R$48. O Black dá 5% em restaurantes hoje; o Autopilot roteia no **crédito à vista** (sem parcelar). Aviso: *"+R$2,40 de cashback."* Banco fatura intercâmbio.
> **16h — Farmácia.** Remédio contínuo R$120. A farmácia é parceira; o **score Ouro** da Helena destrava 8% + desconto de cliente regular. Autopilot no crédito à vista. Aviso: *"+R$9,60 e você é cliente regular aqui."*
> **20h — PIX para o encanador (PJ).** R$300. O valor rendeu no **Saldo Vivo** até a liquidação e foi varrido no último segundo; como é lojista novo, o Autopilot ativa a **proteção** automaticamente.
>
> **Fim do mês:** Helena pagou exatamente como sempre. Mas recebeu ~R$70 a mais em cashback e rendimento, viu o dinheiro render até cada pagamento, foi tratada como VIP na própria rotina — e tudo isso passou pelo Priceless.
> **Para o banco:** recuperou o fluxo que vazava no PIX, faturou intercâmbio no crédito à vista, **reteve todo o saldo dela como AUM no Saldo Vivo (spread)**, subiu o score (mais concentração) e virou o banco principal da Helena.

### Resultados Esperados (produto)
| Indicador | Hoje | Meta |
|-----------|------|------|
| Adoção de carteira digital na base | ~14% | >60% |
| Fluxo diário capturado no ecossistema Priceless | Vaza como PIX cego | Maioria dos ~35 mil PIX/tri |
| Intercâmbio recuperado (crédito à vista) | ~R$100k/tri | Rumo aos R$358k/tri de oportunidade |
| AUM total (Saldo Vivo) | Em fuga (resgate recorde 2025Q4); só a parte poupada rende | Todo o saldo vira AUM; crescente e estável |

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
- **Cashback por score** + migração suave de à-vista-PIX → crédito à vista → **recuperar intercâmbio** (alvo: dos ~R$100k/tri rumo aos R$358k/tri de oportunidade).
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

### Modelo de Receita — "sem taxas para o cliente", e ainda assim lucrativo
O ponto de partida é desfazer uma confusão comum: **o intercâmbio não é uma taxa que o cliente paga.** Ele é pago pelo adquirente (a maquininha do lojista) ao banco emissor, embutido no preço — invisível e sem custo para a Helena. As taxas que *ela* enxerga são outras: anuidade e tarifas. Isso permite uma jogada que parece contraditória, mas não é: **zerar todas as taxas que o cliente vê e, ao mesmo tempo, continuar faturando.**

**Quatro fontes, e as duas maiores são invisíveis para o cliente:**

| Fonte | Quem paga | Visível p/ o cliente? | Papel |
|-------|-----------|----------------------|-------|
| **Spread sobre AUM** (Saldo Vivo) | Ninguém diretamente — é a margem da gestão do saldo | Não — o cliente só vê o **rendimento** dele | **Motor invisível principal:** 100% do saldo vira AUM |
| **Intercâmbio** (crédito à vista/parcelado) | Lojista (adquirente) | Não — custo zero p/ o cliente | Motor invisível que financia o cashback |
| **Assinatura premium** ("Priceless Pay Black") | Cliente, **por opção** | Sim — e **se paga sozinha** | Receita recorrente de alta margem |
| **Juros/IOF** (só se o cliente escolher parcelar) | Cliente que opta por crédito | Sim, e por escolha | Receita do parcelamento |

O **Saldo Vivo muda a escala do modelo:** ao transformar *todo* o saldo do cliente em AUM (não só a parte poupada), o **spread sobre AUM** vira uma fonte estável e recorrente que pode igualar ou superar o intercâmbio — e, como é invisível e sem custo para o cliente, **permite ser ainda mais agressivo no "zero taxa"**.

**A manchete para o cliente: zero anuidade, zero tarifa.** Acaba a anuidade dos cartões premium — a taxa que a Helena realmente sente. O intercâmbio segue por trás, bancado pelo lojista, financiando o cashback dela. Ela percebe um banco "sem taxas"; o banco continua faturando.

**A assinatura é opcional e autofinanciada.** A "Priceless Pay Black" entrega cashback máximo, bônus de rendimento, proteção e os perks do Círculo — e é vendida com uma promessa verificável: *"custa R$X/mês e o Autopilot te devolve, em média, mais do que isso."* Para um perfil que detesta perder dinheiro, assinar algo que comprovadamente se paga é decisão fácil (lógica Amazon Prime / Costco).

> **Por que NÃO vivemos só de assinatura:** eliminar o intercâmbio para cobrar tudo na mensalidade significaria substituir uma receita que **não custa nada ao cliente** (~R$23–82/cliente/mês, conforme a captura do fluxo PIX→PJ) por uma mensalidade alta, criando atrito de adesão contra concorrentes que parecem "gratuitos". Jogaríamos fora o dinheiro do lojista para cobrar do cliente. O híbrido fica com os dois.

**O diferencial de marca — incentivos alinhados:** *"Os outros bancos ganham quando você gasta demais ou se endivida. Nós ganhamos quando você nos acha úteis."* É o modelo do consultor *fee-only* trazido para o varejo — e, para a nossa persona desconfiada e que valoriza confiança, é um dos argumentos mais fortes da solução.

---

## Por Que Nos Torna Líderes
Os concorrentes disputam o **meio de pagamento** (PIX no crédito, invest→limite). O Priceless Pay disputa algo que ninguém olha: **a inteligência que serve a rotina do cliente e o ciclo econômico que se autofinancia por trás dela.** A Helena não escolhe um meio de pagamento — ela escolhe um banco que cuida do dinheiro dela melhor do que ela mesma cuidaria, em cada um dos ~3 pagamentos do dia.

> **Mensagem para a banca:** "Perdemos share porque o valor fugiu para um cano que não monetizamos e não enxergamos. O Priceless Pay traz esse valor de volta — sem maquininha nova, sobre o Apple Pay e o PIX que já existem — escolhendo sempre o melhor jeito de pagar, fazendo o dinheiro render até o último segundo e recompensando a lealdade num ciclo que se paga sozinho. Não competimos pelo instrumento. Competimos pela rotina do cliente. E quem é dono da rotina recupera o share — e depois lidera."

### Roteiro sugerido para o pitch de 5 min
1. **Diagnóstico (1 min):** valor migrou para o PIX cego → caímos de 33% para 19%.
2. **A virada (1,5 min):** Priceless Pay — pagamento pelo celular + Autopilot + Saldo Vivo + Score, com o exemplo da Helena.
3. **Crédito × Débito e o modelo de receita (1 min):** como reconvertemos valor em receita **sem forçar dívida e sem cobrar taxa do cliente** (intercâmbio invisível + assinatura autofinanciada + incentivos alinhados).
4. **Plano de ação e o ciclo econômico (1,5 min):** Fase 0 → 1 → 2 e o motor que recupera e depois ganha market share.

---

*Documento gerado em 13/06/2026 | Base: [`analise-exploratoria.md`](analise-exploratoria.md) e `main.ipynb`*
