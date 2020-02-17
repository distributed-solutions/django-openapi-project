from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from rest_framework.status import HTTP_423_LOCKED

from .utils import get_user_jwt


class JWTAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware for authenticating JSON Web Tokens in Authorize Header.
    """
    @staticmethod
    def process_request(request):
        request.user = SimpleLazyObject(lambda: get_user_jwt(request))


class RestrictBlockedUsersMiddleware(MiddlewareMixin):
    """
    Отсекает запросы от заблокированных пользвателей с кодом - 423 Locked.
    """
    @staticmethod
    def process_request(request):
        if hasattr(request, 'user') and \
                request.user.is_authenticated and \
                request.user.is_restricted:
            return HttpResponse(status=HTTP_423_LOCKED)  # Locked
