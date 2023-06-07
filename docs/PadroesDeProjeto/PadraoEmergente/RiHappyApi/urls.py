from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departmentViewSet, name='departments'),
    path('departments/<int:id>/', views.departmentViewSet, name='department-detail'),
]
