import json

import urllib3

SCOPE_PAYMENT = 'enzona_business_payment'
SCOPE_QR = 'enzona_business_qr'


class BaseAPI:


    host:str = ''

    api_host:str = 'https://api.enzona.net'

    api_sandbox_host:str = 'https://apisandbox.enzona.net'

    api_route:str = ''

    access_token_route:str = '/token'

    use_sandbox:str

    client:object

    config:object

    def __init__(self, use_sandbox=False, client=None, config=None):
        self.use_sandbox = use_sandbox
        self.client = client
        self.config = config
        self.host = self.api_sandbox_host if self.use_sandbox else self.api_host

    def request_access_token(self, customer_key, customer_secret, scopes=None):
        if not scopes:
            scopes = [SCOPE_PAYMENT]
        body_scopes = '+'.join(scopes)
        http = urllib3.PoolManager()
        url = self.host+self.access_token_route
        headers = urllib3.util.make_headers(
            basic_auth='{customer_key}:{customer_secret}'.format(
                customer_key=customer_key,
                customer_secret=customer_secret
            )
        )
        response = http.request('POST', url, fields={
            'grant_type': 'client_credentials',
            'scope': body_scopes
        }, headers=headers, encode_multipart=False)
        if response.status != 200:
            raise Exception('Error with status code: ' + str(response.status) + ' and body: ' + str(response.data))
        elif response.headers.get('Content-Type', None) != 'application/json':
            raise Exception('Invalid response content-type: ' + response.headers.get('content-type', None) + ' required: application/json')
        return json.loads(response.data.decode('utf-8')).get('access_token')

    def set_access_token(self, access_token):
        self.client.configuration.access_token = access_token
