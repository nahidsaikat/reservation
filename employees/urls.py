from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"employee", views.EmployeeViewSet, basename="employee")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
