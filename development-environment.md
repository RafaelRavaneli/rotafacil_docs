# Documentação do Ambiente de Desenvolvimento

<<<<<<< HEAD
[cite_start]Este documento descreve as configurações, ferramentas, linguagens e dependências necessárias para reproduzir, executar e testar o ambiente de desenvolvimento do projeto **Rota-Fácil**[cite: 105, 115].

## 1. Visão Geral do Ecossistema Técnico
* [cite_start]**Sistema Operacional Base:** Windows 10 / Windows 11[cite: 107].
* [cite_start]**Editor de Código / IDE:** Visual Studio Code (VS Code)[cite: 108].
* [cite_start]**Linguagem de Programação:** Python 3.10+[cite: 109].
* [cite_start]**Framework Web (Back-end):** Flask[cite: 109].
* [cite_start]**Banco de Dados:** Google Firebase Firestore (NoSQL orientado a documentos)[cite: 110].

---

## 2. Dependências e Tecnologias do Banco de Dados
[cite_start]Para a camada de persistência e segurança desenvolvida nesta sprint, utilizamos o ecossistema oficial do Firebase para Python:

* [cite_start]**firebase-admin:** SDK oficial do Google Cloud para conectar a aplicação Flask às coleções do Firestore de forma administrativa[cite: 111].
* **uuid:** Biblioteca nativa do Python utilizada para a geração de identificadores únicos universais (UUIDv4) para as chaves primárias dos documentos de Usuários, Trilhas e Agendamentos.

---

## 3. Instruções de Instalação e Configuração Passo a Passo

### Passo 1: Clonar o Repositório Privado
[cite_start]Abra o terminal na pasta onde armazena seus projetos e execute o comando para clonar o projeto[cite: 116]:
```bash
git clone [https://github.com/JoseLucasFerreira44/rotafacil-app.git](https://github.com/RafaelRavaneli/rotafacil-app.git)
cd rotafacil-app
=======
[cite_start]Para garantir a rastreabilidade e permitir que qualquer membro da equipe execute o projeto localmente, documentamos o ambiente utilizado[cite: 156]:

* [cite_start]**Sistema Operacional:** Windows 10/11 / Linux / macOS [cite: 158]
* [cite_start]**Editor/IDE:** Visual Studio Code [cite: 159]
* [cite_start]**Linguagens e Versões:** Python 3.10+ (Backend) e Dart/Flutter (Frontend) [cite: 160]
* [cite_start]**Banco de Dados:** Google Firebase Firestore (NoSQL) [cite: 161]
* [cite_start]**Principais Dependências:** Flask, PyJWT, Werkzeug, Firebase-Admin [cite: 162]

## [cite_start]Instruções de Configuração e Execução [cite: 166, 167]

1. **Clonar o repositório:**
   `git clone [LINK-DO-REPO]`
2. **Criar e ativar o ambiente virtual:**
   * Windows: `python -m venv venv` seguido de `.\venv\Scripts\activate`
   * Linux/Mac: `python3 -m venv venv` seguido de `source venv/bin/activate`
3. [cite_start]**Instalar as dependências do projeto:** [cite: 163]
   `pip install -r requirements.txt`
4. [cite_start]**Configurar as Variáveis de Ambiente:** [cite: 165]
   Crie um arquivo `.env` na raiz do projeto (baseado no `.env.example`) e insira a chave secreta: `KEY=sua_chave_aqui`. Adicione também o arquivo `firebase-key.json` fornecido pelo DBA.
5. [cite_start]**Executar o Servidor:** [cite: 164]
   `python app.py`
>>>>>>> 1bb9056277853a3d620965bee8bf60b98344a674
