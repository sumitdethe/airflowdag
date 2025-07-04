from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_airflow():
    print("Hello from your first DAG!")

with DAG(
    dag_id='my_first_dag',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"]
    # No schedule → manual trigger only
) as dag:
    task1 = PythonOperator(
        task_id='say_hello',
        python_callable=hello_airflow
    )
