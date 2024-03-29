from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.get_routes),
    path('projects/', views.get_projects),
    path('projects/<str:pk>/', views.get_project),
    path('projects/<str:pk>/vote/', views.project_vote),
    path('remove-tag/', views.delete_tag)
]
