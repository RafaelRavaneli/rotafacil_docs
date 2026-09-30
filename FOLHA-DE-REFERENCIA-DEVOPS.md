# FOLHA DE REFERÊNCIA DEVOPS — ROTAFÁCIL

**Trabalho individual**  
**Estudante:** Rafael Ravaneli Schiavon  
**RA:** 101772-21  
**Disciplina e turma:** Projeto Trainee – ADS 2  
**Produto analisado:** RotaFácil  
**Data:** 25/09/2026

## 1. Contexto do produto analisado

O RotaFácil é uma aplicação web desenvolvida em Flutter/Dart com uma API em Python/Flask. O backend utiliza autenticação JWT, integra-se ao Cloud Firestore e possui serviços externos para imagens, recuperação de senha e notificações Firebase. O código está separado em repositórios de frontend, backend e documentação no GitHub.

Atualmente, a execução comprovada é local: a API Flask é iniciada em um terminal e o frontend Flutter Web é iniciado em outro. A equipe criou branches específicas para desenvolver sem alterar diretamente as branches estáveis. Os testes são executados por comandos locais, e ainda não existe pipeline automatizado nem ambiente público de homologação ou produção confirmado.

Essa situação motivou a pesquisa sobre versionamento protegido, integração contínua, separação de ambientes, containers, publicação em nuvem, infraestrutura como código e monitoramento. O objetivo é escolher práticas compatíveis com um MVP acadêmico, sem criar uma estrutura maior do que a equipe consegue manter.

## 2. Lista comentada de referências

### Referência 1 — Branches protegidas e revisão antes da integração

1. **Autor ou organização:** GitHub.
2. **Título do material:** *Managing protected branches*.
3. **Link:** https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** versionamento, workflow, pull requests e proteção de branches.
6. **Ideia principal compreendida:** uma regra de proteção pode impedir exclusões e `force push`, exigir pull request, revisão e verificações de status antes de permitir integração em uma branch importante.
7. **Relação com o RotaFácil:** frontend e backend já utilizam branches de desenvolvimento. Proteger `main` e `develop` diminuiria o risco de alguém enviar código incompleto diretamente ou sobrescrever uma versão estável.
8. **Decisão ou risco analisado:** a referência fortaleceu a decisão de integrar mudanças por pull request. O risco é criar regras rígidas demais para uma equipe pequena ou depender de recursos que variam conforme o plano e a visibilidade do repositório. A regra inicial deve exigir testes e, quando houver disponibilidade, uma revisão simples.

### Referência 2 — Automação de testes com GitHub Actions

1. **Autor ou organização:** GitHub.
2. **Título do material:** *Workflows*.
3. **Link:** https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** GitHub Actions, integração contínua e pipelines.
6. **Ideia principal compreendida:** um workflow é um processo automatizado descrito em YAML dentro de `.github/workflows`. Ele pode ser disparado por eventos do repositório e executar tarefas como compilar e testar pull requests.
7. **Relação com o RotaFácil:** hoje os testes de Flask e Flutter dependem de alguém lembrar de executá-los localmente. Um workflow poderia rodar os testes do backend, `flutter analyze`, os testes do frontend e uma compilação web a cada pull request.
8. **Decisão ou risco analisado:** a automação deve começar apenas com validação de código, sem publicação automática. Isso produz retorno rápido com baixo risco. É necessário investigar o tempo de execução, o cache das dependências, os testes que dependem de Firebase e a forma de substituir integrações externas por mocks ou ambiente de teste.

### Referência 3 — Ambientes e segredos de publicação

1. **Autor ou organização:** GitHub.
2. **Título do material:** *Deployment environments*.
3. **Link:** https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** ambientes separados, homologação, aprovação e segredos.
6. **Ideia principal compreendida:** ambientes como `development`, `staging` e `production` podem ter regras, branches autorizadas, histórico de implantação e segredos próprios. Um job só recebe os segredos do ambiente quando as condições configuradas são atendidas.
7. **Relação com o RotaFácil:** a aplicação depende de URLs, credenciais Firebase, chave JWT e configurações diferentes. Separar homologação e produção evita que um teste use dados ou credenciais reais por engano.
8. **Decisão ou risco analisado:** a equipe deve criar primeiro uma configuração de homologação e manter produção sem implantação automática. Antes disso, precisa verificar quais recursos de aprovação estão disponíveis no plano do GitHub e criar projetos Firebase separados ou coleções claramente isoladas.

### Referência 4 — Armazenamento seguro de credenciais no pipeline

1. **Autor ou organização:** GitHub.
2. **Título do material:** *Secrets*.
3. **Link:** https://docs.github.com/en/actions/concepts/security/secrets
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** proteção de credenciais em pipelines.
6. **Ideia principal compreendida:** informações sensíveis podem ser armazenadas como segredos de organização, repositório ou ambiente e só ficam disponíveis ao workflow quando referenciadas explicitamente. A documentação também recomenda conceder o menor conjunto possível de permissões.
7. **Relação com o RotaFácil:** `firebase-key.json`, chave JWT, senha de aplicativo de e-mail e chave do ImgBB não podem ser incluídos no Git. Em uma futura implantação, esses valores devem ser fornecidos pelo ambiente e limitados ao serviço que realmente precisa deles.
8. **Decisão ou risco analisado:** nenhuma credencial privada será colocada no YAML ou no repositório. Mesmo com secrets, logs e scripts ainda precisam ser revisados para não imprimir valores transformados. A configuração pública do aplicativo Firebase não deve ser confundida com a chave administrativa privada.

### Referência 5 — Containers e execução reproduzível

1. **Autor ou organização:** Docker.
2. **Título do material:** *What is Docker Compose?*
3. **Link:** https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** containers, Dockerfile e Docker Compose.
6. **Ideia principal compreendida:** uma imagem empacota a aplicação e suas dependências; o container é a instância em execução. O Compose descreve serviços e configurações em um arquivo YAML e permite iniciar uma aplicação composta por mais de um serviço de forma padronizada.
7. **Relação com o RotaFácil:** o backend exige Python e dependências específicas, enquanto o frontend precisa ser compilado e servido. Containers podem reduzir diferenças entre máquinas e documentar a versão do runtime usada pela API.
8. **Decisão ou risco analisado:** o primeiro experimento deve containerizar somente a API e executar seus testes. Colocar frontend, API e serviços externos em um Compose completo agora aumentaria a complexidade, e Firestore, Firebase Cloud Messaging, ImgBB e SMTP continuariam externos. Também é necessário verificar tamanho das imagens, tempo de build, portas, CORS e montagem segura das credenciais.

### Referência 6 — Publicação gerenciada em nuvem

1. **Autor ou organização:** Google Cloud.
2. **Título do material:** *What is Cloud Run*.
3. **Link:** https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** nuvem e publicação de aplicações em containers.
6. **Ideia principal compreendida:** o Cloud Run é uma plataforma gerenciada capaz de executar serviços HTTP a partir de código ou imagem de container. Ele fornece endpoint HTTPS e pode ajustar a quantidade de instâncias de acordo com a demanda. Seu sistema de arquivos local é descartável, portanto dados permanentes devem ficar em um serviço externo.
7. **Relação com o RotaFácil:** a API Flask é HTTP e já usa Firestore como persistência externa. Isso combina com um serviço sem estado no Cloud Run e evita administrar uma máquina virtual. A proximidade com Firebase e Firestore também simplifica identidade e observabilidade.
8. **Decisão ou risco analisado:** Cloud Run parece mais adequado que uma VM para o primeiro ambiente de homologação do backend. Ainda é preciso adaptar a aplicação para ouvir a porta fornecida pelo ambiente, retirar o modo `debug`, usar um servidor de produção, medir inicialização, definir região, IAM, CORS, limites, orçamento e tratamento seguro de credenciais.

### Referência 7 — Infraestrutura como código e revisão do plano

1. **Autor ou organização:** OpenTofu.
2. **Título do material:** *Command: plan*.
3. **Link:** https://opentofu.org/docs/cli/commands/plan/
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** infraestrutura como código e OpenTofu.
6. **Ideia principal compreendida:** `tofu plan` mostra as ações que seriam realizadas sem aplicá-las. Um plano salvo pode ser utilizado posteriormente na aplicação, mas o resultado precisa ser revisto novamente porque o estado real pode mudar entre o planejamento e a execução.
7. **Relação com o RotaFácil:** serviços, contas de serviço, permissões e configurações de nuvem poderiam ser descritos em arquivos versionados. Isso facilitaria repetir homologação e produção e revisar alterações antes de modificar recursos reais.
8. **Decisão ou risco analisado:** a referência mostrou que infraestrutura como código também cria responsabilidade sobre estado, permissões e mudanças destrutivas. O RotaFácil ainda não possui infraestrutura de produção estável; por isso, OpenTofu deve entrar somente depois do primeiro deploy manual documentado. Antes da adoção, a equipe precisa comparar OpenTofu e Terraform, estudar armazenamento remoto e bloqueio do estado e executar apenas `plan` em um projeto de teste.

### Referência 8 — Logs, pesquisa e alertas

1. **Autor ou organização:** Google Cloud.
2. **Título do material:** *Cloud Logging overview*.
3. **Link:** https://docs.cloud.google.com/logging/docs/overview
4. **Data de acesso:** 25/09/2026.
5. **Assunto estudado:** monitoramento, logs, alertas e recuperação de incidentes.
6. **Ideia principal compreendida:** o Cloud Logging centraliza coleta, armazenamento, pesquisa e análise de logs. Entradas podem gerar métricas e alertas, ajudando a localizar falhas e acompanhar tendências.
7. **Relação com o RotaFácil:** depois da publicação, erros de login, falhas de Firestore, upload, e-mail e push não estarão visíveis no terminal do desenvolvedor. Logs estruturados com horário, rota, estado e identificador de correlação ajudariam a investigar problemas sem registrar senha, token ou documento pessoal.
8. **Decisão ou risco analisado:** o monitoramento inicial deve ser simples: logs de aplicação, taxa de respostas 5xx, latência e uma verificação de saúde. O risco é armazenar dados pessoais ou gerar custo e ruído excessivos. Antes de ativar alertas, é necessário definir retenção, campos proibidos, responsáveis e limites úteis.

## 3. Estudo escrito

### 3.1 Necessidade que motivou a pesquisa

A principal necessidade do RotaFácil é transformar uma versão que funciona na máquina da equipe em uma versão que possa ser repetida, testada e publicada com menos risco. O frontend e o backend já possuem funcionalidades relevantes e testes, mas a execução ainda depende de comandos manuais, arquivos locais e conhecimento de quem configurou a máquina. Também há branches de desenvolvimento que precisam ser unidas sem perder trabalho.

Esse cenário cria quatro problemas relacionados. Primeiro, uma alteração pode ser integrada sem que todos os testes sejam executados. Segundo, configurações locais podem produzir resultados diferentes em outra máquina. Terceiro, não há um ambiente de homologação claramente separado de uma futura produção. Quarto, quando a API sair do computador do desenvolvedor, será necessário descobrir falhas por logs e alertas, e não apenas observando o terminal.

A pesquisa foi orientada pela seguinte pergunta: **qual conjunto mínimo de práticas DevOps aumenta a confiança na entrega do RotaFácil sem impor à equipe a manutenção de uma plataforma complexa?**

### 3.2 O que as referências explicam

A documentação do GitHub mostrou que o primeiro controle pode acontecer antes da publicação. Branches protegidas e pull requests criam um ponto de revisão. Status checks permitem impedir que uma mudança seja integrada quando um teste automatizado falha. No caso do RotaFácil, isso é mais útil no momento do que automatizar imediatamente a produção, porque o risco atual está na junção do frontend e do backend e na repetição dos testes.

Os workflows do GitHub Actions transformam os comandos que já existem em uma verificação repetível. Para o backend, o pipeline pode instalar `requirements.txt` e executar a suíte de testes. Para o frontend, pode instalar a versão definida do Flutter, executar `flutter analyze` e os testes que não dependem de serviços reais. Uma compilação web sem credenciais privadas também pode confirmar que o projeto continua gerando artefato. A documentação de secrets esclareceu que credenciais não devem ser escritas no workflow. Isso é especialmente relevante porque o RotaFácil usa uma conta administrativa do Firebase, chave JWT, SMTP e ImgBB.

A documentação de ambientes acrescentou uma separação que ainda não existe no produto. Homologação deve usar dados fictícios e credenciais próprias. Produção deve ter acesso mais restrito e, quando o processo estiver maduro, aprovação antes do deploy. Essa leitura modificou a ideia de que bastaria manter arquivos `.env` diferentes na máquina: os arquivos ajudam localmente, mas não oferecem histórico de implantação, política de acesso nem proteção centralizada.

Docker explica como empacotar runtime e dependências em uma imagem. Isso pode resolver a instalação manual do Python e reduzir a diferença entre a máquina de desenvolvimento e o ambiente de nuvem. O Compose facilita aplicações com vários serviços, mas não transforma automaticamente serviços externos em containers. Firestore, Firebase Cloud Messaging, ImgBB e SMTP continuariam sendo serviços externos. Para o RotaFácil, a containerização mais útil começa na API Flask, que é a parte com runtime e servidor bem definidos.

O Cloud Run aparece como alternativa de publicação gerenciada. A API já trabalha com requisições HTTP e persiste dados no Firestore, portanto não depende do disco local do servidor. Em comparação com uma máquina virtual, um serviço gerenciado reduz tarefas de sistema operacional, atualização e escalonamento. Isso não elimina trabalho: é preciso usar um servidor Python adequado à produção, retirar `debug`, configurar porta, identidade, CORS, região, limites e orçamento.

OpenTofu acrescenta reprodutibilidade à própria infraestrutura. A leitura sobre `plan` mostrou que a equipe pode revisar o efeito esperado antes de aplicar uma mudança. Porém, também ficou claro que o plano depende do estado atual e deve ser conferido novamente antes da aplicação. Para um MVP que ainda não possui infraestrutura estabilizada, automatizar recursos cedo demais pode apenas codificar decisões que continuam mudando.

Por fim, Cloud Logging mostra que publicar não encerra a entrega. Uma aplicação disponível precisa permitir investigação. Logs pesquisáveis, métricas baseadas em logs e alertas podem revelar erros de API e aumento de latência. O cuidado é não registrar CPF, CNPJ, senha, JWT, chave Firebase ou conteúdo privado das conversas.

### 3.3 Alternativas encontradas e diferenças

Para integração do código, comparei dois caminhos. O primeiro é continuar executando testes manualmente e integrar branches por comandos Git. Ele exige pouca configuração, mas depende de memória, disciplina e disponibilidade de cada integrante. O segundo é usar pull requests, proteção de branch e GitHub Actions. Ele exige criar e manter arquivos YAML, mas registra o resultado dos testes e torna o critério de integração visível para toda a equipe.

Para execução, comparei a preparação manual da máquina com a containerização. A preparação manual é conhecida pela equipe e facilita depuração, porém cada pessoa instala suas próprias versões. Um container fornece ambiente mais previsível, mas exige Docker, criação de imagem, decisão sobre servidor de produção e tratamento de credenciais. O Compose só deve ser usado se realmente simplificar a inicialização conjunta; não há motivo para simular em containers os serviços gerenciados que o projeto já utiliza.

Para publicação do backend, comparei três possibilidades: continuar somente localmente, criar uma máquina virtual ou usar Cloud Run. A execução local tem custo de infraestrutura praticamente nulo, mas não oferece acesso contínuo ao cliente. A VM oferece controle amplo, porém transfere à equipe tarefas de sistema operacional, servidor, TLS, disponibilidade e atualização. Cloud Run reduz essa administração e combina com uma API HTTP sem estado, em troca de dependência da plataforma, limites próprios e custos que precisam ser acompanhados.

Para infraestrutura como código, comparei adoção imediata com adoção posterior. OpenTofu ou Terraform poderiam descrever recursos desde o início, mas a equipe ainda precisa descobrir a configuração correta por meio de uma primeira homologação. A alternativa posterior registra manualmente o primeiro deploy, estabiliza as decisões e então transforma os passos repetidos em código. Essa ordem reduz a chance de automatizar uma arquitetura provisória.

### 3.4 Alternativa adequada ao momento atual

A alternativa mais adequada agora é implantar **integração contínua antes de entrega contínua**. O próximo incremento deve proteger `develop` e `main`, usar pull requests e executar testes com GitHub Actions. A publicação permanece manual enquanto a equipe prepara um ambiente de homologação.

Essa escolha oferece valor imediato ao cliente porque reduz regressões nos fluxos já implementados. O esforço é moderado: os comandos de teste existem e precisam ser convertidos em jobs. O risco também é controlável, pois o pipeline inicialmente apenas lê o código, instala dependências e valida; ele não altera recursos externos.

Em seguida, a equipe pode containerizar a API e publicá-la manualmente em um serviço gerenciado, preferencialmente um ambiente de homologação no Cloud Run. O frontend pode continuar sendo compilado separadamente e hospedado em solução adequada a conteúdo web. A publicação automática só deve ser adicionada depois que o processo manual estiver documentado, repetido e acompanhado por logs.

OpenTofu fica para uma etapa posterior, quando região, serviços, nomes, permissões e política de segredos estiverem estáveis. Nesse momento, o primeiro uso deve gerar `plan` em um projeto de teste, sem `apply` automático.

### 3.5 O que precisa ser testado antes da adoção

Antes de exigir os checks no GitHub, é necessário executar o workflow em branches de teste e confirmar:

- versão do Flutter e do Python compatível com os projetos;
- cache sem esconder falhas de dependência;
- testes que conseguem rodar sem credencial de produção;
- tempo e consumo do pipeline;
- resultado de falha visível no pull request;
- ausência de valores sensíveis nos logs;
- diferença entre testes locais e conectados.

Antes de adotar Docker e Cloud Run, é preciso validar:

- imagem da API com servidor de produção e sem modo `debug`;
- leitura da porta fornecida pelo ambiente;
- conexão segura com Firestore e demais serviços;
- CORS para a origem de homologação;
- rota de saúde e encerramento correto;
- tempo de inicialização e comportamento após escala para zero;
- limites de CPU, memória, timeout e concorrência;
- custo máximo e alertas de orçamento;
- rollback para uma revisão anterior.

Antes de usar OpenTofu, a equipe deve estudar estado remoto, bloqueio, permissões mínimas, separação entre projetos e proteção contra exclusão acidental. O `plan` precisa ser revisado por outra pessoa, e a primeira aplicação deve ocorrer apenas em infraestrutura descartável de teste.

### 3.6 Afirmação fortalecida, modificada ou abandonada

A afirmação fortalecida foi: **automatizar os testes antes de unir as branches reduz o risco de quebrar a versão demonstrável**. A documentação de branches protegidas e workflows mostrou como transformar essa intenção em um critério obrigatório e registrado.

A afirmação modificada foi: **Docker resolveria todo o ambiente do produto**. Após a leitura, a formulação correta é que Docker pode padronizar o runtime e as dependências da API, enquanto Firestore, Firebase Cloud Messaging, ImgBB e SMTP continuam externos e precisam de configuração própria.

A sugestão abandonada foi: **adotar Kubernetes desde já para preparar o crescimento**. A IA apresentou Kubernetes como possibilidade de escalabilidade, mas essa indicação foi rejeitada porque o RotaFácil ainda é um MVP, não possui tráfego público comprovado e a equipe primeiro precisa estabilizar testes, container e homologação. Um serviço gerenciado como Cloud Run atende melhor ao momento atual com menor carga operacional.

Também foi corrigida a ideia de fazer deploy automático em produção desde o primeiro workflow. A leitura sobre environments e secrets mostrou que o caminho mais seguro é separar CI de CD: primeiro validar pull requests; depois criar homologação; só então estudar deploy com aprovação e credenciais restritas.

## 4. Registro do uso da IA

### Pergunta feita à IA

> Quais referências técnicas oficiais ajudam a comparar testes manuais com GitHub Actions, execução local com Docker e publicação de uma API Flask em uma máquina virtual ou serviço gerenciado?

A pergunta foi usada para levantar palavras-chave e localizar documentação oficial. As decisões deste trabalho foram escritas depois da leitura das fontes listadas.

### Informação conferida diretamente na fonte

Na documentação do GitHub, conferi que workflows ficam em `.github/workflows`, são executados a partir de eventos e podem compilar e testar pull requests. Também conferi que ambientes podem restringir branches, controlar segredos e exigir regras antes da execução de um job de implantação.

Na documentação do Cloud Run, conferi que serviços recebem endpoint HTTPS, executam código em containers, podem ajustar instâncias e utilizam sistema de arquivos descartável. Isso confirmou que os dados permanentes do RotaFácil devem continuar em um serviço externo como Firestore.

### Sugestão da IA rejeitada ou corrigida

Rejeitei a sugestão de introduzir Kubernetes agora. Embora seja uma tecnologia válida, a complexidade de cluster, manifests, rede, observabilidade e operação não corresponde ao estágio atual do RotaFácil. Também corrigi a sugestão de colocar todas as dependências no Docker Compose: Firebase, Firestore, ImgBB e SMTP não devem ser tratados como containers locais obrigatórios para representar o ambiente real.

### Alteração causada pela leitura

Antes da pesquisa, eu considerava criar containers e automatizar a publicação como um único passo. Depois da leitura, alterei o planejamento para quatro etapas:

1. proteger branches e automatizar análise e testes;
2. criar um ambiente de homologação com segredos separados;
3. containerizar e publicar manualmente a API, acompanhada por logs;
4. automatizar deploy e infraestrutura somente depois de repetir e estabilizar o processo.

Essa mudança deixa o plano mais compatível com a capacidade atual da equipe e cria evidências em cada etapa antes de aumentar a automação.

## 5. Síntese da decisão para a prova

| Momento | Ação | Evidência esperada | Principal risco |
|---|---|---|---|
| Agora | Pull requests, proteção de branches e GitHub Actions para testes | Checks aprovados antes da integração | Workflow diferente do ambiente local |
| Depois | Homologação separada, container da API e publicação manual no Cloud Run | URL de teste, roteiro executado e logs consultáveis | Configuração de credenciais, CORS e custo |
| Mais adiante | Deploy aprovado, alertas e infraestrutura com OpenTofu | Histórico de deploy, `plan` revisado e rollback testado | Mudança destrutiva, estado incorreto ou automação excessiva |

## 6. Referências bibliográficas

GITHUB. *Deployment environments*. GitHub Docs. Disponível em: https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments. Acesso em: 25 set. 2026.

GITHUB. *Managing protected branches*. GitHub Docs. Disponível em: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches. Acesso em: 25 set. 2026.

GITHUB. *Secrets*. GitHub Docs. Disponível em: https://docs.github.com/en/actions/concepts/security/secrets. Acesso em: 25 set. 2026.

GITHUB. *Workflows*. GitHub Docs. Disponível em: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows. Acesso em: 25 set. 2026.

DOCKER. *What is Docker Compose?* Docker Docs. Disponível em: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/. Acesso em: 25 set. 2026.

GOOGLE CLOUD. *Cloud Logging overview*. Google Cloud Documentation. Disponível em: https://docs.cloud.google.com/logging/docs/overview. Acesso em: 25 set. 2026.

GOOGLE CLOUD. *What is Cloud Run*. Google Cloud Documentation. Disponível em: https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run. Acesso em: 25 set. 2026.

OPENTOFU. *Command: plan*. OpenTofu Documentation. Disponível em: https://opentofu.org/docs/cli/commands/plan/. Acesso em: 25 set. 2026.
