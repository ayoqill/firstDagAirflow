from airflow import DAG
from datetime import datetime

from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from random import randint

def _choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=['training_model_A', 'training_model_B', 'training_model_C'])
    best_accuracy = max(accuracies)
    if(best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'

def _trainning_model():
    return randint(1,10)

# create a DAG instance/object
with DAG(
    dag_id='my_dag',
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:
    
    #task  
    train_model_A = PythonOperator(
        task_id='training_model_A',
        python_callable=_trainning_model
    )

    train_model_B = PythonOperator(
        task_id='training_model_B',
        python_callable=_trainning_model
    )

    train_model_C = PythonOperator(
        task_id='training_model_C',
        python_callable=_trainning_model
    )

    choose_model = BranchPythonOperator(
        task_id='choose_best_model',
        python_callable=_choose_best_model
    )

    accurate = BashOperator(
        task_id='accurate',
        bash_command='echo "The best model is accurate!"'
    )

    inaccurate = BashOperator(
        task_id='inaccurate',
        bash_command='echo "The best model is not accurate."'
    )

    # Set task dependencies
    [train_model_A, train_model_B, train_model_C] >> choose_model
    choose_model >> [accurate, inaccurate]