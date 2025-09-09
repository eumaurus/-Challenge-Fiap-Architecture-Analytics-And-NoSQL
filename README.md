# -Challenge-Fiap-Architecture-Analytics-And-NoSQL
About Intregração do banco de dados MongoDB, com pipeline de dados orquestrado pelo airflow no Container Docker

Documentação do Projeto

Introdução: Este projeto tem como objetivo criar um fluxo de dados automatizado usando o Apache Airflow e o MongoDB. A ideia é pegar informações do arquivo CSV fornecido pela ClickBus e salvar esses dados no banco de dados NoSQL Mongo DB , como solicitado. A base de dados não foi anexada no github por questões de segurança.

Objetivos: Criar um fluxo que leia dados de um arquivo CSV e carregue no MongoDB usando o Airflow e python juntamente com a biblioteca PyMongo para ingestão de dados.

Metodologia: Primeiramnete criando o ambiente com containers Docker instalando Airflow e MongoDB, depois fazer a DAG no Airflow para ler o arquivo CSV usando Python e PyMongo para inserir os dados no banco, e depois rodar o código para verificação de tarefa.

Resultados Esperados: Automação na carga de dados e arquivo CSV salvos no banco Mongo DB de forma organizada;
