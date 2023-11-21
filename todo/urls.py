from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()
router.register(r"task", views.TaskViewSet)
router.register(r"user", views.UserViewSet)
router.register(r"history", views.HistoryViewSet)
router.register(r"file", views.FileViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('login/',views.LoginViewSet.as_view({'post': 'create'}),name="schema"),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),

]
