"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from sms.views import ClientViewSet, MailingViewSet, MessageViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Service notification',
        default_version='v1',
        description="Cервис управления рассылками API администрирования и получения статистики, в котором реализованы: "
                    "методы создания новой рассылки, просмотра созданных и получения статистики по выполненным "
                    "рассылкам, сам сервис отправки уведомлений на внешнее API, организовано тестирование кода",
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='deriabin_85@mail.ru'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'mailings', MailingViewSet, basename='mailings')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('docs/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'
         )
]
