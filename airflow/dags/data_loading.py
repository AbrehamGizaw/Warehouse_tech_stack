from airflow import DAG
from airflow.providers.bash.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': '{{ var.value.start_date }}',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='data_loading_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Adjust schedule as needed
) as dag:

    load_data_from_source = BashOperator(
        task_id='load_data_from_source',
        bash_command='python /path/to/your_etl_script.py {{ var.value.data_dir }}'
    )
