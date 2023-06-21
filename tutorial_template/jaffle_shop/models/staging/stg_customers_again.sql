select
    id as another_customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop', 'customers_raw') }}

