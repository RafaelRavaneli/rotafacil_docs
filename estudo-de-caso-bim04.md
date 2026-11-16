# BIM04 — Estudo de caso: avaliação do modelo de documentação e proposta de melhoria

**Projeto analisado:** RotaFácil (backend Flask, frontend Flutter, repositório de documentação).
**Modelo avaliado:** documento B04-001 ("Dicas para documentação"): princípios, perguntas prévias, distinção POP × jornada, prompt-base, banco de 12 prompts e checklist de saída.
**Como foi usado:** o modelo guiou a produção da documentação de usuário em `documentacao-usuario/` (8 arquivos Markdown e 8 capturas de tela). A avaliação abaixo vem dessa experiência, não de uma análise teórica.

## 1. Contexto

Antes do trabalho, o projeto já tinha documentação, mas em estado misto:

- `planning/backlog.md` (RF-03) prevê "Login e autenticação via Firebase Auth". O código usa JWT próprio (`services/autenticacao.py`).
- `planning/roadmap.md` deixa agendamento e avaliações para versões futuras. Ambos já estão implementados e testados.
- O README do backend lista 5 módulos; o `app.py` registra 12 blueprints.
- `workflow/gantt.md` e `workflow/kanban.md` têm 0 linhas.

Ou seja, a documentação descrevia o que foi **planejado** como se fosse o que **existe**. É exatamente o problema que o modelo B04-001 diz atacar.

## 2. O que o modelo fez bem (com evidência do projeto)

| Princípio do modelo | O que aconteceu na prática |
|---|---|
| Começar por leitor e tarefa | A documentação foi dividida por perfil (turista, guia, agência, administração) e por tarefa, em vez de por tela. Cada guia diz "Ao final você saberá…". |
| Distinguir definido / implementado / verificado | Obrigou a marcar trechos como **[não verificado]**. Quatro afirmações nasceram assim (telefone opcional, quem responde às reservas, quem pode denunciar avaliações, rótulo do botão de salvar) e foram conferidas no código depois; as que não puderam ser conferidas continuam declaradas como não verificadas. Sem o marcador, teriam ficado como fato. |
| "Aponte contradições; não as resolva silenciosamente" | Gerou a tabela de contradições (roadmap × código, README × código) e a regra de que o código prevalece. |
| Uma fonte canônica por assunto | Evitou repetir regras. O guia da agência aponta para o do guia em vez de copiá-lo. |
| Checklist de saída | Serviu de roteiro de fechamento: links, exemplos, lacunas declaradas. |

O ponto mais valioso foi a combinação "estado + marcador de incerteza": ela transformou revisão em uma lista de itens a fechar.

## 3. Limites encontrados

Quatro situações que o modelo não orientou, e que o projeto exigiu resolver por conta própria.

**3.1 Comportamento condicionado por configuração.**
O modelo tem quatro estados (definido, proposto, implementado, verificado). No RotaFácil há recursos **implementados e testados, mas desligados por padrão**: confirmação de e-mail (`EMAIL_VERIFICATION_ENABLED=false`) e check-in/check-out (`ENABLE_CHECKIN_CHECKOUT=false`). O usuário de uma instalação pode ou não ver esses botões. Nenhum dos quatro estados descreve isso; foi preciso improvisar o texto "pode não aparecer na sua instalação".

**3.2 Deriva entre documentação e código (drift).**
O modelo cita "Docs as Code" apenas como leitura de apoio. Não diz **quando** revisar nem **quem** revisa. O estado inicial do projeto (seção 1) é o resultado típico de uma documentação escrita uma vez e nunca reaberta. Mesmo o trabalho feito aqui sofreu disso: um número que escrevi na primeira versão (13 blueprints) estava errado e só foi corrigido numa releitura (o correto é 12).

**3.3 Testes automatizados validam o código, não o texto.**
O backend tem 148 testes e o frontend 164, todos passando. Isso não garantia nada sobre a documentação. A checagem de links foi feita por script, mas a checagem de que "o botão se chama Adicionar roteiro" foi manual. O modelo pede verificar "links e exemplos", sem separar **que tipo de verificação** sustenta cada afirmação.

**3.4 Evidências visuais e privacidade.**
O banco de prompts tem um item para diagramas, mas nenhum para capturas de tela. Os prints do app continham nome real de pessoas e dados de demonstração. O modelo não trata de anonimização, texto alternativo, nem de como saber se a imagem ainda corresponde à tela.

## 4. Proposta de melhoria

Escolho tratar os pontos **3.1 e 3.3 juntos**, porque têm a mesma raiz: o modelo não registra **de onde vem cada afirmação nem quão forte é a evidência**. Proponho dois acréscimos pequenos.

### 4.1 Um quinto estado: **condicional**

Acrescentar à distinção do modelo:

> **Condicional:** implementado, mas dependente de configuração, plataforma ou permissão. O documento deve dizer **qual** condição e **qual é o valor padrão**.

Exemplo no RotaFácil: "Check-in e check-out — condicional; desligado por padrão (`ENABLE_CHECKIN_CHECKOUT=false`)."

### 4.2 Uma tabela de rastreabilidade ("afirmação → fonte → evidência")

Para cada afirmação que o leitor usará para agir, registrar:

| Afirmação | Fonte | Estado | Tipo de evidência | Data |
|---|---|---|---|---|
| Cancelar só vale para reserva não iniciada | `services/agendamentos.py`, `cancelar_agendamento` | implementado | **lido no código** | 10/11/2026 |
| Só o criador do roteiro responde reservas | `services/trilhas.py`, `_usuario_pode_gerenciar_trilha` | implementado | **lido no código** | 10/11/2026 |
| Login abre a tela Explorar do turista | app local, tela de login | implementado | **executado no app** | 10/11/2026 |
| Link de recuperação vale 30 minutos | texto da tela de recuperação | implementado | **lido na tela** (envio real não testado) | 10/11/2026 |
| Check-in só aparece com a flag ligada | `AppConfig`, `routes/agendamentos_routes.py` | condicional | **lido no código** | 10/11/2026 |

Os tipos de evidência propostos, do mais fraco ao mais forte: *informado pela equipe* → *lido no código/tela* → *coberto por teste automatizado* → *executado no app* → *testado com leitor real*.

### 4.3 Um prompt novo para o banco (nº 13)

```text
Audite a aderência entre [documento] e [código/app na versão X].
Para cada afirmação que orienta uma ação do leitor, informe: fonte
(arquivo e função ou tela), estado (definido, proposto, implementado,
condicional, verificado), tipo de evidência e se há divergência.
Liste primeiro as divergências e as afirmações sem fonte. Não corrija
o documento; proponha as correções para aprovação.
```

### 4.4 Gatilhos de revisão

Revisar o trecho quando mudar: (a) um contrato de API, (b) uma flag de configuração, (c) um texto visível ao usuário, (d) o papel que pode executar uma ação. Isso responde ao ponto 3.2 com um critério simples e verificável.

## 5. Limitações desta avaliação

- É **um único projeto**, de equipe pequena e de curso. Não prova que a melhoria vale para outros contextos.
- A tabela de rastreabilidade tem **custo de manutenção**. Em documentos grandes só compensa para afirmações que levam o leitor a agir ou que envolvem permissão, dinheiro ou dados pessoais.
- Parte da checagem (texto de botões) poderia ser automatizada comparando a documentação com as strings do frontend. Isso **não foi implementado nem testado**; é uma sugestão.
- A proposta **não foi validada com leitores**, o que o próprio modelo recomenda (prompt 12). Esta avaliação vem da experiência de quem produziu a documentação.
- O app foi executado só em modo local, e só o perfil de turista foi percorrido na prática.

## 6. Conclusão

O modelo B04-001 funcionou bem como **método de escrita**: obrigou a separar fato de intenção e expôs lacunas. Ele é menos eficaz como **método de manutenção**, porque não registra de onde vem cada afirmação nem trata comportamento condicionado por configuração. Um quinto estado (*condicional*), uma tabela de rastreabilidade e um prompt de auditoria de aderência cobrem essas duas lacunas com pouco custo adicional.
