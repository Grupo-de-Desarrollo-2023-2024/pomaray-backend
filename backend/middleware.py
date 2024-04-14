# middleware.py

from django.http import HttpRequest
from backend.views import profile as profile_view

def profile_middleware(get_response):
    def middleware(request):
        profile_response = profile_view(request)
        request.profile_data = profile_response.data  # Guardar los datos de perfil en el objeto request
        return get_response(request)
    return middleware
