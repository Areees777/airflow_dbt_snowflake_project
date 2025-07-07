FROM quay.io/astronomer/astro-runtime:12.8.0

# Crear un entorno virtual Python específico para dbt en /dbt/dbt_venv,
# instalar dbt-core y dbt-snowflake dentro de ese entorno para aislar dependencias.
# La activación del entorno virtual con `source` en RUN no persiste entre capas,
# por eso modificamos la variable PATH para que use los ejecutables del venv por defecto.
RUN python -m venv dbt/dbt_venv && source dbt/dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-core==1.9.4 dbt-snowflake==1.9.4 && deactivate

# Ajustamos PATH para que todos los comandos usen el entorno virtual automáticamente.
ENV PATH="/dbt/dbt_venv/bin:$PATH"