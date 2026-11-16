# BIM04 — Folha de referência: estudo das referências técnicas aplicado à documentação de usuário do RotaFácil

**Leitor:** professor avaliador e equipe do RotaFácil.
**Tarefa:** a partir da entrega da prova ([documentacao-usuario/](documentacao-usuario/README.md)), estudar as referências técnicas do texto de apoio B04-001 e verificar o quanto a entrega as atende.
**Base da auditoria:** os 8 arquivos Markdown de `documentacao-usuario/` e as 8 capturas de tela, no estado de 11/11/2026.
**Método:** (1) leitura das 7 referências em 11/11/2026; (2) checagem automática da estrutura da entrega (títulos, textos alternativos, links, âncoras, tamanho de frases, siglas); (3) leitura crítica. Este estudo **não alterou** a entrega.
**Escala usada:** *Atende* · *Em parte* · *Não atende* · *Não verificado*.

## 1. Resumo: referência → o que exige → resultado

| Referência | Ideia central (paráfrase) | Resultado na entrega |
|---|---|---|
| **Diátaxis** | Há 4 necessidades do leitor (aprender, executar uma tarefa, consultar, compreender) e cada uma pede um tipo de página: tutorial, how-to, referência, explicação. Misturar os tipos é a causa de muita documentação confusa. | **Em parte.** Falta tutorial; vários arquivos misturam how-to, referência e explicação (seção 2.1). |
| **OASIS DITA 1.3** | Conteúdo em tópicos curtos, de um só assunto, compreensíveis sozinhos, classificados por tipo (conceito, tarefa, referência) e reutilizados por composição. | **Em parte.** Tópicos independentes e linkados, mas regras repetidas em vários arquivos (2.2). |
| **Google Technical Writing** | Definir o público; usar termos de forma consistente e definir siglas; voz ativa; frases curtas; listas numeradas para sequências. | **Em parte.** Frases curtas e passos numerados; faltam definição de siglas e padronização de termos (2.3). |
| **WCAG 2.2 / WAI** | Conteúdo perceptível, operável, compreensível e robusto: alternativa textual para imagens, estrutura determinável, links com finalidade clara, idioma declarado. | **Em parte.** Estrutura, textos alternativos e links ok; idioma e leitura por tecnologia assistiva não verificados (2.4). |
| **GOV.UK (necessidades e mapa de experiência)** | Partir de necessidades de usuários reais, escritas como "eu preciso… para que…", com evidência de pesquisa; suposições sem pesquisa devem ser tratadas como suposições. | **Não atende.** Não houve pesquisa; as necessidades vieram do código e do projeto (2.5). |
| **GitHub Docs (README e Markdown)** | README diz o que é, por que serve, como começar, onde pedir ajuda e quem mantém; links relativos; imagens com texto alternativo; âncoras geradas dos títulos. | **Em parte.** Links, âncoras e imagens ok; faltam "onde pedir ajuda / quem mantém" no README e link a partir do README raiz (2.6). |
| **Write the Docs — Docs as Code** | Tratar documentação como código: Git, texto puro, revisão e testes automatizados, no mesmo fluxo do time. | **Em parte.** Está em Git e em texto puro; não há testes automáticos nem revisão registrada (2.7). |

## 2. Auditoria por referência

### 2.1 Diátaxis: o tipo de cada arquivo

| Arquivo | Tipo predominante | Mistura observada |
|---|---|---|
| `README.md` | Explicação + navegação | adequado como porta de entrada |
| `01-primeiros-passos.md` | How-to | tabelas de campos (referência); regras de privacidade (explicação) |
| `02-turista.md` | How-to | tabela de situações da reserva (referência); regras de negócio (explicação) |
| `03-guia.md` | How-to | tabela de campos do roteiro (referência) |
| `04-agencia.md` | How-to | abre com "Como funciona" (explicação) |
| `05-administracao.md` | How-to | tabela de ações (referência) |
| `06-solucao-de-problemas.md` | Referência | coerente: tabelas de mensagem → ação |
| `verificacao.md` | Relatório interno | **público diferente** (equipe), dentro da pasta do usuário final |

**Lacunas:** (a) **não há tutorial**: ninguém conduz uma pessoa nova do cadastro à primeira reserva em um percurso único; (b) o `verificacao.md` mistura público interno com a documentação do usuário, o que o B04-001 pede para separar ("limites público/interno").

### 2.2 DITA: tópicos e reuso

- **Bom:** cada guia abre com "Para quem / Ao final você saberá / Pré-requisito", o que o torna compreensível sozinho.
- **Regras repetidas** (risco de divergir): "a conta/perfil/vínculo não pode mudar com **reservas ativas**" aparece em 4 arquivos (`01`, `03`, `04` e `06`); "o Cadastur **não é conferido** na base oficial" aparece em 3 (`README`, `01`, `05`).
- **Sugestão no espírito da referência:** uma página canônica de regras gerais da conta, linkada pelos guias. O Markdown não tem "mapas" como o DITA; a composição seria feita por links e pelo README.

### 2.3 Google Technical Writing: clareza do texto

| Critério | Medição | Resultado |
|---|---|---|
| Público definido | cada guia declara "Para quem" | Atende |
| Frases curtas | média de 9,8 a 11,3 palavras por frase nos guias 01–05; 3 frases acima de 30 palavras | Atende |
| Voz ativa | busca aproximada por construções passivas nos guias 01–04: 5 ocorrências | Atende |
| Listas | 46 itens numerados para sequências (01–05); listas com marcadores para itens sem ordem | Atende |
| **Termos consistentes** | "atividade" significa duas coisas: o **tipo** (trekking, ciclismo) e a **experiência inteira** ("a atividade começou"); "saída" e "roteiro" também se sobrepõem às vezes | **Não atende** |
| **Siglas definidas** | CPF, CNPJ, UF, GPS e Cadastur aparecem sem expansão na primeira ocorrência | **Não atende** |
| Jargão para o leitor final | "token" aparece uma vez, em `06`, ao citar uma mensagem real do app | Em parte |

*Limite:* a medição de frases e de voz passiva usa expressões regulares simples e é aproximada.

### 2.4 WCAG 2.2: critérios aplicáveis a texto, imagens, tabelas e links

| Critério | Verificação feita | Resultado |
|---|---|---|
| 1.1.1 Conteúdo não textual (A) | 8 de 8 imagens têm texto alternativo (mínimo de 15 caracteres, checado por script). A **qualidade** do texto não foi testada com leitor de tela | Em parte |
| 1.3.1 Informação e relações (A) | 1 título principal por arquivo, nenhum salto de nível, tabelas com linha de cabeçalho | Atende |
| 1.4.1 Uso de cor (A) | situações e alertas são escritos em texto; o aviso usa o símbolo ⚠️ **junto** de texto | Atende |
| 1.4.5 Imagens de texto (AA) | as capturas contêm texto, mas todo o conteúdo importante também está no corpo do guia | Em parte |
| 2.4.2 / 2.4.6 Título e rótulos (A/AA) | cada arquivo tem título descritivo | Atende |
| 2.4.4 Finalidade do link (A) | 0 links com texto genérico ("clique aqui") | Atende |
| 3.1.1 Idioma da página (A) | Markdown não carrega metadado de idioma; o PDF do estudo de caso foi gerado de HTML com `lang="pt-BR"`, mas **não confirmei** o idioma dentro do PDF | Não verificado |
| 1.4.10 Reflow (AA) | tabelas de até 4 colunas, não testadas em tela pequena | Não verificado |
| Contraste das capturas (1.4.3) | não avaliado | Não verificado |

*Limites das fontes:* li parte do texto do WCAG 2.2 (cerca de 40 mil de 270 mil caracteres); o texto literal confirma o 1.1.1, e os demais níveis vêm de resumo e coincidem com o que a especificação define, mas não os conferi linha a linha. A própria especificação afirma que a conformidade não garante acessibilidade total, e os critérios foram escritos para conteúdo web: para Markdown e PDF é preciso aplicar técnicas específicas, que não estudei.

### 2.5 GOV.UK: necessidades de usuário

A entrega foi escrita a partir do código e da visão do projeto, **sem entrevistas nem observação**. A referência trata o que não vem de usuários como suposição a comprovar. Abaixo, as necessidades que a documentação assume, no formato "eu preciso… para que…". **São hipóteses, não achados.**

| # | Perfil | Hipótese de necessidade | Onde a entrega responde | Evidência |
|---|---|---|---|---|
| H1 | Turista | Eu preciso achar um roteiro perto de mim e na minha data, para planejar um fim de semana | `02` seções 1–2 | nenhuma coleta |
| H2 | Turista | Eu preciso saber se o roteiro é acessível, para decidir se posso ir | `02` seção 3 | nenhuma coleta |
| H3 | Turista | Eu preciso saber o que acontece depois de pedir a reserva, para não ficar sem resposta | `02` seções 4–6 | nenhuma coleta |
| H4 | Guia | Eu preciso publicar um roteiro com várias datas sem erro, para receber reservas | `03` seção 2 | nenhuma coleta |
| H5 | Agência | Eu preciso vincular guias sem perder o controle das reservas, para operar com equipe | `04` | nenhuma coleta |
| H6 | Qualquer | Eu preciso saber o que fazer quando uma mensagem de erro aparece, para não desistir | `06` | nenhuma coleta |

**Validação sugerida:** entrevistar ou observar pessoas reais de cada perfil cumprindo as tarefas. A página do GOV.UK não define o tamanho da amostra. Um **mapa de experiência** só faz sentido depois dessa coleta; por isso não foi feito, em linha com o aviso do B04-001 contra inventar uma jornada "real" a partir de persona fictícia.

### 2.6 GitHub: README e Markdown

| Critério | Verificação | Resultado |
|---|---|---|
| Links relativos | todos os links entre arquivos são relativos e existem | Atende |
| Âncoras | as âncoras `#...` foram conferidas pela regra de geração descrita no GitHub (minúsculas, espaços viram hífens, pontuação removida): 0 problemas | Atende |
| Imagens com texto alternativo e caminho relativo | 8 de 8 | Atende |
| README responde "o que é / como começar" | sim, com índice por tarefa | Atende |
| README diz **onde pedir ajuda e quem mantém** | o suporte (`nao.responda.rotafacil@gmail.com`) só aparece em `06`; ninguém é indicado como mantenedor | **Não atende** |
| Descoberta a partir do repositório | o README **raiz** do repositório de docs tem 2 linhas e não aponta para `documentacao-usuario/` | **Não atende** |

### 2.7 Write the Docs: Docs as Code

| Prática citada na referência | Situação no RotaFácil |
|---|---|
| Controle de versão (Git) e texto puro | **Sim**: Markdown em repositório Git |
| Revisão (code review) | **Não registrada** para a documentação |
| Testes automatizados | **Não há** no repositório. A checagem de links e âncoras foi feita por script **fora** do repositório |
| Mesmo fluxo do time de desenvolvimento | **Parcial**: a documentação de usuário está num repositório separado do código; no backend e no frontend existem **ao menos 6 arquivos com o mesmo nome** (por exemplo `ACESSIBILIDADE_ROTEIRO.md`, `ADMINISTRACAO.md`) com **conteúdo diferente** entre os dois repositórios |

A referência cita o benefício de bloquear a entrega de funcionalidade sem documentação; isso não é praticado no projeto. Ela não lista custos, e o custo de manter essa disciplina nesta equipe pequena **não foi avaliado**.

## 3. Melhorias priorizadas

Nenhuma foi aplicada. Esforço: **P** pequeno, **M** médio, **G** grande.

| Prioridade | Melhoria | Referência | Esforço |
|---|---|---|---|
| 1 | Criar o tutorial **"Sua primeira reserva"** (cadastro → busca → reserva → acompanhar), enxuto e sem alternativas | Diátaxis | M |
| 2 | Mover `verificacao.md` para fora da pasta do usuário final (ou rotular como interno) | Diátaxis, B04-001 | P |
| 3 | **Glossário** com siglas e termos; padronizar "atividade" (tipo) × "roteiro" (oferta) × "saída" (data) | Google TW | P |
| 4 | README: acrescentar "onde pedir ajuda" e "quem mantém"; linkar `documentacao-usuario/` no README raiz do repositório | GitHub | P |
| 5 | Página canônica de **regras gerais da conta** (reservas ativas, Cadastur) e trocar as repetições por links | DITA, B04-001 | M |
| 6 | Versionar o script de checagem (links, âncoras, texto alternativo) no repositório e registrar um passo de revisão | Write the Docs | M |
| 7 | Validar H1–H6 com pessoas reais de cada perfil | GOV.UK | G |
| 8 | Decidir com a equipe a fonte única dos 6 documentos duplicados entre backend e frontend | B04-001, DITA | M |

## 4. Limites deste estudo

- Fontes lidas só em parte: WCAG 2.2 (cerca de 15%, ver 2.4); Google Technical Writing (páginas de objetivos, **não** as unidades do curso); Diátaxis (não li as páginas "tutorials-how-to" e "map"); DITA (página base, que é só sumário, mais duas subpáginas; o restante veio de resumo).
- As referências foram lidas em inglês e **parafraseadas**; nada foi copiado.
- Não houve teste com leitores, nem com leitor de tela, nem em dispositivo pequeno.
- A entrega foi avaliada contra boas práticas **de referência**, não contra um padrão obrigatório; "Não atende" indica distância da prática, não erro de conteúdo.
- As medições de frases e voz passiva são aproximadas.

## 5. Fontes consultadas (em 11/11/2026)

- Diátaxis: <https://diataxis.fr/> e páginas `tutorials`, `how-to-guides`, `reference`, `explanation` e `compass`.
- OASIS DITA 1.3, parte Base: <https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/dita-v1.3-os-part1-base.html> e as subpáginas `information-typing` e `topicbenefits`.
- Google Technical Writing: <https://developers.google.com/tech-writing> e `/one`.
- WCAG 2.2 (Recomendação W3C de 12/12/2024): <https://www.w3.org/TR/WCAG22/>; WAI: <https://www.w3.org/WAI/> e visão geral do WCAG.
- GOV.UK: [necessidades do usuário](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) e [mapa de experiência](https://www.gov.uk/service-manual/user-research/creating-an-experience-map).
- GitHub Docs: [sobre READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) e [sintaxe Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- Write the Docs: <https://www.writethedocs.org/guide/docs-as-code/>.
- Texto de apoio B04-001 (fornecido pela disciplina) e [estudo de caso BIM04](estudo-de-caso-bim04.md).
