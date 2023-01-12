from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('warehouses/<int:pk>/update/', WarehouseViewSet.as_view({'patch': 'update_warehouse'})),
    path('warehouses/<int:pk>/delete/', WarehouseViewSet.as_view({'delete': 'delete_warehouse'})),
]