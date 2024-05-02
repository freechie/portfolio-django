from django.utils.crypto import get_random_string
import base64


class NonceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        nonce = base64.b64encode(get_random_string(
            length=16).encode()).decode('utf-8')
        request.nonce = nonce
        response = self.get_response(request)
        response['Content-Security-Policy'] = f"style-src 'self' 'nonce-{nonce}'; script-src 'self' 'nonce-{nonce}';"
        return response
