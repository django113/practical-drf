from django.urls import path

from products.api_v1_admin.views import productsAdminUserDetailsAPIView, productsAdminUserCreateGenericsView, \
    productsAdminBrandCreateGenericsView, productsAdminBrandDetailsAPIView, productsAdminProductMainCreateGenericsView, \
    productsAdminProductMainDetailsAPIView, productsAdminCartCreateGenericsView, productsAdminCartDetailsAPIView, \
    productsAdminUserCartCreateGenericsView, productsAdminUserCartDetailsAPIView

urlpatterns = [
    # productsBrandModelbrand-details
    path('brand-create/', productsAdminBrandCreateGenericsView.as_view(), name='productsAdminBrandCreateGenericsViewURL'),
    path('brand-details/<slug>/', productsAdminBrandDetailsAPIView.as_view(), name='productsAdminBrandDetailsAPIViewURL'),
    # productsProductMainModel
    path('productmain-create/', productsAdminProductMainCreateGenericsView.as_view(), name='productsAdminProductMainCreateGenericsViewURL'),
    path('productmain-details/<slug>/', productsAdminProductMainDetailsAPIView.as_view(), name='productsAdminProductMainDetailsAPIViewURL'),
    # productsCartModel
    path('cart-create/', productsAdminCartCreateGenericsView.as_view(), name='productsAdminCartCreateGenericsViewURL'),
    path('cart-details/<slug>/', productsAdminCartDetailsAPIView.as_view(), name='productsAdminCartDetailsAPIViewURL'),
    # User
    path('user-create/', productsAdminUserCreateGenericsView.as_view(), name='productsAdminUserCreateGenericsViewURL'),
    path('user-details/<slug>/', productsAdminUserDetailsAPIView.as_view(), name='productsAdminUserDetailsAPIViewURL'),
   # User Cart
    path('user-cart-create/', productsAdminUserCartCreateGenericsView.as_view(), name='productsAdminUserCartCreateGenericsViewURL'),
    path('user-cart-details/<slug>/', productsAdminUserCartDetailsAPIView.as_view(), name='productsAdminUserCartDetailsAPIViewURL'),


]
