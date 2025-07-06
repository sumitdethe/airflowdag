from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello World 👋")

with DAG(
    dag_id="hello_world_trigger",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Only runs when manually triggered
    catchup=False,
    tags=["example"],
) as dag:

    task = PythonOperator(
        task_id="print_hello",
        python_callable=hello_world,
    )
