from datetime import datetime, timedelta

from airflow import DAG
from airflow.configuration import conf
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

namespace = conf.get('kubernetes', 'NAMESPACE')
# This will detect the default namespace locally and read the
# environment namespace when deployed to Astronomer.
in_cluster = True
config_file = None
if namespace == 'default':
    config_file = 'include/.kube/config'
    in_cluster = False

with DAG(
        dag_id='bulk_sign_process',
        schedule_interval=None,
        owner='airflow',
        depends_on_past=False,
        start_date=datetime(2022, 1, 1),
        email_on_failure=False,
        retries=1,
) as dag:
    KubernetesPodOperator(
        namespace=namespace,
        image="bulksend_test",
        labels={},
        name="airflow-test-pod",
        image_pull_policy="Never",
        env_vars={
            'V4_BASE_URL': '{{ var.value.V4_BASE_URL }}',
        },
        cmds=[
            "python", "run.py",
            "--X_REAL_IP", "{{ dag_run.conf['X_REAL_IP'] }}",
            "--parallel_key", "{{ dag_run.conf['parallel_key']|tojson }}",
            "--recipients", "{{ dag_run.conf['recipients']|tojson  }}",
            "--resource_hash", "{{ dag_run.conf['resource_hash'] }}"
        ],
        task_id="task-one",
        in_cluster=in_cluster,
        cluster_context="docker-desktop",
        config_file=config_file,
        is_delete_operator_pod=True,
        get_logs=True,
    )
