# Unofficial Python SDK for EnZona

***This is a work in progress, there are rough corners and the 
API can change witouth previuos warnings. 
Not recommended for production usage.***

This is a Python library that allows interaction with 
[EnZona's API](https://api.enzona.net).

## Requeriments

Python 3.0 and later

## Installation & Usage

To install via pip run:

`pip install git+https://github.com/daxslab/enzona-sdk-python@master#egg=enzona-sdk`

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from enzona_sdk.payments import PaymentAPI

# Creates an API instance
payment_api = PaymentAPI(use_sandbox=True)

# Get access token
access_token = payment_api.request_access_token('CUSTOMER_KEY', 'CUSTOMER_SECRET')

# Configure access token for authorization
payment_api.set_access_token(access_token)

# creates an api endpoint object
api_object = payment_api.list_refunds_payment()

# define parameters
transaction_uuid = "transaction_uuid_example"
limit = "limit_example"
offset = "offset_example"
status_filter = "status_filter_example"
start_date_filter = "start_date_filter_example"
end_date_filter = "end_date_filter_example"
order_filter = "order_filter_example"

# call endpoint
try:
    result = api_object.payments_transaction_uuid_refunds_get(
        transaction_uuid=transaction_uuid,
        limit=limit,
        offset=offset,
        status_filter=status_filter,
        start_date_filter=start_date_filter,
        end_date_filter=end_date_filter,
        order_filter=order_filter
    )
    print(result)
except Exception as e:
    print('Exception when calling api_object.payments_transaction_uuid_refunds_get: '+ str(e))

```
