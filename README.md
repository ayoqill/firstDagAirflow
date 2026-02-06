# firstDagAirflow

## Project summary
This project is a small Apache Airflow setup running in Docker. It defines a single DAG (`my_dag`) with simple tasks that simulate model training, choose a best result, and branch to a success or failure message. The goal is to practice Airflow basics: DAG structure, scheduling, task dependencies, and the UI.

## notes: data engineering basics
Data engineering is about building reliable pipelines that move, transform, and monitor data so it is ready for analytics or ML. Airflow is one tool used to schedule and observe those pipelines.

Key ideas to remember:
- A DAG (Directed Acyclic Graph) is the pipeline: tasks plus their order.
- Tasks should return data (or produce artifacts) so downstream tasks can use it.
- Scheduling matters: `start_date` and `schedule` control when runs are created.
- The UI is for visibility: you can see runs, task states, logs, and retries.
- Failures are normal: read logs, fix the task code, and re-run.

How this project maps to those ideas:
- `dags/my_dag.py` defines the DAG and tasks.
- The training tasks return random scores, and the branch task chooses which path to take.
- Logs for each task are written under `logs/` for debugging.

What to try next:
- Replace the random number with a real computation or file read.
- Add a task that writes output to a file and another task that reads it.
- Change the schedule and observe how runs appear in the UI.

## student pov: what can i do with this dag
Think of this DAG as a simple classroom exercise that teaches the pipeline idea.

Example you can try (simple ETL flow):
1. Extract: read a local file (CSV) in a task.
2. Transform: clean the data (remove empty rows, convert types).
3. Load: write the cleaned data to another file.
4. Decide: use a branch task to send you to a "success" or "review" message.

Why this helps you learn:
- You see how tasks pass results using XCom.
- You practice debugging from logs when a task fails.
- You learn how schedules create automatic runs.

<img width="1906" height="992" alt="task instances" src="https://github.com/user-attachments/assets/abb5c3f7-8120-4d01-865b-0db9c1745554" />

<img width="1918" height="811" alt="my_dag" src="https://github.com/user-attachments/assets/a162a2da-32d4-46d1-bfee-b96d196980df" />

<img width="1917" height="871" alt="DAG showed graph" src="https://github.com/user-attachments/assets/97adeeb6-3e7c-4b79-88e4-47ad4139f397" />




