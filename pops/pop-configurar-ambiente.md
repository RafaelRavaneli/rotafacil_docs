# Procedimento Operacional Padrão (POP 04)
## Configuração e Inicialização do Ambiente Local de Desenvolvimento (Flask + Firebase)

* **Objetivo:** Estabelecer um padrão reprodutível para o isolamento e configuração do ambiente local de desenvolvimento, garantindo que o back-end em Python/Flask execute corretamente e conecte-se com segurança aos serviços do Firebase.
* **Responsável:** Desenvolvedores Back-end (Rafael Ravaneli e Thiago de Carvalho).
* **Quando usar:** Durante o onboarding de novos desenvolvedores no projeto, ao configurar uma nova estação de trabalho ou ao reinicializar as dependências locais do sistema do zero.
* **Pré-requisitos:** Python 3.10 ou superior, Git e ferramenta de linha de comando instalados localmente, além de um projeto já criado no console do Firebase.

### Passo a Passo da Execução:
1. **Clonagem do Repositório:** Abra o terminal na pasta de destino desejada e execute o comando `git clone <URL_DO_REPOSITORIO>` seguido de `cd <PASTA_DO_PROJETO>` para acessar a raiz do código-fonte.
2. **Isolamento com Ambiente Virtual:** Crie uma estrutura isolada de pacotes executando `python -m venv venv`. Ative o ambiente virtual executando `source venv/bin/activate` (Linux/macOS) ou `.\venv\Scripts\Activate.ps1` (Windows PowerShell) para garantir que as instalações não interfiram no escopo global do sistema.
3. **Instalação de Dependências:** Execute o gerenciador de pacotes através do comando `pip install -r requirements.txt` para baixar e estruturar bibliotecas fundamentais como `Flask`, `firebase-admin` e `python-dotenv`.
4. **Injeção de Credenciais do Firebase:** Acesse o console do Firebase, navegue até 'Configurações do Projeto' > 'Contas de Serviço', clique em 'Gerar nova chave privada' e salve o arquivo JSON gerado na raiz do projeto sob o nome literal `firebase-credentials.json`. Adicione este nome ao arquivo `.gitignore` para impedir seu versionamento involuntário.
5. **Configuração de Variáveis de Ambiente:** Crie um arquivo local denominado `.env` na raiz do projeto e defina as chaves de controle da aplicação, especificando explicitamente as propriedades `FLASK_DEBUG=1` e `FIREBASE_CREDENTIALS_PATH=firebase-credentials.json`.
6. **Inicialização do Servidor Local:** Dispare a aplicação executando o comando `flask run` no terminal ativo. Certifique-se de que o servidor inicializou na porta padrão emitindo uma requisição de teste para o endereço `http://127.0.0.1:5000/`.

* **Evidências esperadas:** Diretório virtual `venv/` populado, arquivo `.env` configurado localmente e o terminal exibindo o status ativo do servidor Flask em modo de desenvolvimento (Development Mode).
* **Critérios de sucesso:** O back-end executando localmente sem disparar erros de módulos ausentes (`ModuleNotFoundError`) e estabelecendo comunicação inicial estável com o SDK do Firebase.
* **Referências utilizadas:**
  * PALLETS PROJECTS. Installation - Flask Documentation. Pallets, 2024. Disponível em: <https://flask.palletsprojects.com/en/stable/installation/>.
  * GOOGLE. Add the Firebase Admin SDK to your server. Firebase Docs, 2026. Disponível em: <https://firebase.google.com/docs/admin/setup>.

  