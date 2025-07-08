{{ config(materialized='ephemeral') }}

WITH raw_hosts AS (
    SELECT *
    FROM {{ source('snowflake_db', 'RAW_HOSTS') }}
)

SELECT
    id AS host_id,
    NAME AS host_name,
    is_superhost,
    created_at,
    updated_at
FROM
    raw_hosts