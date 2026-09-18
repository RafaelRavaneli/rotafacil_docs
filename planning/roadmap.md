# Roadmap do Projeto

O Rota Fácil segue o padrão de versionamento semântico (SemVer). A evolução do sistema está planejada em ciclos (Sprints) para garantir a entrega da versão de produção 1.0 até o final do terceiro bimestre. A nossa estratégia técnica prioriza a construção e estabilização completa da API (Backend) antes do desenvolvimento da interface de usuário (Frontend).

## Versão 0.1 (Atual - Fim do 1º Bimestre)
* Configuração do repositório, ambiente virtual e banco de dados Firebase.
* Implementação da API REST (Backend Flask) com CRUD completo para a entidade `Usuários`.
* Elaboração da documentação de planejamento e fluxo de trabalho.

## Versão 0.5 (Beta - 2º Bimestre)
* Expansão da API: Implementação do CRUD da entidade `Atividades/Trilhas` no backend.
* Desenvolvimento da lógica de filtros de busca (por cidade, dificuldade) direto na API.
* Implementação da lógica de upload de imagens e arquivos no servidor.
* Testes de integração de todas as rotas utilizando ferramentas como Postman.

## Versão 1.0.0 (Produção - Final do 3º Bimestre)
* Início do desenvolvimento do Frontend em Flutter.
* Criação das interfaces gráficas (Telas de Login, Cadastro, Catálogo e Perfil).
* Integração do Frontend Mobile/Web com a API Flask já finalizada.
* **Meta:** Sistema integrado, testado e organizado para uso real com interface gráfica completa.

## Versões Futuras (Pós 1.0 / Fora do Escopo Atual)
* `v1.1.0`: Sistema de agendamento e calendário.
* `v1.2.0`: Sistema de avaliações e comentários (Reviews).