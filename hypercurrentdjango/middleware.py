from django.http import HttpResponse
import hypercurrent_metering
import os
from hypercurrent_metering.rest import ApiException

class HypercurrentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Set up the Hypercurrent API client once
        self.hypercurrent = hypercurrent_metering.MeteringControllerApi(hypercurrent_metering.ApiClient())
        self.hypercurrent.api_client.default_headers["x-api-key"] = os.environ.get('HYPERCURRENT_API_KEY')
        self.hypercurrent.api_client.configuration.host = os.environ.get('HYPERCURRENT_API_URL',"https://api.hypercurrent.io/meter/v1/api")

    def __call__(self, request):
        response = self.get_response(request)

        body = hypercurrent_metering.MeteringRequestDTO(
            application=request.headers.get('clientId', None),
            method="GET", # REQUIRED
            url=request.path, # REQUIRED
            response_code=response.status_code,
            request_headers=[], # REQUIRED (but can be empty)
            response_headers=[], # REQUIRED (but can be empty)
        )

        """
        # After processing the request and getting the response, send the data to Hypercurrent
        body = hypercurrent_metering.MeteringRequestDTO(
            application=request.headers.get('clientId', None),
            method=request.method,
            url=request.path,
            request_headers=list(request.headers.items()),  # Convert the header to a list of tuples
            response_headers=list(response.headers.items()),
            response_code=response.status_code,
            content_type=response['Content-Type'],
            # Add any other necessary fields here, possibly extracting more info from request and response
        )
        """

        try:
            self.hypercurrent.meter(body)
        except ApiException as e:
            print(f"Exception when metering API request: {e}")

        return response

