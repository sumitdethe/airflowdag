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
        # Step 1: Install gcloud SDK
        install_script = """
        apt-get update && apt-get install -y curl gnupg apt-transport-https ca-certificates &&
        echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
            | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list &&
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
            | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - &&
        apt-get update && apt-get install -y google-cloud-sdk
        """
        subprocess.run(["bash", "-c", install_script], check=True)

        # Step 2: Run gcloud command (e.g., list GKE clusters)
        result = subprocess.run(
            ["gcloud", "container", "clusters", "list"],
            capture_output=True, text=True
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)

    print_hello() >> list_gke_clusters()

dag = hello_world_dag()
