# Procedimento Operacional Padrão (POP 03)
## Padronização de Endpoints RESTful e Serialização de Respostas JSON

* **Objetivo:** Estabelecer um padrão de arquitetura e design de software para a construção de rotas na API Flask, garantindo a uniformidade dos métodos HTTP, códigos de status e a estrutura de entrega dos dados trafegados entre a aplicação e o cliente.
* **Responsável:** Desenvolvedores Back-end (Rafael Ravaneli e Thiago de Carvalho).
* **Quando usar:** Durante o mapeamento de rotas (endpoints), recepção de requisições de criação/atualização e definição das estruturas de retorno de dados da aplicação.
* **Pré-requisitos:** Rotas mapeadas nos arquivos de controle (ex: `usuarios.py`) e métodos de serviço que interagem com o Firebase (mapeados de acordo com o **POP 02**) já funcionais.

### Passo a Passo da Execução:
1. **Definição do Método HTTP:** Utilize os verbos HTTP estritamente associados à operação lógica: `GET` para listagens ou buscas por ID, `POST` para inserções, `PUT` para atualizações completas e `DELETE` para exclusões de documentos.
2. **Captura e Validação de Payload:** Para os métodos que recebem dados (`POST`/`PUT`), capture o corpo da requisição utilizando o método `request.get_json()`. Valide a presença dos atributos obrigatórios em nível de dicionário Python antes de prosseguir.
3. **Invocação da Camada de Serviço:** Repasse as variáveis validadas para as funções do módulo de serviços responsável por persistir as alterações diretamente nas coleções do Firebase.
4. **Serialização com `jsonify`:** Formate a saída do endpoint convertendo dicionários ou listas estruturadas através da função `jsonify()` nativa do Flask, garantindo que o cabeçalho `Content-Type` seja definido automaticamente como `application/json`.
5. **Aplicação do Status Code Adequado:** Retorne explicitamente o código de status HTTP correspondente ao resultado da operação (Ex: `201 Created` para inserções bem-sucedidas e `200 OK` para consultas e atualizações).

* **Evidências esperadas:** Métodos decorados com `@app.route` retornando a estrutura `return jsonify(dados), status_code` implementados na pasta de rotas do projeto.
* **Critérios de sucesso:** Requisições à API retornando matrizes e objetos JSON válidos, tipados corretamente e utilizando os códigos de status HTTP apropriados para cada operação, sem vazamento de strings brutas.
* **Referências utilizadas:**
  * FLASK. Responses in Flask. Pallets Projects, 2024. Disponível em: <https://flask.palletsprojects.com/en/stable/quickstart/#about-responses>.
  