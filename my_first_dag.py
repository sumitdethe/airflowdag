from airflow.decorators import dag, task
from datetime import datetime
import subprocess

@dag(
    dag_id="hello_world_k8s",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example", "k8s"],
)
def hello_world_dag():
    @task
    def print_hello():
        print("👋 Hello from Airflow 3.0 on GKE with KubernetesExecutor!")

    @task
    def list_gke_clusters():
        try:
            result = subprocess.run(
                ["gcloud", "container", "clusters", "list"],
                capture_output=True,
                text=True,
                check=True
            )
            print("Clusters:\n", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error running gcloud:", e.stderr)

    print_hello() >> list_gke_clusters()

dag = hello_world_dag()
