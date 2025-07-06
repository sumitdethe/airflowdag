from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="hello_world_k8s",
    start_date=datetime(2023, 1, 1),
    schedule=None,            # Manual trigger only
    catchup=False,
    tags=["example", "k8s"],
)
def hello_world_dag():
    @task
    def print_hello():
        print("👋 Hello from Airflow 3.0 on GKE with KubernetesExecutor!")

    print_hello()

dag = hello_world_dag()
