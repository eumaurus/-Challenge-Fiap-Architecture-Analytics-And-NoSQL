from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pymongo import MongoClient
import csv, os

CSV_PATH = "/opt/airflow/data/massa_de_dados.csv"
MONGO_URI = "mongodb://mongoadmin:datatrip@mongodb:27017/"
DB_NAME = "clickbus"
COLLECTION = "compras"

#carregando dados
def load_csv_to_mongo():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError("Arquivo CSV não encontrado: ")
    
#loop de leitura
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

#conexão com o mongo
    client = MongoClient(MONGO_URI)
    col = client[DB_NAME][COLLECTION]
    if rows:
        col.insert_many(rows)
        print(f"Inseridos {len(rows)} documentos na base de dados")

with DAG(
    dag_id="csv_to_mongo",
    start_date=datetime(2025, 8, 1),
    schedule=None,
    catchup=False
) as dag:
    insert_task = PythonOperator(
        task_id="load_csv",
        python_callable=load_csv_to_mongo
    )
