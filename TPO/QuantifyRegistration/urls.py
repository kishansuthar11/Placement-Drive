from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("api/", include(router.urls)),
]
