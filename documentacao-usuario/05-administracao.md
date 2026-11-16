# Guia da administração

**Para quem:** equipe da plataforma com perfil **admin**.
**Ao final você saberá:** verificar profissionais, aplicar ações em contas e roteiros e moderar avaliações.

[← Voltar ao índice](README.md)

> O perfil admin **não pode ser escolhido no cadastro**. Ele é definido manualmente no banco de dados (Firestore). Sem esse perfil, o app mostra *"Acesso administrativo necessário."*

## 1. Console de administração

O console reúne três áreas: **Administração** (contas e roteiros), **Verificação profissional** e **Moderar avaliações**. Use a busca por nome, cidade ou e-mail para localizar o alvo.

## 2. Ações em contas e roteiros

Toda ação administrativa exige um **motivo de 3 a 500 caracteres** e fica **registrada em histórico**.

| Ação | Efeito |
|---|---|
| Bloquear / Desbloquear conta | Bloqueada, a pessoa não consegue mais entrar. Reservas e dados existentes são preservados |
| Suspender / Liberar roteiro | Suspenso, impede novas reservas. **Não cancela** as reservas existentes |
| Verificar perfil / Remover selo | Concede ou retira o selo "Perfil verificado". Uma conta bloqueada precisa ser desbloqueada antes de ser verificada |

⚠️ A administração **não exclui roteiros diretamente**; use a moderação com motivo e histórico.

## 3. Verificação profissional

1. Abra **Verificação profissional** e filtre pela situação do documento.
2. Veja o documento enviado e o número/validade do Cadastur informados (**Cadastur não informado** aparece quando faltar).
3. Aprove ou rejeite. Na rejeição, preencha **Motivo da rejeição** explicando o que precisa ser corrigido.

> O Cadastur **não é consultado automaticamente** na base oficial. A conferência é feita por quem analisa.

## 4. Moderar avaliações

1. Abra **Moderar avaliações** e veja as **Denúncias pendentes**.
2. Leia a avaliação e decida: **ocultar** ou **Manter e concluir análise**.
3. Justifique a decisão (3 a 500 caracteres) e toque em **Confirmar decisão**.

Avaliações ocultadas deixam de contar e não podem mais ser editadas pelo autor.

## 5. Testar lembretes

Existe um acionamento manual dos lembretes diários, restrito ao admin, usado para testes. Está documentado no backend (`POST /api/agendamentos/testar-lembretes`) e **não tem tela no app [não verificado em uso real]**.
