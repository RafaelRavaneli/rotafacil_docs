# Procedimento Operacional Padrão (POP 02)
## Modelagem e Consulta de Relacionamentos entre Documentos (NoSQL)

* **Objetivo:** Estabelecer um padrão de rastreabilidade e integridade referencial para vincular entidades distintas (ex: Usuários, Trilhas e Guias) dentro de uma coleção transacional (Agendamentos) em um banco NoSQL orientado a documentos.
* **Responsável:** Administrador de Banco de Dados (José Lucas).
* **Quando usar:** Durante a modelagem de entidades associativas ou criação de recursos que dependam de filtros cruzados e relatórios (métodos GET de listagem por ID).
* **Pré-requisitos:** Coleções principais (`usuarios` e `trilhas`) já existentes e populadas com IDs no formato string (UUID).

### Passo a Passo da Execução:
1. **Armazenamento de Chaves Estrangeiras:** Ao criar um documento dependente, salve as chaves das coleções pais de forma literal como propriedades de texto (Ex: guardar `id_usuario` e `id_trilha` dentro do documento da coleção `agendamentos`).
2. **Estruturação de Métodos de Busca (Queries):** Para consultar dados relacionados, crie métodos específicos utilizando os seletores lógicos do Firestore.
3. **Aplicação do filtro `.where()`:** Utilize a cláusula `.where('campo_estrangeiro', '==', id_buscado)` para filtrar a coleção de forma performática diretamente no servidor do Firebase, em vez de trazer todos os dados e filtrar na memória do Python.
4. **Consumo de Streams:** Execute o método `.stream()` para ler a resposta de forma otimizada.
5. **Serialização dos Dados:** Converta a resposta em uma lista de dicionários Python utilizando a função de compreensão de lista `[doc.to_dict() for doc in ref]` para entrega limpa ao desenvolvedor Back-end.

* **Evidências esperadas:** Métodos como `listar_agendamentos_usuario` e `listar_agendamentos_guia` implementados no arquivo `services/agendamentos.py`.
* **Critérios de sucesso:** Consultas retornando matrizes de dados filtradas corretamente por ID em tempo menor que 200ms, sem vazamento de dados de outros usuários.
* **Referências utilizadas:**
  * FIREBASE. Cloud Firestore Queries. Google, 2026. Disponível em: <https://firebase.google.com/docs/firestore/query-data/queries>.