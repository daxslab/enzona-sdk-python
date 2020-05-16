from enzona_payment import Configuration, PermiteCrearUnPagoApi, PermiteConfirmarUnPagoApi, PermiteCancelarUnPagoApi, \
    PermiteCompletarUnPagoApi, ObtieneListadoDePagosRealizadosApi, ObtieneLosDetallesDeUnPagoRealizadoApi, \
    PermiteRealizarElCheckoutDeUnPagoApi, PermiteRealizarLaDevolucinDeUnPagoApi, ListaDeDevolucionesDeUnPagoApi, \
    ObtieneLosDetallesDeUnaDevolucinRealizadaApi, ObtieneUnListaDeDevolucionesRealizadasApi, \
    PermiteCrearUnRecieveCodeApi, ApiClient

from enzona_sdk.base import BaseAPI


class PaymentAPI(BaseAPI):

    api_route:str = '/payment/v1.0.0'

    config:Configuration

    def __init__(self, use_sandbox=False, client=None, config=None):
        super().__init__(use_sandbox, client, config)
        if not self.config:
            self.config = Configuration()
            self.config.host = self.host + self.api_route
        if not client:
            self.client = ApiClient(configuration=self.config)

    def create_payment(self) -> PermiteCrearUnPagoApi:
        return PermiteCrearUnPagoApi(api_client=self.client)

    def confirm_payment(self) -> PermiteConfirmarUnPagoApi:
        return PermiteConfirmarUnPagoApi(api_client=self.client)

    def cancel_payment(self) -> PermiteCancelarUnPagoApi:
        return PermiteCancelarUnPagoApi(api_client=self.client)

    def complete_payment(self) -> PermiteCompletarUnPagoApi:
        return PermiteCompletarUnPagoApi(api_client=self.client)

    def list_payment(self) -> ObtieneListadoDePagosRealizadosApi:
        return ObtieneListadoDePagosRealizadosApi(api_client=self.client)

    def details_payment(self) -> ObtieneLosDetallesDeUnPagoRealizadoApi:
        return ObtieneLosDetallesDeUnPagoRealizadoApi(api_client=self.client)

    def checkout_payment(self) -> PermiteRealizarElCheckoutDeUnPagoApi:
        return PermiteRealizarElCheckoutDeUnPagoApi(api_client=self.client)

    def refund_payment(self) -> PermiteRealizarLaDevolucinDeUnPagoApi:
        return PermiteRealizarLaDevolucinDeUnPagoApi(api_client=self.client)

    def list_refunds_payment(self) -> ListaDeDevolucionesDeUnPagoApi:
        return ListaDeDevolucionesDeUnPagoApi(api_client=self.client)

    def refund_details(self) -> ObtieneLosDetallesDeUnaDevolucinRealizadaApi:
        return ObtieneLosDetallesDeUnaDevolucinRealizadaApi(api_client=self.client)

    def list_refunds(self) -> ObtieneUnListaDeDevolucionesRealizadasApi:
        return ObtieneUnListaDeDevolucionesRealizadasApi(api_client=self.client)

    def create_receive_code(self) -> PermiteCrearUnRecieveCodeApi:
        return PermiteCrearUnRecieveCodeApi(api_client=self.client)
