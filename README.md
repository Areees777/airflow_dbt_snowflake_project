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

[Airbnb Raw Data in Snowflake]  -->  [Apache Airflow (Orchestrates dbt)]  -->  [dbt (Transform & Model Data)]  -->  [Final Tables in Snowflake]


### 📊 dbt Models

The transformation logic is organized inside the `models/` directory of dbt, and includes:

- **Staging models** (`stg_`) that clean and rename raw data from Snowflake  
- **Intermediate and final models** for analytics and reporting  
- **Schema tests** defined in YAML files to ensure data quality (e.g., non-null, unique)

---

### 🧠 What I Learned

- How to integrate **Airflow** and **dbt** to build orchestrated transformation pipelines  
- Best practices for organizing dbt models, using modular SQL and schema validation  
- How to securely connect and authenticate with **Snowflake** from containers  
- How to build **reproducible** and **scalable** data engineering workflows using **Docker**

