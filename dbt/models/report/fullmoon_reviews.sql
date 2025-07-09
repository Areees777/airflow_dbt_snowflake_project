{{ config(
    alias='fullmoon_reviews',
    materialized = 'table'
) }}

WITH fct_reviews AS (
    SELECT * FROM {{ ref('fct_reviews') }}
),

full_moon_dates AS (
    SELECT * FROM {{ ref('seed_full_moon_dates') }}
)

SELECT
    r.listing_id,
    {{ to_date_column("r.review_date") }} AS review_date,
    r.reviewer_name,
    r.review_text,
    r.review_sentiment,
    CASE
        WHEN fm.full_moon_date IS NULL THEN 'not full moon'
    ELSE 'full moon'
    END AS is_full_moon
FROM fct_reviews r
LEFT JOIN full_moon_dates fm
ON (TO_DATE(r.review_date) = DATEADD(DAY, 1, fm.full_moon_date))