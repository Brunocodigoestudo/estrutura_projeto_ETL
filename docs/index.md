# Bem vinda(o) ao projeto de ETL

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

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
