from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from airflow.operators.bash import bash
from datetime import datetime

@dag(
    dag_id="test_gcp_auth_k8s",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["gcp", "k8s", "auth", "test"],
)
def test_gcp_auth_k8s():
    
    @bash
    def check_gcp_auth():
        return """
        echo "🔒 Checking GCP auth context..."
        gcloud auth list
        echo "🔍 Listing GKE clusters..."
        gcloud container clusters list --zone us-central1-a --project eighth-epigram-462408-d6
        """

    check_gcp_auth()

dag = test_gcp_auth_k8s()
