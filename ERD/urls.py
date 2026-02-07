from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ERD1.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Your CRUD lives here!
]