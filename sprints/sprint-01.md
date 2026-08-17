# Planejamento e Execução - Sprint 01

Este documento registra o planejamento, a divisão de tarefas, o acompanhamento e a retrospectiva da primeira sprint do projeto Rota-Fácil.

---

## 1. Informações Gerais
* **Nome da Sprint:** Sprint 01: Infraestrutura de Banco de Dados e Serviços Base
* **Período:** 10/05/2026 a 25/05/2026
* **Objetivo da Sprint:** Configurar o ambiente inicial do projeto, estabelecer a conexão segura com o Firebase Firestore, estruturar a arquitetura de rotas com segurança de login JWT, e implementar as regras de negócio de persistência para as coleções de Usuários, Trilhas e Agendamentos.

---

## 2. Sprint Backlog (Tarefas Selecionadas e Divisão de Trabalho)

| ID da Task | Descrição da Tarefa | Responsável | Status Atual | Evidência Vinculada |
| :--- | :--- | :--- | :--- | :--- |
| #001 | Configuração do Firebase Admin SDK e conexão com Firestore | José Lucas | Concluído | `credentials.json` |
| #002 | Desenvolvimento do serviço e validações de Usuários (`users.py`) | José Lucas | Concluído | `services/users.py` |
| #003 | Desenvolvimento do serviço e mapeamento de Trilhas (`trilhas.py`) | José Lucas | Concluído | `services/trilhas.py` |
| #004 | Implementação da lógica de Agendamentos e chaves (`agendamentos.py`) | José Lucas | Concluído | `services/agendamentos.py` |
| #005 | Integração dos serviços no servidor Flask e criação de rotas base | Rafael Ravaneli | Em andamento | `app.py` |
| #006 | Setup do Ambiente Virtual e estrutura inicial do `app.py` | Rafael / Thiago C. | Concluído | `app.py` |
| #007 | Implementação de Hash de Senha e Token JWT | Rafael / Mateus | Concluído | `services/autenticacao.py` |

---

## 3. Critérios de Pronto (Definition of Done - DoD)
Nenhuma tarefa foi movida para "Concluído" no Kanban sem cumprir:
1. **Validação de Dados:** Presença obrigatória de checagem contra dados nulos antes do envio ao banco.
2. **Versionamento Estrito:** Execução de `git pull` antes de abrir frentes de trabalho, para evitar conflitos no repositório.
3. **Persistência Sem Conflitos:** Geração de identificadores exclusivos (`uuid4`) para chaves primárias textuais no Firestore.

---

## 4. Gerenciamento de Riscos e Impedimentos
* **Risco Identificado:** Erros de indentação e escopo de loops no Python que poderiam causar gravações repetidas ou incompletas de dados (como a chave `valor_pago` no agendamento).
  * *Mitigação Utilizada:* Revisão de código interna e ajuste do recuo das linhas de criação de dicionários para rodarem estritamente fora dos laços de repetição.
* **Impedimentos:** Nenhum impedimento técnico travou a execução desta sprint após o alinhamento de rotas.

---

## 5. Rituais Scrum de Fechamento

### Revisão da Sprint (Sprint Review)
* **O que foi demonstrado:** Estrutura física do banco NoSQL no console do Firebase, arquivos da camada `services/` funcionando de forma modular, e uma API RESTful funcional respondendo na porta 5000, com rotas protegidas por criptografia JWT.
* **Feedback do time:** A arquitetura NoSQL por referências de strings isolou bem as responsabilidades, permitindo que o Back-end trabalhe nas rotas HTTP sem necessidade de configurar bancos locais.

### Retrospectiva da Sprint (Sprint Retrospective)
* **O que funcionou bem:** A comunicação sobre versionamento funcionou perfeitamente — o `git pull` executado antes do desenvolvimento de agendamentos confirmou "Already up to date", dando segurança para criar o arquivo sem sobrescrever código alheio.
* **O que podemos melhorar:** Precisão na escrita inicial de escopos de funções em Python, para evitar retrabalhos com erros de sintaxe e indentação em métodos associativos (como o `cancelar_agendamento`); e alinhamento de nomes de variáveis com a equipe de Frontend (Flutter).
* **Plano de Ação para a Sprint 02:** Aplicar rigorosamente a validação de dados desde o primeiro rascunho de código das novas coleções.

---

## 6. Evidências
* **Testes e Validações:** ![Print do Postman mostrando o Token JWT Gerado](../evidences/postman-jwt.png)
* **Histórico de Commits:** _(inserir link do GitHub com os commits desta sprint)_