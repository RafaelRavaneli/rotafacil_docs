# RotaFácil — Especificação funcional, telas e integração

**Data:** 01/10/2026  
**Finalidade:** orientar a criação das telas e a integração Flutter–Flask.  
**Base:** arquivos locais de frontend, rotas e serviços do backend, backlog e visão do produto.  
**Escopo:** turista, guia, agência e dependências administrativas.

## 1. Como utilizar este documento

Cada função tem um identificador para relacionar telas, tarefas, contratos e testes. Os estados significam:

- **Integrado:** há interface e chamadas de API; não equivale a homologação real.
- **Parcial:** existe parte do fluxo, mas faltam dados, integração ou definição.
- **API:** existe implementação no backend; falta o fluxo completo no frontend.
- **Planejado:** requisito ou proposta de organização sem contrato completo implementado.

As regras identificadas como **propostas** precisam de decisão da equipe. Não devem ser interpretadas como comportamento atual. Os documentos históricos que mencionam Firebase Auth ou ausência de chat conectado estão desatualizados: a autenticação atual usa JWT emitido pelo Flask e há telas remotas de comunidade.

## 2. Perfis e fronteiras de acesso

| Perfil exibido | Valor da API | Responsabilidade |
|---|---|---|
| Turista | `usuario` | Descobrir trilhas, reservar, acompanhar participação e avaliar após conclusão |
| Guia | `guia` | Administrar suas trilhas, acompanhar reservas e responder a convites |
| Agência | `agencia` | Administrar suas atividades e vínculos com guias |
| Administrador | `admin` | Verificação de profissionais e atendimento; não disponível no cadastro público |

O servidor deve validar identidade, papel e vínculo em cada operação. Ocultar um botão não substitui autorização. Usar IDs como referências; e-mails legados precisam de compatibilidade ou migração explícita. Não usar o nome do guia como identificador.

**Divergências atuais:** a API permite que guia e agência também criem reservas próprias. A listagem de agenda permite agência consultar outro guia sem comprovar vínculo nessa rota. A equipe deve decidir o primeiro comportamento e restringir o segundo antes de expor a gestão de participantes.

## 3. Funções comuns e acesso

| ID | Função | Interface e comportamento | Estado |
|---|---|---|---|
| AC-01 | Entrar no aplicativo | Boas-vindas com Fazer login e Criar conta | Integrado |
| AC-02 | Autenticar | Somente e-mail e senha; servidor determina perfil e home | Integrado |
| AC-03 | Escolher perfil de cadastro | Turista, guia ou agência; não aparece antes do login | Integrado |
| AC-04 | Cadastrar turista | Nome, e-mail, senha e dados de contato/localização | Integrado |
| AC-05 | Cadastrar guia | Dados básicos e CPF válido no campo `documento` | Integrado |
| AC-06 | Cadastrar agência | Dados básicos e CNPJ válido no campo `documento` | Integrado |
| AC-07 | Recuperar senha | Solicitar e-mail; informar token e nova senha | Integrado; SMTP pendente de homologação |
| AC-08 | Restaurar/encerrar sessão | Restaurar conta e token; no logout remover dispositivo e dados de sessão | Integrado |
| AC-09 | Consultar/editar perfil | Foto, nome, telefone, cidade, estado e demais campos autorizados | Integrado |
| AC-10 | Manter contato de emergência | Nome e telefone em dados pessoais | API; falta interface |
| AC-11 | Privacidade e segurança | Informações de sessão e ações de senha; conferir comportamento remoto | Parcial |
| AC-12 | Conversar | Lista de conversas e mensagens; turista inicia com guia | Integrado; atualização manual |
| AC-13 | Solicitar suporte | Abrir assunto e primeira mensagem; acompanhar respostas | Integrado |
| AC-14 | Notificações | Permissão, registro de dispositivo, central e preferências | Parcial; ver seção 9 |
| AC-15 | Excluir conta | API possui exclusão; falta definir impacto nas reservas e mensagens | API; não liberar sem política de dados |
| AC-16 | Alterar tipo da conta | Endpoint específico com documento; não pelo update genérico | API; mudança pela interface depende de decisão |
| AC-17 | Enviar documentos profissionais | Upload privado e acompanhamento da análise | Planejado; upload de imagens atual não equivale a este fluxo |

Validação de CPF/CNPJ pertence ao cadastro correspondente. Login nunca solicita documento nem escolha de perfil. Documento numericamente válido não equivale a profissional verificado.

## 4. Funções do turista

| ID | Função | Dados/ações necessários | Estado |
|---|---|---|---|
| TU-01 | Explorar catálogo | Listagem, imagem, nome, cidade, dificuldade, data e preço | Integrado |
| TU-02 | Buscar trilhas | Cidade, estado, dificuldade, período e proximidade | Parcial: conferir uso dos filtros da API versus filtros locais |
| TU-03 | Filtrar acessibilidade | Opção acessível e informação nos detalhes | API; completar modelo e interface |
| TU-04 | Abrir detalhes | Descrição, distância, localização, responsável e situação | Integrado; complementar planejamento |
| TU-05 | Ver guia | Perfil público, trilhas e ação de conversa | Parcial: catálogo remoto é reduzido; estatísticas não têm contrato completo |
| TU-06 | Favoritar | Adicionar, remover e recuperar favoritos após login | Integrado |
| TU-07 | Reservar atividade | Selecionar trilha/data, confirmar e receber ID da reserva | Integrado; regras de vagas/preço precisam evoluir |
| TU-08 | Consultar/cancelar reservas | Lista própria, situação e confirmação de cancelamento | Integrado |
| TU-09 | Consultar planejamento | Equipamentos, percurso, previsão e rota até o início | API; falta tela integrada |
| TU-10 | Fazer check-in/check-out | Iniciar e concluir reserva, respeitando estado | API; falta interface |
| TU-11 | Avaliar trilha concluída | Nota 1–5 e comentário, uma avaliação por usuário/trilha | API; falta interface |
| TU-12 | Ler avaliações | Notas, comentários, média e quantidade | API; falta interface |

Não há pagamento online comprovado. `valor_pago` é um campo declarado da reserva, não confirmação financeira. Não criar tela de cartão, cobrança ou reembolso sem definição e integração próprias.

## 5. Funções do guia

| ID | Função | Dados/ações necessários | Estado |
|---|---|---|---|
| GU-01 | Consultar dashboard | Quantidade de reservas, estados e valores declarados | Parcial: painéis Flutter calculam sobre dados carregados; existe endpoint próprio |
| GU-02 | Gerenciar trilhas | Listar suas atividades; criar, editar e desativar | Integrado |
| GU-03 | Preencher trilha | Nome, descrição, dificuldade, modalidade, distância, data, preço, capa e coordenadas | Integrado |
| GU-04 | Completar planejamento | Acessibilidade, itens recomendados e pontos do trajeto | API; falta completar formulário/modelo |
| GU-05 | Acompanhar agenda | Reservas sob sua responsabilidade | Integrado; verificar referências legadas |
| GU-06 | Consultar participantes | Lista por atividade/data e detalhes autorizados | Parcial: reservas existem; resposta de participante precisa ser definida |
| GU-07 | Consultar emergência | Dados permitidos pela reserva e vínculo | API; revisar duração da autorização |
| GU-08 | Acompanhar execução | Check-in/check-out e situação de cada reserva | API; falta interface |
| GU-09 | Responder convites | Consultar, aceitar ou recusar convite da agência | Integrado |
| GU-10 | Responder mensagens | Conversar com participantes autorizados | Integrado |
| GU-11 | Manter disponibilidade | Calendário, horários bloqueados e vagas | Planejado; não há contrato de disponibilidade completo |
| GU-12 | Manter dados profissionais | Descrição, especialidades, documentos e verificação | Parcial; definir campos persistidos e exposição pública |

## 6. Funções da agência

| ID | Função | Dados/ações necessários | Estado |
|---|---|---|---|
| AG-01 | Consultar dashboard | Atividades e reservas da agência | Parcial: definir agregação das trilhas atribuídas a guias |
| AG-02 | Gerenciar trilhas | Criar, editar, desativar e completar planejamento | Integrado no básico; planejamento parcial |
| AG-03 | Atribuir responsável | Própria agência ou guia com convite aceito | Integrado; servidor valida vínculo |
| AG-04 | Consultar catálogo de guias | Nome, cidade, estado, foto e verificação | Integrado |
| AG-05 | Convidar guia | Enviar convite e acompanhar situação | Integrado |
| AG-06 | Gerenciar vínculo | Ver aceitos, pendentes e recusados | Integrado; reenvio, revogação e desligamento não implementados |
| AG-07 | Acompanhar reservas | Consultar reservas relacionadas às suas atividades | Parcial: corrigir escopo da autorização e agregação |
| AG-08 | Acompanhar participantes | Lista, andamento e emergência apenas quando autorizada | API parcial; falta fluxo seguro completo |
| AG-09 | Planejar calendário | Distribuir atividades e evitar choque de horários | Planejado; requer contrato de disponibilidade |
| AG-10 | Manter perfil empresarial | Nome, contato, localização, foto, CNPJ e verificação | Parcial para documentos e análise |
| AG-11 | Atendimento e notificações | Usar suporte e receber eventos das atividades | Parcial; chat genérico agência–turista não está implementado |

Não reutilizar controles locais de “ativar/remover guia” como se alterassem vínculos remotos. Não presumir que o papel agência concede acesso a todos os usuários e reservas.

## 7. Inventário de telas e componentes

As telas compartilhadas devem receber contexto e permissões, evitando três implementações iguais.

| Tela/fluxo | Arquivo atual em `lib/pages/` ou situação | Funções |
|---|---|---|
| Boas-vindas | `auth/welcome_screen.dart` | AC-01 |
| Login | `auth/login_screen.dart` | AC-02 |
| Seleção de perfil | `auth/profile_choice_screen.dart` | AC-03 |
| Cadastro por perfil | `auth/register_screen.dart` | AC-04–06 |
| Recuperação/redefinição | `auth/forgot_password_screen.dart` | AC-07 |
| Home turista | `tourist/tourist_home_tab.dart` | TU-01 |
| Busca | `tourist/trail_search_screen.dart` | TU-02–03 |
| Detalhes da trilha | `tourist/trail_details_screen.dart` | TU-04, TU-07 |
| Perfil público do guia | `tourist/guide_profile_screen.dart` | TU-05 |
| Favoritos | `common/favorites_screen.dart` | TU-06 |
| Reservas/agenda | `common/bookings_screen.dart` | TU-08, GU-05, AG-07 |
| Dashboard guia | `guide/guide_dashboard_tab.dart` | GU-01 |
| Dashboard agência | `agency/agency_dashboard_tab.dart` | AG-01 |
| Minhas trilhas | `common/trails_management_screen.dart` | GU-02, AG-02 |
| Formulário de trilha | `management/trail_form_screen.dart` | GU-03–04, AG-03 |
| Guias e convites | `agency/remote_guides_screen.dart`; variante local em `guides_screen.dart` | GU-09, AG-04–06 |
| Lista e detalhe de conversa | `common/remote_conversations_screen.dart`; entrada em `messages_screen.dart` | AC-12 |
| Perfil | `common/profile_tab.dart` | AC-09, GU-12, AG-10 |
| Dados pessoais | `common/settings/personal_data_screen.dart` | AC-09–10 |
| Privacidade e segurança | `common/settings/privacy_security_screen.dart` | AC-11 |
| Central de notificações | `common/notification_center_screen.dart` | AC-14 |
| Preferências de notificações | `common/settings/notifications_screen.dart` | AC-14 |
| Suporte | `common/settings/help_support_screen.dart` e conversa remota | AC-13 |
| Detalhe da reserva/participantes | A completar; pode ser painel dentro da agenda | TU-08, GU-06–08, AG-08 |
| Planejamento e mapa | A criar; reutilizar detalhes da trilha | TU-09 |
| Avaliações/lista e formulário | A criar | TU-11–12 |
| Calendário de disponibilidade | A criar após contrato | GU-11, AG-09 |
| Documentos e situação da análise | A criar após contrato privado | AC-17 |
| Administração: verificação e suporte | A criar; usar login único com papel admin | Dependências operacionais |

Os arquivos `tourist_shell.dart`, `guide_shell.dart` e `agency_shell.dart` organizam navegação por perfil. Não representam novas funções de negócio. Check-in, cancelamento e confirmação de reserva podem ser ações/modais na tela de detalhes.

### Estados obrigatórios

Toda consulta deve prever carregamento, lista vazia, sucesso, falha e tentativa novamente. Formulários devem manter os dados após falha, indicar erro por campo e impedir envio repetido enquanto aguardam resposta. Tratar sessão expirada, permissão negada e recurso removido. Geolocalização e notificações devem continuar opcionais para navegar; exibir alternativa quando a permissão for negada.

## 8. Catálogo de contratos existentes

Base local: `http://127.0.0.1:5000`. Utilizar JSON, exceto upload. Rotas protegidas recebem `Authorization: Bearer <JWT>`. O prefixo `/api` está incluído abaixo. Preservar barras finais usadas pelo backend.

### 8.1 Conta

| Método e rota | Entrada/retorno principal | Permissão |
|---|---|---|
| POST `/api/usuarios/` | Cadastro: `nome`, `email`, `senha`, `tipo`, `documento` para guia/agência | Público |
| POST `/api/auth/login` | `email`, `senha`; retorno contém `token`, `id`, `tipo`, `nome` e mensagem | Público |
| POST `/api/auth/senha/solicitar` | `email` | Público |
| POST `/api/auth/senha/redefinir` | `token`, `nova_senha` | Token de recuperação |
| GET/PUT/DELETE `/api/usuarios/<id>` | Consultar, editar ou excluir conta | Próprio usuário/admin |
| GET/PUT/DELETE `/api/usuarios/email/<email>` | Alternativa legada por e-mail | Próprio usuário/admin |
| GET `/api/usuarios/` | Listagem administrativa | Admin |
| PUT `/api/usuarios/<id>/tipo` | `tipo`, `documento` | Próprio usuário/admin; regras específicas |
| PUT `/api/usuarios/<id>/verificar` | `verificado` booleano | Admin |
| GET `/api/usuarios/<id>/contato-emergencia` | Nome/telefone do participante e contato de emergência | Guia/agência com vínculo verificado no serviço, ou admin |

O cadastro também persiste `telefone`, `cidade`, `estado`, `contato_emergencia_nome` e `contato_emergencia_telefone`. Atualizações precisam de lista explícita de campos permitidos. Não enviar `tipo` ou `verificado` pelo formulário genérico de perfil.

### 8.2 Trilhas, favoritos e imagens

| Método e rota | Entrada/retorno | Permissão |
|---|---|---|
| GET `/api/trilhas/` | Lista de trilhas | Autenticado |
| GET `/api/trilhas/<id>` | Detalhes | Autenticado |
| GET `/api/trilhas/busca` | Query: `cidade`, `estado`, `dificuldade`, `data_inicio`, `data_fim`, `latitude`, `longitude`, `raio_km`, `acessivel` | Autenticado |
| GET `/api/trilhas/periodo` | `data_inicio`, `data_fim` obrigatórios | Autenticado |
| POST `/api/trilhas/` | Dados de trilha | Guia/agência |
| PUT `/api/trilhas/<id>` | Campos editados | Criador/responsável/admin |
| DELETE `/api/trilhas/<id>` | Desativação lógica: `ativo=false` | Criador/responsável/admin |
| GET `/api/trilhas/<id>/clima` | Previsão completa e previsão da data, que pode ser nula | Autenticado |
| GET `/api/trilhas/<id>/rota-ate-destino` | `latitude`, `longitude`, `perfil`; retorno `distancia_km`, `duracao_minutos`, `perfil`, `trajeto` | Autenticado |
| GET/POST `/api/favoritos/` | GET lista; POST recebe `id_trilha` | Própria conta |
| DELETE `/api/favoritos/<id_trilha>` | Remove favorito | Própria conta |
| POST `/api/uploads/imagem` | Multipart, campo `image`; retorno `url` consumido pelo frontend | Qualquer usuário autenticado |

Dados básicos da trilha: `nome`, `descricao`, `dificuldade` obrigatórios na criação; `cidade`, `estado`, `modalidade`, `distancia_km`, `data_atividade`, `imagem_url`, `preco`, `ativo`, `id_guia`, `latitude`, `longitude`. Planejamento: `acessivel`, `itens_recomendados` (lista de textos), `trajeto` (lista de pontos). O frontend ainda não envia todos os campos de planejamento.

Datas devem viajar como `YYYY-MM-DD`, com formatação brasileira apenas na apresentação. Coordenadas dos pontos usam `latitude` e `longitude`; não inverter ao desenhar mapas. A rota externa é convertida pelo servidor para esse formato. A imagem atual é uma capa; galeria e elevação previstas no backlog não possuem contrato completo confirmado.

Busca avançada vazia atualmente retorna 404 com mensagem, em vez de lista vazia. Tratar esse caso apenas na busca; não transformar qualquer 404 em sucesso. Proposta futura: padronizar listas vazias com 200 e `[]`.

### 8.3 Reservas, execução e avaliações

| Método e rota | Entrada/retorno | Permissão/regra |
|---|---|---|
| POST `/api/agendamentos/` | `id_trilha`, `data_agendada`, `valor_pago`; retorna `id` e mensagem | Servidor define `id_usuario`; aceita turista, guia e agência |
| GET `/api/agendamentos/usuario/<id>` | Lista própria | Dono/admin |
| GET `/api/agendamentos/guia/<id>` | Lista por responsável | Guia próprio/admin; agência possui permissão ampla atual a corrigir |
| PUT `/api/agendamentos/<id>/cancelar` | Sem dados adicionais obrigatórios | Dono/responsável/admin |
| PUT `/api/agendamentos/<id>/checkin` | `latitude`, `longitude` opcionais | Dono/responsável/admin; exige estado `agendado` |
| PUT `/api/agendamentos/<id>/checkout` | Sem dados adicionais obrigatórios | Dono/responsável/admin; exige `em_andamento` |
| GET `/api/agendamentos/dashboard/<id>` | `total_agendamentos`, `por_status`, `valor_declarado_ativo` | Próprio guia/agência ou admin |
| POST `/api/avaliacoes/` | `id_trilha`, `nota`, `comentario` | Usuário com reserva concluída; identidade vem da sessão |
| GET `/api/avaliacoes/trilha/<id>` | Lista de avaliações | Autenticado |
| POST `/api/agendamentos/testar-lembretes` | Disparo da rotina de lembretes | Admin; não expor em tela comum |

Estados da reserva: `agendado`, `em_andamento`, `concluido`, `cancelado`. Check-in transforma agendado em em_andamento; check-out transforma em_andamento em concluido. A política de cancelamento após início/conclusão ainda precisa de revisão: não presumir bloqueios que o serviço não implementa.

Uma avaliação é permitida por par usuário/trilha, com nota de 1 a 5 e reserva concluída. Repetição retorna conflito. Não existe contrato de avaliação independente do guia; não apresentar notas fictícias como reputação real.

### 8.4 Comunidade

| Método e rota | Entrada/retorno | Regra |
|---|---|---|
| GET `/api/guias` | Catálogo reduzido: ID, nome, cidade, estado, foto e verificação | Autenticado; sem documento, senha ou e-mail |
| GET/POST `/api/conversas` | POST `id_guia`; GET lista própria | Turista inicia; repetir par recupera conversa |
| GET/POST `/api/conversas/<id>/mensagens` | POST `texto`, até 2000 caracteres | Somente participantes; servidor define autor |
| GET/POST `/api/suporte` | POST `assunto` até 120 caracteres e `texto` | Conta abre atendimento; admin lista todos |
| GET/POST `/api/suporte/<id>/mensagens` | POST `texto` | Dono/admin; apenas admin é atendente |
| GET/POST `/api/convites-guias` | POST `id_guia`; GET lista própria | Agência envia; guia/agência consultam |
| PUT `/api/convites-guias/<id>` | `status`: `aceito` ou `recusado` | Apenas guia convidado; resposta única |

Mensagens usam atualização manual e limite de 100 mensagens recentes. Não há anexos, confirmação de leitura ou paginação anterior. Convites não possuem reenvio/revogação. O vínculo aceito permite atribuir guia à trilha; não transfere automaticamente todas as permissões da agência.

## 9. Notificações: divergência encontrada após integração das branches

Há duas implementações para POST/DELETE `/api/usuarios/fcm-token`:

1. `routes/community_routes.py` usa `dispositivos_fcm`, com `token` e `dispositivo_id`; DELETE recebe `dispositivo_id` na query. É o contrato usado pelo frontend atual.
2. `routes/usuarios_routes.py` chama `Notificacoes` e mantém `usuarios.fcm_tokens`; POST/DELETE recebem `token` no JSON.

O teste POST `/api/usuarios/fcm-token/teste` utiliza `PushDevices`, enquanto as notificações de agendamento/cancelamento e os lembretes usam `Notificacoes`. Portanto, o teste de dispositivo pode funcionar sem que os eventos de reserva alcancem os mesmos dispositivos.

**Decisão proposta:** manter um único contrato por instalação, centralizar envio e migrar tokens legados com segurança. Remover a ambiguidade das rotas após testes. Não manter duas fontes de verdade.

O código atual contém gatilhos de agendamento, cancelamento e lembretes diários às 18h de São Paulo. O documento histórico de comunidade que afirma ausência desses gatilhos ficou desatualizado após o merge. Presença do código não comprova recebimento real nem execução confiável do agendador.

Faltam definir histórico persistente da central, marcação como lida, preferências por evento e comportamento de múltiplos dispositivos. “Envio aceito pelo FCM” não significa “notificação recebida”.

## 10. Pendências que bloqueiam contratos definitivos

| ID | Divergência/decisão | Tratamento necessário |
|---|---|---|
| PD-01 | Dois contratos e armazenamentos FCM | Unificar antes de homologar notificações automáticas |
| PD-02 | Agência pode consultar agenda de qualquer guia na rota atual | Exigir vínculo e escopo de atividade no servidor |
| PD-03 | Emergência considera qualquer reserva não cancelada, inclusive concluída | Definir janela de acesso; alinhar regra e teste |
| PD-04 | Preço/`valor_pago` enviados pelo cliente | Definir preço autoritativo no servidor e separar pagamento de reserva |
| PD-05 | Capacidade, duplicidade, data e cancelamento não formam política completa | Definir vagas, conflitos e estados permitidos antes do calendário |
| PD-06 | Conta e trilha usam referências legadas por e-mail em alguns fluxos | Padronizar IDs e planejar migração; testar alteração de e-mail |
| PD-07 | Agência e guia atribuído não têm a mesma visão de reservas/dashboard | Definir agregação por proprietário e responsável |
| PD-08 | Perfil público tem mais campos que catálogo remoto | Criar contrato sanitizado; nunca usar endpoint privado de usuário como atalho |
| PD-09 | Documentos, análise e motivo de recusa não têm fluxo completo | Definir armazenamento privado, acesso, estados e retenção |
| PD-10 | Atualização de perfil/trilha precisa de campos controlados | Revisar listas permitidas e validação no servidor |
| PD-11 | Central e preferências de notificação incompletas | Definir persistência, leitura e aplicação das preferências |
| PD-12 | Serviços externos e agendador ainda não homologados | Testar em ambiente isolado e registrar resultados reais |

Este documento registra as divergências; não altera o código nem afirma que elas foram corrigidas.

## 11. Critérios de aceite para integração e telas

| Cenário | Resultado verificável |
|---|---|
| Login dos três perfis | E-mail/senha abrem a home correta sem escolher perfil |
| Cadastro inválido | CPF/CNPJ inválido bloqueado apenas no perfil correspondente; duplicidade tratada |
| Sessão | Reabertura restaura conta válida; 401 exige autenticação novamente |
| Perfil | Alteração persiste após novo login; mudança de papel não passa pelo update genérico |
| Trilha | Criar/editar recupera mesmos dados; terceiro não altera; desativada não recebe reserva |
| Reserva | ID e situação persistem; outro turista não consulta ou cancela |
| Agência | Agência sem vínculo não consulta reservas nem emergência de outra operação |
| Execução | Check-out antes de check-in falha; transição válida atualiza tela |
| Avaliação | Sem conclusão falha; nota inválida falha; duplicada retorna conflito |
| Convite | Guia convidado decide; outro não decide; aceite atualiza seletor de responsável |
| Conversa | Terceiro não acessa mensagens; autor não pode ser falsificado |
| Suporte | Usuário não se apresenta como atendente; admin responde |
| Planejamento | Sem GPS ou sem previsão, detalhes continuam acessíveis com informação clara |
| Push | Registro, rotação, logout de uma instalação e evento real funcionam nos dispositivos corretos |
| Falha externa | Upload/e-mail/clima falham com mensagem útil; reserva não deve falhar após persistir por erro de notificação |

Para cada tarefa, registrar: ID funcional, tela, endpoint, payload, resposta, permissão, teste positivo, teste negativo e evidência de persistência. Testes com serviços simulados e testes reais devem ser identificados separadamente.

## 12. Sequência de implementação

1. **Estabilizar contratos:** PD-01 a PD-07, respostas de erro e modelos por ID.
2. **Homologar núcleo existente:** conta, trilhas, favoritos, reserva, comunidade e convites.
3. **Completar experiência da atividade:** participantes, emergência, check-in/check-out e avaliações.
4. **Completar planejamento:** equipamentos, acessibilidade, mapa, clima e rota.
5. **Completar operação:** perfil profissional, documentos, verificação e suporte administrativo.
6. **Evoluir disponibilidade:** calendário, vagas e bloqueios após definir regras de negócio.

Nenhuma tela deve ser marcada concluída apenas por exibir dados locais. No modo conectado, o critério é executar a operação autorizada, persistir e recuperar o resultado da API.

## 13. Fontes locais e manutenção

- Backend: `D:/projetos/rotafacil_backend/routes/` e `services/`.
- Frontend: `D:/projetos/rotafacil_frontend/lib/pages/`, `lib/services/backend_repository.dart`, modelos e estado.
- Planejamento: `planning/backlog.md`, `planning/project-vision.md` e `planning/roadmap.md` no repositório de documentação.
- Contratos históricos: `D:/projetos/rotafacil_backend/CONTRATOS_COMUNIDADE.md`; aplicar a ressalva da seção 9.

Atualizar este documento sempre que uma rota, permissão, payload ou regra de negócio mudar. O backend mantém os contratos executáveis; o frontend mantém o mapeamento de modelos e telas; a equipe revisa em conjunto os critérios de aceite. Registrar as decisões PD em tarefas antes de implementar regras novas.
