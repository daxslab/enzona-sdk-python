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
from enzona_sdk.payment import PaymentAPI
from enzona_payment import Payload2

# Creates an API instance
payment_api = PaymentAPI(use_sandbox=True)

# Get access token
access_token = payment_api.request_access_token('CUSTOMER_KEY', 'CUSTOMER_SECRET')

# Configure access token for authorization
payment_api.set_access_token(access_token)

# creates an api endpoint object
api_object = payment_api.create_payment()

# define parameters
payoad = Payload2(
    description='string',
    currency='CUP',
    amount={
        "total": 0.05,
        "details": {
            "shipping": 0.01,
            "tax": 0.01,
            "discount": 0.01,
            "tip": 0.01
        }
    },
    items=[
        {
            "name": "string",
            "description": "string",
            "quantity": 1,
            "price": 0.03,
            "tax": 0.01
        }
    ],
    merchant_op_id=123456789123,
    invoice_number=1212,
    return_url="https://mymerchant.cu/return",
    cancel_url="https://mymerchant.cu/cancel",
    terminal_id=12121,
    # buyer_identity_code="string"
)

# call endpoint
try:
    result = api_object.payments_post(payload=payoad)
    print(result)
except Exception as e:
    print('Exception when calling api_object.payments_post: '+ str(e))

```
