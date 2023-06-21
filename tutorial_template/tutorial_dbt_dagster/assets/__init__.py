## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two

# /tutorial_template/tutorial_dbt_dagster/assets/__init__.py

import pandas as pd
from dagster import asset, file_relative_path
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_PATH = file_relative_path(__file__, "../../jaffle_shop")
DBT_PROFILES = file_relative_path(__file__, "../../jaffle_shop")


@asset(key_prefix=["jaffle_shop"], group_name="staging")
def customers_raw() -> pd.DataFrame:
    data = pd.read_csv("https://docs.dagster.io/assets/customers.csv")
    return data


@asset(key_prefix=["jaffle_shop"], group_name="staging")
def orders_raw() -> pd.DataFrame:
    data = pd.read_csv("https://docs.dagster.io/assets/orders.csv")
    return data


dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["jaffle_shop"]
)
