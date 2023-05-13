from  django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.permissions import AllowAny
from django.urls import path,include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


doc=get_schema_view(
    
    openapi.Info(
    title="Sos docta API",
    default_version="v1",
    description="cet api a été conçue en vue l' application SOS-DOKTA  du gsdcucb pour le solution challenge",
    contact=openapi.Contact(email="augustinnjuc `i@gmail.com"),
    license=openapi.License(name="BSD Licence"),    
    ),
    public=True,
    permission_classes=[AllowAny],
)

api1="apihopital/"
api="accounts/"

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path("",include("SOS.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', doc.without_ui(cache_timeout=0), name='schema-json'),
     re_path(r'^swagger/$', doc.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', doc.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(api,include("accounts.urls"))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)