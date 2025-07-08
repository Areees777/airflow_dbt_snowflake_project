{{ config(
        materialized = 'incremental',
        on_schema_change = 'fail',
        
)}}

WITH reviews AS (
    SELECT * FROM {{ ref('reviews') }}
)

SELECT *
FROM reviews
WHERE review_text IS NOT NULL
{% if is_incremental() %}
  and review_date >= (select max(review_date) from {{ this }})
{% endif %}