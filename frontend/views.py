from django.shortcuts import render
from django.utils.crypto import get_random_string


def index(request):
    # Generate a random nonce value
    csp_nonce = get_random_string(20)
    context = {
        'csp_nonce': csp_nonce,
    }
    return render(request, 'frontend/index.html', context)
