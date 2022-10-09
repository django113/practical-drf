from django.urls import path, include

urlpatterns = [
    path('api/admin/v1/', include('accounts.api_v1_admin.urls')),
]
