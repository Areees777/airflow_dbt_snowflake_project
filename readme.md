# 🧩 Airflow + dbt + Snowflake Project

This project showcases an end-to-end data pipeline using **Apache Airflow** to orchestrate transformation workflows with **dbt**, working directly from data already loaded into **Snowflake**. The entire environment is containerized with Docker and Docker Compose.

---

## 📌 Overview

- Start with raw Airbnb data already stored in **Snowflake**
- Orchestrate transformation pipelines with **Apache Airflow**
- Clean and model data using **dbt**
- Produce analytics-ready tables in Snowflake
- Run the entire process in a reproducible, containerized environment

---

## ⚙️ Technologies Used

- [Apache Airflow](https://airflow.apache.org/)
- [dbt (Data Build Tool)](https://www.getdbt.com/)
- [Snowflake](https://www.snowflake.com/)
- Docker & Docker Compose
- Python 3.x

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Raw Airbnb Data in Snowflake] --> B[Airflow DAG]
    B --> C[dbt Transformations]
    C --> D[Snowflake (Modeled Tables)]
