# Projeto criação da estrtura do zero de ETL com python
## Descrição

Este projeto Python foi desenvolvido para simplificar o processo de Extração, Transformação e Carga (ETL) de dados provenientes de arquivos Excel (.xlsx). Com um conjunto robusto de funcionalidades, o projeto facilita a coleta, consolidação e exportação eficiente de dados, visando simplificar tarefas recorrentes de manipulação de dados.

Principais Funcionalidades:

1.  Extração de Dados:

- Uma função dedicada lê arquivos Excel de um diretório específico, gerando uma lista de dataframes Pandas. Cada dataframe representa os dados de um arquivo Excel individual.

2. Transformação de Dataframes:

- Uma função realiza a transformação dos dataframes individuais em um único dataframe consolidado, proporcionando uma visão unificada dos dados.

3. Exportação para Excel:

- Uma funcionalidade permite exportar o dataframe consolidado para um novo arquivo Excel, facilitando a visualização e o compartilhamento dos dados transformados.
  
4. Características de Carregamento (Load):

 - Para o carregamento dos dados consolidados, foi implementada uma função que recebe um dataframe e o salva como um arquivo Excel no diretório especificado. Essa função é útil para garantir a persistência das transformações realizadas.

## Utilização:
Este projeto é importante em cenários onde dados estão distribuídos em vários arquivos Excel, e a consolidação é necessária para análises mais eficientes.

## Instruções de Uso:
 - Versão de Python 3.11.5
 
 - Roadar pipeline:
   task start

## Licença:

Distribuído sob a licença MIT, este projeto promove a liberdade de uso e modificação.

## Fluxo
![pipeline](https://github.com/Brunocodigoestudo/imagens/blob/69f9c06a9fcd11a4c4834294144dba21062d3891/pipeline.png)
