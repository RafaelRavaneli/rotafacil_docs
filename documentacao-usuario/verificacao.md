# Registro de verificação e lacunas

[← Voltar ao índice](README.md)

Este documento separa o que foi **verificado**, o que ficou **não verificado** e as **lacunas** da documentação de usuário. Data da análise: 10/11/2026.

## Briefing (resumo)

| Item | Definição |
|---|---|
| Leitores | Turistas, guias, agências e administração do RotaFácil |
| Tarefas | Criar conta, buscar/reservar/avaliar, operar roteiros, gerenciar vínculos, moderar |
| Gêneros | How-to e tutorial por perfil; referência de mensagens (solução de problemas) |
| Fonte autoritativa | Código do frontend e do backend nos commits indicados no README |
| Fora do escopo | Instalação e deploy (já cobertos em `DEPLOY_VERCEL.md` e `DEPLOY_RENDER.md` do backend) |

## O que foi verificado

- Textos de botões, títulos e mensagens foram extraídos das telas Flutter (`rotafacil_frontend/lib/pages` e `widgets`).
- Regras de cancelamento, resposta, finalização de saída, convites, ações administrativas e prazo de edição de avaliação foram conferidas em `rotafacil_backend/services`.
- Suíte de testes do backend (148 testes) e do frontend (164 testes, 11 pulados) passou; `flutter analyze` sem alertas. Isso valida o código, **não** o texto desta documentação.
- O app foi **executado em modo local** (build web servido em 127.0.0.1) e percorridos: tela inicial, login, Explorar, filtros de busca, detalhe de roteiro, Minhas reservas e detalhe da reserva. Os textos desses fluxos batem com os guias.
- Os links relativos entre os arquivos desta pasta foram checados por script.
- Telefone é opcional no cadastro (a validação exige só nome, e-mail, senha, termos e, por perfil, documento).
- Só o criador do roteiro (ou admin) responde reservas e finaliza saídas; o guia responsável de roteiro de agência não (`_usuario_pode_gerenciar_trilha`).
- Denúncia de avaliação: qualquer usuário logado, menos o autor; motivos conteúdo ofensivo, dados pessoais, spam e outro.
- Botões do formulário de roteiro: **Adicionar roteiro** e **Salvar alterações**.

- **Revisão de 16/11/2026:** textos de Perfil, Dados pessoais, notificações e da home conferidos no código publicado (`a1093e5`). A refatoração das telas removeu o atalho "Editar perfil" (agora tudo fica em "Dados pessoais"), trocou o botão "Salvar alterações" pela barra "Salvar", criou "Ajustar foto" e passou a pedir a localização só quando a pessoa toca em "Usar minha localização". O print `perfil.png` foi removido por mostrar a tela antiga.

## O que **não** foi verificado

- Os fluxos de **criar reserva**, **cancelar**, **avaliar**, de **guia/agência** e de **administração** não foram percorridos no app: os dados de demonstração usados não tinham roteiro com datas disponíveis. Esses passos vêm da leitura do código.
- O teste foi em modo local (dados fictícios), sem backend. E-mail, push e mapa (tiles) não funcionaram no ambiente de teste.
- Comportamento com check-in/check-out ligado (recurso desativado por padrão).
- Envio real de e-mail e notificações push (dependem de SMTP e Firebase configurados).

## Lacunas (decisão humana)

1. **URL de produção:** `rotafacil.eco.br`, informada pela equipe (confirmada com a grafia correta). Não foi acessada por esta documentação.
2. **Canal de suporte:** `nao.responda.rotafacil@gmail.com`, informado pela equipe. O nome do endereço sugere caixa "não responda"; confirme que alguém lê as mensagens.
3. **Capturas de tela**: há 7 prints do perfil de turista em `imagens/` (o do Perfil foi removido na revisão de 16/11). Faltam capturas dos perfis de guia, agência e administração.
4. **Validação com leitores reais**: não realizada. Sugestão: pedir a 3 pessoas (um turista, um guia, uma agência) que cumpram as tarefas de cada guia e anotar onde travam.
5. **Documentos de planejamento** (`planning/`) estão desatualizados (citam Firebase Auth e deixam agendamento e avaliações para versões futuras, mas o código já os implementa). Eles não foram alterados.

## Contradições encontradas nas fontes

| Fonte A | Fonte B | Tratamento |
|---|---|---|
| `planning/roadmap.md`: login via Firebase Auth, agendamento só na v1.1 | Código: login com JWT próprio, agendamento e avaliações implementados | Prevaleceu o código |
| README do backend lista 5 módulos | Código tem 12 blueprints | Prevaleceu o código |
