# RotaFácil — Alinhamento Frontend x Backend

> Checklist consolidado a partir da revisão dos arquivos do frontend Flutter (`app_store.dart`, `pubspec.yaml`, models, `session_service.dart`, `app_config.dart`, `api_client.dart`, `notification_service.dart`, `fcm_token_api.dart`, `local_auth_service.dart`, `app.dart`, `demo_data.dart`, `login_screen.dart`, `auth_gateway.dart`, `document_validator.dart`, `forgot_password_screen.dart`, `register_screen.dart`) comparado com o que está registrado sobre o backend Flask.

## Contexto atual

- O app hoje roda **inteiramente em modo local/demo**, persistindo tudo via `SharedPreferences` (`AppStore`).
- Já existe um toggle de ambiente pronto: `AppConfig.useBackend` (`bool.fromEnvironment`, default `false`).
- A infraestrutura de rede (`ApiClient`, `SessionService`, `AuthGateway`, `FcmTokenApi`) já existe e está **parcialmente** ligada — o fluxo de login já respeita `useBackend`, mas a maior parte do resto do app ainda não.

---

## 🔴 Prioridade alta — bloqueadores para ligar o backend real

- [ ] **`ApiClient` só tem `post` e `delete`.** Faltam `get` e `put`/`patch` — sem eles não dá para listar trilhas/agendamentos/notificações/guias, nem atualizar perfil, status de agendamento ou trilha.
- [ ] **Sem suporte a multipart no `ApiClient`.** Necessário para upload de foto de perfil e imagem de trilha (o backend usa ImgBB para hospedagem).
- [ ] **Reset de senha ignora `AppConfig.useBackend`.** `ForgotPasswordScreen` chama `LocalAuthService.resetPassword` direto, mesmo com o backend real ligado (a própria tela avisa: "No modo local, a senha é atualizada neste dispositivo"). Decisão pendente: implementar fluxo real (e-mail + token) ou manter assim para o demo?
- [ ] **`AppStore` não consulta `useBackend` em nada.** Trilhas, agendamentos, favoritos, chat e notificações in-app continuam 100% locais mesmo com o backend ligado — só login/registro (`AuthGateway`) e token de push (`FcmTokenApi`) respeitam a flag hoje.
- [ ] **Sem bootstrap de sessão.** `app.dart`/`main.dart` sempre abre em `WelcomeScreen`, nunca verifica se já existe um token salvo em `SessionService` para pular direto pra tela logada.

---

## 🟠 Prioridade média — precisa confirmação com o backend antes de implementar

- [ ] **Claim `id` no JWT:** `AuthGateway` assume que o payload do token tem uma chave `id`. Se o backend usar outro nome (`sub`, `user_id`, `id_usuario`...), `SessionService.userId` fica vazio sem erro visível.
- [ ] **Nome dos campos de documento:** o front manda `cpf` e `cnpj` separados no body de login/registro. Confirmar se o backend espera exatamente esses nomes ou um campo único (`documento`).
- [ ] **Vocabulário de status de agendamento:** front usa `'Pendente'`/`'Confirmado'`/`'Cancelado'` (livre, capitalizado); backend usa state machine `agendado` → `em_andamento` → `concluido`. Precisa mapear os dois antes de conectar bookings.
- [ ] **Vocabulário de status de trilha:** front tem pelo menos `'Ativa'` e `'Em revisão'` — não confirmado se bate com os valores reais do backend.
- [ ] **`AppUser.role` vs. `tipo` do backend:** front guarda string capitalizada (`'Turista'`, `'Guia'`, `'Agência'`); backend espera minúsculo (`usuario`/`guia`/`agencia`). Existe conversão (`normalizeRole`, `UserRoleX.apiValue`), mas não é usada de forma 100% consistente em todo o app.
- [ ] **`Trail.guideName` mapeado para `id_guia`:** o campo do backend deveria ser uma referência (ID), não o nome do guia já resolvido. Decidir se o backend passa a devolver o nome, ou se o front ganha um `guideId` separado.
- [ ] **`AppUser.profileImageDataUrl`** guarda a imagem como Data URL local (base64); o fluxo real com ImgBB devolveria uma URL hospedada. Campo/fluxo ainda não preparado para isso.

---

## 🟡 Prioridade baixa — débito técnico / consistência interna

- [ ] **Normalização de papel duplicada em 3 lugares:** `AppStore.normalizeRole`, `LocalAuthService._roleKey` e `DocumentValidator` (`isValidForRole`/`labelForRole`/`formatForRole`) fazem a mesma checagem de string de forma independente. Vale extrair para uma função única compartilhada.
- [ ] **`AuthGateway.register` não inspeciona a resposta do backend** — depois da chamada, o front grava os dados do formulário direto no `AppStore`, sem usar nada que o backend tenha retornado (ex: um ID gerado).
- [ ] **Tratamento de erro genérico** nas telas de login/registro/reset (`error.toString()` direto na tela). Funciona bem para erro de API (`ApiException.message` já vem formatado), mas fica técnico em erro de rede (timeout, sem internet).

---

## 🟣 Funcionalidades do backend sem nenhuma representação no frontend ainda

- [ ] Planejamento de trilha (checklist de equipamento, polyline de rota, previsão do tempo, navegação) — feature branch do backend, nada equivalente em `Trail`.
- [ ] Flag de trilha acessível — existe no backend, ausente em `Trail`.
- [ ] Contato de emergência (restrito a guias com agendamento ativo) — sem campo em `AppUser`/`GuideProfile`.
- [ ] Avaliações pós-trilha (reviews) — não há model `Review`/`Avaliacao` no front; `GuideProfile.reviews` é só um contador (`int`).
- [ ] Papel de admin — backend tem badge de verificação de guia "admin-only"; `UserRole` do front só tem turista/guia/agência.
- [ ] Busca geoespacial — `Trail` já tem `latitude`/`longitude`, mas nada no front usa isso para buscar por proximidade ainda.
- [ ] Token de dispositivo FCM — fluxo existe (`FcmTokenApi`), mas ainda não testado ponta a ponta contra `/api/usuarios/fcm-token`.

---

## Arquivos ainda não revisados (para fechar o quadro por completo)

- Telas de trilhas/agendamentos/perfil (pasta `pages/`) — para ver como consomem `Trail`/`LocalBooking` hoje.
- Demais arquivos em `services/`, se houver algum além dos já revisados.
- Módulo de avaliações (reviews) no front, se já existir algum rascunho.

---

## 🟢 O que já está bem encaminhado (não mexer sem necessidade)

- `SessionService` já guarda `token`/`role`/`email`/`userId` corretamente para JWT.
- `ApiClient` já injeta `Authorization: Bearer <token>` automaticamente e trata erro no formato que o backend costuma devolver (`erro`/`mensagem`).
- `AuthGateway` já roteia entre modo local e modo backend real no login e registro, com nomes de campo (`tipo`, `senha`) consistentes com a convenção do backend.
- `DocumentValidator` implementa validação real de CPF/CNPJ (dígito verificador mod 11), não só formatação.
- `Trail.fromJson` já antecipa nomes divergentes (`nome`/`name`, `cidade`/`city` etc.) — só falta completar o caminho inverso (`toApiJson`).
