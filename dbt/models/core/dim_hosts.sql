WITH hosts AS (
    SELECT *
    FROM {{ ref('hosts') }}
)

SELECT
    host_id,
    COALESCE(host_name, 'Anonynous') AS host_name,
    is_superhost,
    created_at,
    updated_at
FROM hosts