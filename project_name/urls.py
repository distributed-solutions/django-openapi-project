""" {{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.contrib import admin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

from core.views import ping

# Schema and API docs
schema_view = get_schema_view(
    openapi.Info(
        title='Safe Tec API',
        default_version='v1',
        # contact=openapi.Contact(email=""),
        # license=openapi.License(name="Private License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

docs_view = include_docs_urls(
    permission_classes=(permissions.AllowAny,)
)

# Default router
router = DefaultRouter()
router.register(r'events', AuditViewSet)

# Urlpattern
urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('schema-swagger-ui')), name='index'),
    url(r'^ping/$', ping, name='ping'),
    url(r'^docs/', docs_view),

    # OpenAPI schema & docs
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    # API v1
    url(r'^v1/', include((router.urls, 'v1'), namespace='v1')),
    url(r'^v1/login/$', ObtainJSONWebToken.as_view(), name='login'),
    url(r'^v1/refresh_token/$', RefreshJSONWebToken.as_view(), name='refresh_token'),

    # Control panel
    url(r'^admin/', admin.site.urls),
]
