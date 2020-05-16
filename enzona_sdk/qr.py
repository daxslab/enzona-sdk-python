from enzona_qr import Configuration, PermiteCrearUnQRDePagoAUnComercioApi, \
    PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api, ObtieneLaInformacinDeUnQRApi, ApiClient

from enzona_sdk.base import BaseAPI


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

    def create_qr_merchant(self)->PermiteCrearUnQRDePagoAUnComercioApi:
        return PermiteCrearUnQRDePagoAUnComercioApi(api_client=self.client)

    def create_qr_account(self)->PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api:
        return PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api(api_client=self.client)

    def qr_code(self)->ObtieneLaInformacinDeUnQRApi:
        return ObtieneLaInformacinDeUnQRApi(api_client=self.client)
