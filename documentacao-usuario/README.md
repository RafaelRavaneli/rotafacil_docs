# RotaFácil — Documentação de usuário

Guia para quem usa o aplicativo RotaFácil: descobrir e reservar roteiros de ecoturismo (turista), publicar e operar roteiros (guia e agência) e moderar a plataforma (administração).

> **Versão coberta:** frontend publicado em 16/11/2026 (commit `a1093e5` na `main`) e backend do commit `be4d127`. Primeira análise em 10/11/2026; revisão em 16/11/2026. Plataforma: aplicativo Flutter (web e mobile).
> **Fonte de verdade:** o comportamento descrito aqui foi conferido nas telas do aplicativo e nas regras do backend. Onde algo não pôde ser confirmado, o texto traz o marcador **[não verificado]**. Veja [verificacao.md](verificacao.md).

## Por onde começar

| Eu quero… | Leia |
|---|---|
| Criar conta, entrar, recuperar a senha, editar o perfil | [01-primeiros-passos.md](01-primeiros-passos.md) |
| Buscar, reservar, cancelar e avaliar um roteiro | [02-turista.md](02-turista.md) |
| Cadastrar roteiros, responder reservas e finalizar saídas | [03-guia.md](03-guia.md) |
| Convidar guias e gerenciar vínculos da agência | [04-agencia.md](04-agencia.md) |
| Bloquear contas, verificar profissionais e moderar avaliações | [05-administracao.md](05-administracao.md) |
| Resolver um problema ou mensagem de erro | [06-solucao-de-problemas.md](06-solucao-de-problemas.md) |

Cada assunto tem **uma** página de referência. Quando outra página precisa de um assunto, ela aponta o link em vez de repetir o conteúdo.

## Perfis de conta

| Perfil | Para quem | O que faz no app |
|---|---|---|
| Turista | Quem quer fazer atividades | Busca roteiros, favorita, reserva, cancela, avalia |
| Guia | Profissional autônomo (exige CPF e Cadastur) | Cadastra roteiros, responde reservas, finaliza saídas |
| Agência | Empresa de ecoturismo (exige CNPJ e Cadastur) | Tudo que o guia faz, mais convidar guias para seus roteiros |
| Administração | Equipe da plataforma | Não se cadastra pelo app; o perfil é definido manualmente no banco |

## O que o RotaFácil **não** faz

- **Não cobra pagamento online.** O valor exibido é informado pelo organizador e não comprova pagamento. O combinado financeiro é feito diretamente com o responsável.
- **Não certifica acessibilidade nem segurança.** As informações de acessibilidade são declarações do organizador.
- **Não consulta a base oficial do Cadastur.** O número é apenas informado pelo profissional; o selo "Perfil verificado" é concedido pela administração após análise de documentos.

## Estado dos recursos

| Recurso | Estado |
|---|---|
| Cadastro, login, recuperação de senha, busca, reserva, avaliação, convites, administração | Implementado e coberto por testes automatizados |
| Confirmação de e-mail no cadastro | Implementado, mas **desligado por padrão** no backend (`EMAIL_VERIFICATION_ENABLED=false`) |
| Check-in e check-out | Implementado, mas **desligado por padrão** (`ENABLE_CHECKIN_CHECKOUT=false`); pode não aparecer na sua instalação |
| Notificações push | Depende de configuração do Firebase e de permissão no dispositivo |
| Endereço do aplicativo em produção | `rotafacil.eco.br` (informado pela equipe; esta documentação não acessou o endereço) |

## Fontes usadas

- Telas e textos do frontend: `rotafacil_frontend/lib/pages/**` e `lib/widgets/**`.
- Regras e validações: `rotafacil_backend/services/**` e `routes/**`.
- Documentos de contrato do backend: `ACESSIBILIDADE_ROTEIRO.md`, `CADASTUR.md`, `CONTATO_EMERGENCIA.md`, `AVALIACOES_MODERACAO.md`.
- Documentação de planejamento (`planning/`) foi consultada, mas está desatualizada em relação ao código e **não** foi usada como fonte de comportamento.
