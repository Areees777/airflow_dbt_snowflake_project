{% macro to_date_column(column_name) %}
    TO_DATE({{ column_name }})
{% endmacro %}