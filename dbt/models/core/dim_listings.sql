WITH cte_listings AS (
    SELECT *
    FROM {{ ref('listing') }}
)

SELECT 
    listing_id, 
    listing_name,
    room_type,
    CASE
        WHEN minimum_nights = 0 THEN 1
        ELSE minimum_nights
    END AS minimum_nights,
    host_id,
    TO_NUMBER(REPLACE(price_str, '$', '')) AS price,
    created_at,
    updated_at
FROM cte_listings