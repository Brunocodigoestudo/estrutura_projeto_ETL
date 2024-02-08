# Bem vinda(o) ao projeto de ETL

Para a documentação completa, visite [Meu Projeto](https://Brunocodigoestudo.github.io/estrutura_projeto_ETL/).

## Workflow

```mermaid
flowchart LR
    subgraph ETL[Pipeline]
        A(50 arquivos Excel) --> B[Extract: extract_from_excel]
        B[Extract: extract_from_excel] --> |Gera uma lista de Dataframes| C[Transformation: Consolidação do DataFrame]
        C[Transformation: Consolidação do DataFrame] -->|Gera um Dataframe Consolidado| D[Load: Converte para Excel]
        D(Load: Converte para Excel) --> |Salva o consolidado em Excel| E(Pasta Output: Um arquivo único Excel)

    end
```

# Função de EXTRAÇÃO de dados

### ::: app.pipeline.extract.extract_from_excel

# Função de TRANSFORMAÇÃO de dados

### ::: app.pipeline.transform.concat_data_frames

# Função de LOAD(CARGA NOS DADOS) de dados

### ::: app.pipeline.load.load_excel



