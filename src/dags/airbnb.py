from airflow.decorators import dag, task_group
from airflow.operators.empty import EmptyOperator
from cosmos import DbtTaskGroup, RenderConfig
from pendulum import datetime

from utils.dbt import COSMOS_RENDER_CONFIG, get_cosmos_base_config, get_profile_config


@dag(
    dag_id='airbnb',
    description="This dag is to read and write data in Snowflake.",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 1},
    tags=["example"],
)
def airbnb_dag():
    start_task = EmptyOperator(task_id="start")
    end_task = EmptyOperator(task_id="end")

    # Cosmos version should be ^1.9.0
    # def dbt_freshness():
    #     return DbtTaskGroup(
    #         group_id="dbt_freshness",
    #         dbt_command="source freshness",
    #         profile_config=get_profile_config(),
    #         render_config=RenderConfig(**COSMOS_RENDER_CONFIG),
    #         **get_cosmos_base_config(),
    #     )


    def load_seeds():
        return DbtTaskGroup(
            group_id="dbt_seeds",
            profile_config=get_profile_config(),
            render_config=RenderConfig(**COSMOS_RENDER_CONFIG, select=["path:seeds"]),
            **get_cosmos_base_config(),
        )

    def run_snapshots():
        return DbtTaskGroup(
            group_id="dbt_snapshots",
            profile_config=get_profile_config(),
            render_config=RenderConfig(**COSMOS_RENDER_CONFIG, select=["path:snapshots"]),
            **get_cosmos_base_config(),
        )

    def stage_models():
        return DbtTaskGroup(
            group_id="dbt_stage",
            profile_config=get_profile_config(),
            render_config=RenderConfig(**COSMOS_RENDER_CONFIG, select=["path:models/stage"]),
            **get_cosmos_base_config(),
        )
    
    def core_models():
        return DbtTaskGroup(
            group_id="dbt_core",
            profile_config=get_profile_config(),
            render_config=RenderConfig(**COSMOS_RENDER_CONFIG, select=["path:models/core"]),
            **get_cosmos_base_config(),
        )

    def report_models():
        return DbtTaskGroup(
            group_id="dbt_report",
            profile_config=get_profile_config(),
            render_config=RenderConfig(**COSMOS_RENDER_CONFIG, select=["path:models/report"]),
            **get_cosmos_base_config(),
        )
    
    # freshness_task = dbt_freshness()
    load_seeds_task = load_seeds()
    run_snapshots_task = run_snapshots()
    stg_dbt_models_task = stage_models()
    core_dbt_models_task = core_models()
    report_dbt_models_task = report_models()

    start_task >> load_seeds_task >> run_snapshots_task >> stg_dbt_models_task
    stg_dbt_models_task >> core_dbt_models_task
    core_dbt_models_task >> report_dbt_models_task >> end_task


airbnb_dag()