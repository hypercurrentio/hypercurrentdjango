from django.conf import settings
import hypercurrent_metering
from hypercurrent_metering.rest import ApiException


class HyperCurrentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        HC_API_KEY = getattr(settings, 'HYPERCURRENT_API_KEY', None)
        HC_API_URL = getattr(settings, 'HYPERCURRENT_API_URL', "https://api.hypercurrent.io/meter/v1/api")

        self.hypercurrent = hypercurrent_metering.MeteringControllerApi(hypercurrent_metering.ApiClient())
        self.hypercurrent.api_client.default_headers["x-api-key"] = HC_API_KEY
        self.hypercurrent.api_client.configuration.host = HC_API_URL

    def __call__(self, request):

        HC_METADATA_HEADER = getattr(settings, 'HYPERCURRENT_METADATA_HEADER', None)
        HC_APPLICATION_HEADER = getattr(settings, 'HYPERCURRENT_APPLICATION_HEADER', "clientId")

        response = self.get_response(request)

        body = hypercurrent_metering.MeteringRequestDTO(
            application=request.headers.get(HC_APPLICATION_HEADER, 'clientId'),
            method="GET",
            url=request.path,
            response_code=response.status_code,
            request_headers=list(request.headers.items()),
            response_headers=list(response.headers.items()),
            content_type=response.headers['Content-Type'],
            remote_host=response.headers['x-forwarded-for'],
            request_message_size=request.headers['content-length'],
            response_message_size=request.headers['content-length'],
            metadata=response[HC_METADATA_HEADER],
            user_agent=request.headers['user-agent'],
        )

        try:
            self.hypercurrent.meter(body)
        except ApiException as e:
            print(f"Exception when metering API request: {e}")

        return response
