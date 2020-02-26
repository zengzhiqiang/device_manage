from django.urls import path, include
from rest_framework.routers import DefaultRouter
from device_manage_main import views
from rest_framework.urlpatterns import format_suffix_patterns

device_router = DefaultRouter()
device_router.register(r"devices", views.DeviceViewSet)
device_router.register(r'devicedetail', views.DeviceDetailViewSet)

urlpatterns = [
    path(r"search/<str:search_str>", views.DeviceSearchView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [path("", include(device_router.urls))]