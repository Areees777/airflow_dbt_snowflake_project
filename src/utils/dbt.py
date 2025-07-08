from cosmos import (
    ExecutionConfig,
    ExecutionMode,
    LoadMode,
    ProfileConfig,
    ProjectConfig,
    TestBehavior,
)

DBT_EXECUTABLE_PATH = "/usr/local/airflow/dbt/dbt_venv/bin/dbt"

# Execution configuration
COSMOS_EXECUTION_CONFIG = ExecutionConfig(execution_mode=ExecutionMode.LOCAL, dbt_executable_path=DBT_EXECUTABLE_PATH)

COSMOS_RENDER_CONFIG = {
    "emit_datasets": False,
    "test_behavior": TestBehavior.AFTER_EACH,
    "load_method": LoadMode.CUSTOM,
    "dbt_deps": False,
}

DEFAULT_AIRFLOW_TO_DBT_VARS = {
    "data_interval_start": "{{ data_interval_start.in_timezone(dag.timezone)}}",
    "run_id": "{{ run_id }}",
    "time_zone": "{{ dag.timezone }}",
}


def get_profile_config() -> ProfileConfig:
    return ProfileConfig(
        profile_name="snowflake_profile",
        target_name="dev",
        profiles_yml_filepath="/usr/local/airflow/dbt/airbnb/profiles.yml",
    )


def get_cosmos_base_config(
    dbt_vars: dict[str, str] | None = DEFAULT_AIRFLOW_TO_DBT_VARS,
):
    project_config = ProjectConfig(
        dbt_project_path="/usr/local/airflow/dbt/airbnb",
        dbt_vars=dbt_vars,
        partial_parse=False,
    )

    return {
        "project_config": project_config,
        "execution_config": COSMOS_EXECUTION_CONFIG,
    }