from django.urls import path

from accounts.api_v1_admin.views import productsAdminUserProfileCreateGenericsView, \
    productsAdminUserProfileDetailsAPIView

urlpatterns = [

    path('user-profile-create/', productsAdminUserProfileCreateGenericsView.as_view(), name='productsAdminUserProfileCreateGenericsViewURL'),
    path('user-profile-details/<slug>/', productsAdminUserProfileDetailsAPIView.as_view(), name='productsAdminUserProfileDetailsAPIViewURL'),


]
