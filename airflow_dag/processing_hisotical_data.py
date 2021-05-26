import logging
import os
import sys

from airflow import DAG
#from airflow.hooks import PythonOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime


args = {
            'owner': 'airflow',
            'start_date': datetime(2021, 5, 1),
            'provide_context': True
       }

dag = DAG(
            'procress_history_data',
            start_date = datetime(2019, 5, 1),
            schedule_interval = '@once',
            default_args = args
        )

historical_data_ingestion = BashOperator(
                            task_id='ingset_historical_data',
                            bash_command='python {{ params.file }}',
                            params={'file':'/mnt/d/d/self/interviews/assignment_ganit/venv/historical_data_ingestion/main.py'},
                            dag=dag
                            )

make_zip = BashOperator(
                            task_id='zip_source_code',
                            bash_command='python {{ params.file }}',
                            params={'file':'/mnt/d/d/self/interviews/assignment_ganit/venv/zip_builder/main.py'},
                            dag=dag
                        )

process_historical_data = BashOperator(
					task_id='processing_history_data',
                    bash_command='spark-submit --packages {{ params.package }} --py-files {{ params.pyfiles }} {{ params.file }}',
                    params={'package': 'org.mongodb.spark:mongo-spark-connector_2.11:2.4.0', 'pyfiles': '/mnt/d/d/self/interviews/assignment_ganit/venv/zip_builder/src.zip', 'file':'/mnt/d/d/self/interviews/assignment_ganit/venv/historical_data_processing/main.py'},
                    #  bash_command = 'echo $SPARK_HOME',
                    dag=dag
                    )

historical_data_ingestion >> make_zip >> process_historical_data