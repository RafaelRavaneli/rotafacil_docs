# Procedimento Operacional Padrão (POP 01)
## Validação e Consistência de Dados em Coleções NoSQL

* **Objetivo:** Garantir que nenhum documento seja salvo no banco de dados Firestore com campos obrigatórios ausentes, nulos ou com tipos incorretos, preservando a integridade dos dados do sistema Rota-Fácil.
* **Responsável:** Administrador de Banco de Dados (José Lucas).
* **Quando usar:** Sempre que uma nova coleção (tabela) for mapeada ou um novo método de inserção de dados (Create/POST) for desenvolvido no sistema.
* **Pré-requisitos:** 1. SDK `firebase_admin` instalado e configurado no ambiente.
  2. Biblioteca nativa `uuid` importada para geração de chaves primárias.

### Passo a Passo da Execução:
1. **Mapeamento de Requisitos:** Antes de codificar, liste em um array de strings (`campos_obrigatorios`) quais chaves o documento obrigatoriamente precisa ter para existir (Ex: no agendamento: `id_usuario`, `id_trilha`, `data_agendada`, `valor_pago`).
2. **Implementação da barreira de validação:** No início do método de inserção, crie uma estrutura de repetição (`for`) que varre a lista de campos obrigatórios verificando sua existência no dicionário de dados recebido da API.
3. **Tratamento de exceção de dados:** Caso algum campo falhe na checagem, interrompa o fluxo imediatamente retornando uma mensagem de erro clara indicando qual campo está ausente e o código de status HTTP `400 (Bad Request)`.
4. **Geração de Chave Primária Única (UUID):** Garanta que o ID do documento seja gerado via código utilizando `str(uuid.uuid4())`, evitando colisões ou sobreescritas acidentais no Firestore.
5. **Carimbo de data de servidor:** Adicione o campo `createdAt` utilizando a propriedade `firestore.SERVER_TIMESTAMP` para auditoria temporal confiável.
6. **Persistência Segura:** Utilize o método `.document(id).set(dados)` para gravar o registro na coleção correta.

* **Evidências esperadas:** Código-fonte estruturado contendo a validação por loop no arquivo da entidade correspondente dentro da pasta `services/`.
* **Critérios de sucesso:** O banco de dados rejeitar requisições incompletas com HTTP 400 e registrar com sucesso (HTTP 201) documentos completos com IDs únicos.
* **Referências utilizadas:** * FIREBASE. Firebase Admin Python SDK Documentation. Google, 2026.
  * ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR ISO 9001:2015: Sistemas de gestão da qualidade — Requisitos. Rio de Janeiro: ABNT, 2015.