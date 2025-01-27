"""API View Functions"""
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    """Home Api"""
    return JsonResponse({"message": "Mama we made it"})
