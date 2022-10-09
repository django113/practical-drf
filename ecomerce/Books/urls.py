from django.urls import path, include

urlpatterns = [
    path('api/admin/v1/', include('Books.api_v1_admin.urls')),    
]
