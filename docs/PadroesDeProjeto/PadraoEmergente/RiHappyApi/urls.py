from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departmentViewSet, name='departments'),
    path('departments/<int:id>/', views.departmentViewSet, name='department-detail'),
    path('products/', views.productViewSet, name='products'),
    path('products/<int:id>/', views.productViewSet, name='product-detail'),
]
