{% snapshot listings %}

{{
    config(
        target_schema='RAW',
        unique_key='id',
        strategy='timestamp',
        updated_at='updated_at',
        invalidate_hard_deletes=True
    )
}}

SELECT * FROM {{ source('snowflake_db', 'RAW_LISTINGS') }}

{% endsnapshot %}