from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from json_reader import read_json_files_in_folder
from data_transformer import transform_json_to_dataframe


folder_path = '/content/source'
default_args = {
    'owner': 'Faurel Gema',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
def export_to_parquet():
    json_data = read_json_files_in_folder(folder_path)


    df = transform_json_to_dataframe(json_data)


    df.to_parquet('/path/to/your/output/file.parquet', index=False)  
with DAG(
    dag_id='DAG_Faurel_Gema',
    default_args=default_args,
    description='A DAG to export JSON data to Parquet',
    schedule_interval='0 11 * * *',  
    tags=['DE', 'TechnicalTest', 'Faurel Gema']
) as dag:

    export_to_parquet_task = PythonOperator(
        task_id='export_to_parquet',
        python_callable=export_to_parquet,
    )
