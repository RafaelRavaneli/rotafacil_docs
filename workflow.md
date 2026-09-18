# Workflow Funcional da Equipe RotaFácil

[cite_start]Nossa equipe adotou um fluxo de trabalho baseado no **GitHub Flow**, que é ideal para entregas contínuas e revisão colaborativa antes da integração do código[cite: 86, 87].

## Fluxo de Trabalho (Passo a Passo)
1. **Criação de Tarefas:** Toda nova funcionalidade é registrada no Trello (Kanban).
2. **Criação de Branches:** O desenvolvedor cria uma branch a partir da `main` usando o padrão `tipo/nome-da-tarefa` (ex: `feat/autenticacao-jwt` ou `fix/erro-login`).
3. **Padrão de Commits:** Utilizamos mensagens claras e descritivas (ex: "Feat: Adiciona criptografia de senhas no auth.py").
4. **Pull Request (PR):** Ao finalizar, o desenvolvedor abre um PR no GitHub solicitando o merge para a `main`.
5. [cite_start]**Revisão de Código:** Outro membro da equipe revisa o código para garantir a qualidade[cite: 82].
6. [cite_start]**Merge e Atualização:** Após aprovação, o merge é realizado e a documentação é atualizada[cite: 83, 85].

## Evidências Reais
* **Exemplo Completo Executado:** O desenvolvedor Rafael (Backend) assumiu a Issue de Autenticação, criou a branch `feat/jwt`, realizou os commits das bibliotecas e abriu o PR. O desenvolvedor Thiago Carvalho revisou o código e aprovou o merge.
* [INSERIR LINK DO PULL REQUEST AQUI]
* ![Print do Histórico de Commits](../evidences/historico-commits.png)