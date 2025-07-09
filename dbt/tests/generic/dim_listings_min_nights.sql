{% test minimum_nights(model, column_name) %}

WITH validation AS (
    SELECT {{ column_name }} as test_field
    FROM {{ model }}

),

validation_errors AS (
    SELECT test_field
    FROM validation
    WHERE test_field < 1
    LIMIT 10
)

SELECT *
FROM validation_errors

{% endtest %}