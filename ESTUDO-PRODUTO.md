## 1. Diagnóstico do produto entregue

### 1.1 Qual é o produto e qual problema ele resolve?

O RotaFácil é uma aplicação web que conecta turistas, guias e agências responsáveis por atividades em trilhas. Seu objetivo é concentrar em um único sistema a consulta de trilhas, o cadastro dos participantes, os agendamentos, os favoritos, os dados de perfil e a comunicação entre os usuários.

O turista pode localizar atividades e registrar reservas. O guia pode manter seus dados profissionais e responder a convites. A agência pode cadastrar trilhas, administrar informações e convidar guias. O sistema reduz a dependência de contatos e controles separados para organizar essas atividades.

### 1.2 Quem usa, quem mantém e quem recebe as versões?

Os usuários do produto são turistas, guias e agências. Cada perfil possui permissões e uma área própria. O login solicita somente e-mail e senha, e o tipo da conta retornado pelo backend define para qual área o usuário será encaminhado. CPF e CNPJ são validados no cadastro, conforme o perfil, e não durante o login.

A manutenção ainda depende da equipe que desenvolveu o projeto. Essa equipe administra os repositórios, executa testes, configura credenciais e prepara as versões. O cliente, o avaliador e os futuros usuários recebem a versão considerada estável pela equipe. Ainda não existe uma pessoa formalmente definida como responsável por release, publicação, atendimento ou recuperação de falhas.

### 1.3 Como o produto é executado hoje?

O produto é executado localmente no Windows. O backend utiliza Python e Flask e é iniciado na porta 5000. O frontend utiliza Flutter Web e é aberto no Chrome, normalmente na porta 8080. Para o modo conectado, o frontend recebe a URL da API e a indicação `USE_BACKEND=true`.

```powershell
cd D:\projetos\rotafacil_backend
.\venv\Scripts\python.exe app.py
```

Em outro terminal:

```powershell
cd D:\projetos\rotafacil_frontend
flutter run -d chrome --web-port=8080 --dart-define=USE_BACKEND=true --dart-define=API_BASE_URL=http://127.0.0.1:5000
```

A persistência utiliza Cloud Firestore. O produto também possui integrações com Firebase Cloud Messaging, ImgBB e SMTP. Essas integrações dependem de credenciais e configurações locais que não são incluídas no Git. Não existe endereço público de produção comprovado nesta versão.

### 1.4 Quais passos ainda dependem de ação manual?

Atualmente, uma pessoa da equipe precisa:

- preparar as versões corretas de Python, Flutter e dependências;
- criar o ambiente virtual do backend;
- configurar `.env`, chave JWT e credencial administrativa do Firebase;
- configurar Firebase Web, chave VAPID, ImgBB e conta de e-mail;
- iniciar backend e frontend em terminais separados;
- executar os testes e conferir os resultados;
- gerar a compilação web;
- conferir se frontend e backend usam contratos compatíveis;
- testar CORS, autenticação e serviços externos;
- decidir quando uma branch pode ser integrada;
- registrar problemas, versão apresentada e retorno do cliente.

Também não existe um processo automatizado e documentado de publicação, rollback ou restauração. A integração das branches com `develop` e `main` depende de comandos e revisão manual.

### 1.5 O que pode dar errado em uma nova entrega?

Uma alteração no contrato da API pode quebrar o frontend mesmo quando os dois projetos compilam separadamente. Um novo campo, nome de rota ou regra de autorização pode deixar login, agendamento, conversa ou convite incompatível.

Também podem ocorrer falhas por versão de dependência, configuração de CORS, variável de ambiente ausente, credencial expirada, permissão incorreta no Firebase ou indisponibilidade de ImgBB e SMTP. Uma alteração enviada diretamente à branch estável pode substituir trabalho anterior ou introduzir regressão sem revisão.

Em uma publicação futura, outros riscos serão o uso do servidor Flask em modo de desenvolvimento, ausência de monitoramento, falta de separação entre dados de teste e produção e inexistência de rollback registrado. Logs sem tratamento também podem expor JWT, documentos ou informações privadas de usuários.

### 1.6 Que evidência mostra que o produto está pronto hoje?

As evidências mostram que existe um **MVP técnico executável localmente**, e não um serviço de produção já homologado. A versão analisada é identificada por:

- frontend `1.1.0+2`, branch `desenvolvimento/frontend-integracao`, commit `776ba352a2f84e3567bc531f63da25b33bb389d7`;
- backend na branch `feature/planejamento-trilha`, commit `88acb9accc21d27a8fc6c26e6a9e85cb8abcd097`;
- 16 testes automatizados aprovados no backend;
- 23 testes conectados aprovados e 3 ignorados no frontend;
- 21 testes locais aprovados e 5 ignorados no frontend;
- `flutter analyze` executado sem problemas;
- compilação web concluída com configuração Firebase/VAPID;
- tela de login registrada, com entrada por e-mail e senha.

Os fluxos de autenticação, perfis, trilhas, agendamentos, favoritos, conversas, suporte e convites estão presentes no código e nos contratos. Porém, recebimento real de push, envio real de e-mail, upload externo e demonstração formal ao cliente ainda precisam de homologação específica.

### 1.7 O que deve ser documentado para outra pessoa manter o sistema?

Outra pessoa precisaria encontrar, em um local único:

- arquitetura do frontend, backend e serviços externos;
- versões mínimas de Flutter, Dart e Python;
- lista de variáveis de ambiente, finalidade e responsável por cada segredo;
- procedimento seguro para obter, substituir e revogar credenciais;
- contratos da API e regras de autorização por perfil;
- estrutura das principais coleções do Firestore;
- comandos de instalação, execução, teste e compilação;
- critérios para integrar uma branch e identificar uma versão;
- procedimento de publicação, verificação e rollback;
- política de backup e recuperação dos dados;
- localização dos logs e procedimento para investigar falhas;
- problemas conhecidos e integrações que exigem validação manual;
- contato ou papel responsável por manutenção, publicação e atendimento.

Sem essas informações, a continuidade depende da memória dos integrantes atuais.

## 2. Leitura do futuro do produto

### 2.1 Ponto 1 — Branches protegidas e GitHub Actions

**Problema que poderia resolver:** os testes e a revisão dependem de execução manual. Uma mudança pode ser integrada em `develop` ou `main` sem que frontend, backend e contratos tenham sido verificados.

**Benefício para o cliente ou para a equipe:** pull requests, proteção de branches e checks automáticos criariam um critério visível para aceitar uma mudança. O pipeline poderia executar os testes do Flask, `flutter analyze`, testes do Flutter e uma compilação web. Isso diminuiria regressões e manteria um histórico das validações.

**Custo, risco ou dificuldade:** seria necessário criar e manter workflows YAML, fixar versões das ferramentas e separar testes que dependem de serviços externos. Um pipeline mal configurado pode passar sem testar o modo conectado ou pode expor informações em logs. Recursos de proteção também podem variar conforme o plano e a visibilidade do repositório.

**Informação ainda necessária:** tempo de execução dos testes, estratégia de cache, testes que exigem Firebase, permissões dos repositórios, regras disponíveis no plano do GitHub e responsável por revisar cada pull request.

**Aplicação indicada:** começar com integração contínua, sem publicação automática. Somente mudanças com checks aprovados devem ser candidatas à integração.

### 2.2 Ponto 2 — Ambiente de homologação reproduzível e container da API

**Problema que poderia resolver:** a execução atual depende da preparação manual da máquina. Versões diferentes de Python, bibliotecas ou configurações podem produzir resultados diferentes. Também não há um ambiente separado para testar antes de uma futura produção.

**Benefício para o cliente ou para a equipe:** um container da API documentaria runtime e dependências. Um ambiente de homologação com dados fictícios permitiria testar login, agendamento, conversa, convites e integrações antes de disponibilizar uma versão aos usuários. A equipe poderia reproduzir o mesmo backend em diferentes máquinas e em um serviço gerenciado.

**Custo, risco ou dificuldade:** a equipe precisaria aprender Docker, criar e atualizar o `Dockerfile`, escolher um servidor Python de produção e tratar portas, CORS e credenciais. Firebase, Firestore, ImgBB e SMTP continuariam sendo serviços externos; o container não elimina essa dependência. Manter homologação também pode gerar custo de nuvem.

**Informação ainda necessária:** provedor e região, orçamento disponível, política de dados de teste, origem do frontend, limites de memória e timeout, forma de injetar secrets, rota de saúde e procedimento de rollback.

**Aplicação indicada:** containerizar primeiro apenas a API e publicar manualmente em homologação. A automação do deploy deve acontecer somente depois que esse processo for repetido e documentado.

### 2.3 Ponto 3 — Monitoramento, recuperação e documentação operacional

**Problema que poderia resolver:** quando o backend deixar de rodar no terminal local, a equipe não verá imediatamente uma exceção, falha de autenticação ou indisponibilidade de integração. Hoje também não há procedimento registrado para voltar à versão anterior ou recuperar o serviço.

**Benefício para o cliente ou para a equipe:** logs estruturados e alertas permitiriam descobrir erros de API, aumento de latência e falhas de serviços externos. Uma documentação operacional com versão, responsável, rollback e recuperação reduziria o tempo de indisponibilidade e facilitaria a entrada de outro mantenedor.

**Custo, risco ou dificuldade:** logs e métricas criam custo, precisam de retenção e podem gerar alertas inúteis. Registrar conteúdo demais pode expor CPF, CNPJ, JWT, senhas ou conversas. Backup sem teste também pode transmitir uma segurança que não existe.

**Informação ainda necessária:** quais indicadores representam saúde do produto, quem recebe alertas, tempo aceitável de indisponibilidade, período máximo de perda de dados, política de retenção, recursos de backup do Firestore e obrigações de privacidade.

**Aplicação indicada:** começar por rota de saúde, logs de erro sem dados pessoais, taxa de respostas 5xx e registro de cada versão. Depois, testar rollback e restauração com dados fictícios antes de definir o processo como concluído.

## 3. Ordem recomendada de adoção

| Momento | Ação | Evidência de conclusão |
|---|---|---|
| Agora | Proteger branches, usar pull requests e executar testes no GitHub Actions | Pull request bloqueado quando um teste falhar e liberado após checks aprovados |
| Depois | Criar container da API e ambiente separado de homologação | Outra pessoa inicia a versão documentada e executa o roteiro sem usar dados de produção |
| Mais adiante | Automatizar publicação, monitorar e testar rollback/recuperação | Histórico de deploy, alerta validado e retorno comprovado à versão anterior |

Essa ordem prioriza o risco existente. Primeiro, impede-se que código não validado seja integrado. Depois, torna-se o ambiente reproduzível e cria-se um local seguro para testar. Por último, automatizam-se publicação e recuperação quando a equipe já conhece o processo manual.

## 4. Conclusão

O RotaFácil está pronto como MVP técnico local: possui versão identificada, código versionado, testes aprovados, compilação web e funcionalidades centrais implementadas. Ele ainda não está pronto para continuar vivo sem participação da equipe original, porque publicação, configuração, validação externa e recuperação dependem de conhecimento manual.

A continuidade do produto não exige implantar todas as práticas DevOps imediatamente. O passo mais útil é transformar os testes atuais em verificações automáticas de pull request. Depois, a equipe pode criar homologação reproduzível e documentação operacional. Monitoramento, deploy automatizado e infraestrutura como código fazem sentido quando a primeira publicação estiver estabilizada e houver responsáveis definidos.

## 5. Referências às evidências da entrega principal

- [`ENTREGA-PRODUTO-ROTAFACIL-SEM-PRINTS.docx`](./ENTREGA-PRODUTO-ROTAFACIL-SEM-PRINTS.docx) — versão, execução, recursos, resultados técnicos e limitações.
- [`FOLHA-DE-REFERENCIA-DEVOPS.md`](./FOLHA-DE-REFERENCIA-DEVOPS.md) — pesquisa sobre branches, GitHub Actions, ambientes, containers, nuvem, OpenTofu e monitoramento.
- Frontend: https://github.com/RafaelRavaneli/rotafacil_frontend — branch `desenvolvimento/frontend-integracao`, commit `776ba35`.
- Backend: https://github.com/RafaelRavaneli/rotafacil_backend — branch `feature/planejamento-trilha`, commit `88acb9a`.
- Documentação: https://github.com/RafaelRavaneli/rotafacil_docs.

## 6. Referências técnicas

- GITHUB. *Managing protected branches*. Disponível em: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches. Acesso em: 25 set. 2026.
- GITHUB. *Workflows*. Disponível em: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows. Acesso em: 25 set. 2026.
- DOCKER. *What is Docker Compose?* Disponível em: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/. Acesso em: 25 set. 2026.
- GOOGLE CLOUD. *What is Cloud Run*. Disponível em: https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run. Acesso em: 25 set. 2026.
- GOOGLE CLOUD. *Cloud Logging overview*. Disponível em: https://docs.cloud.google.com/logging/docs/overview. Acesso em: 25 set. 2026.
