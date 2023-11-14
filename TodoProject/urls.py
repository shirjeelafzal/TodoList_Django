
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from todo import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router=DefaultRouter()
router.register(r"task",views.TaskViewSet)
router.register(r"user",views.UserViewSet)
router.register(r"history",views.HistoryViewSet)
router.register(r"file",views.FileViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/schema/',SpectacularAPIView.as_view(),name="schema"),
    path('api/schema/docs/',SpectacularSwaggerView.as_view(url_name="schema")),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
