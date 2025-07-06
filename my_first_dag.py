from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello from KubernetesExecutor 👋")

with DAG(
    dag_id="hello_world_k8s",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=["kubernetes"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello_world,
    )
