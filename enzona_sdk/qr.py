from enzona_qr import Configuration, PermiteCrearUnQRDePagoAUnComercioApi, \
    PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api, ObtieneLaInformacinDeUnQRApi, ApiClient

from enzona_sdk.base import BaseAPI, SCOPE_QR


class QrAPI(BaseAPI):

    api_route:str = '/qr/v1.0.0'

    config:Configuration

    def __init__(self, use_sandbox=False, client=None, config=None):
        super().__init__(use_sandbox, client, config)
        if not self.config:
            self.config = Configuration()
            self.config.host = self.host + self.api_route
        if not client:
            self.client = ApiClient(configuration=self.config)

    def request_access_token(self, customer_key, customer_secret, scopes=None):
        if not scopes:
            scopes = [SCOPE_QR]
        return super().request_access_token(customer_key, customer_secret, scopes)

    def create_qr_merchant(self)->PermiteCrearUnQRDePagoAUnComercioApi:
        return PermiteCrearUnQRDePagoAUnComercioApi(api_client=self.client)

    def create_qr_account(self)->PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api:
        return PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api(api_client=self.client)

    def qr_code(self)->ObtieneLaInformacinDeUnQRApi:
        return ObtieneLaInformacinDeUnQRApi(api_client=self.client)
