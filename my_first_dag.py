from airflow.decorators import dag, task
from datetime import datetime
import subprocess
import os

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
    def install_gcloud_and_list_clusters():
        # Step 1: Download and extract gcloud SDK
        subprocess.run([
            "bash", "-c",
            """
            curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz &&
            tar -xf google-cloud-cli-linux-x86_64.tar.gz &&
            ./google-cloud-sdk/install.sh --quiet
            """
        ], check=True)

        # Step 2: Export PATH so `gcloud` is found
        os.environ["PATH"] = f"{os.getcwd()}/google-cloud-sdk/bin:" + os.environ["PATH"]

        # Step 3: Use gcloud directly (auth via Workload Identity)
        result = subprocess.run(
            ["gcloud", "container", "clusters", "list"],
            capture_output=True, text=True
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)

    print_hello() >> install_gcloud_and_list_clusters()

dag = hello_world_dag()
