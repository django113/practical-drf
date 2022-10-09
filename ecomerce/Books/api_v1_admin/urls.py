from django.urls import path
from .views import booksAdminAuthorGenericsView, booksAdminAuthorDetailsAPIView, booksAdminBookGenericsView, \
    booksAdminBookDetailsAPIView, booksAdminPublishGenericsView, booksAdminPublishDetailsAPIView

urlpatterns = [
    # author
    path('books-author/', booksAdminAuthorGenericsView.as_view(), name='booksAdminAuthorGenericsViewURL'),
    path('books-author/<slug>/', booksAdminAuthorDetailsAPIView.as_view(), name='booksAdminAuthorDetailsAPIViewURL'),

    # books
    path('books-book/',booksAdminBookGenericsView.as_view(), name='booksAdminBookGenericsViewURL'),
    path('books-book/<slug>/', booksAdminBookDetailsAPIView.as_view(), name='booksAdminBookDetailsAPIViewURL'),

    # publish
    path('books-publish/',booksAdminPublishGenericsView.as_view(), name='booksAdminBookGenericsViewURL'),
    path('books-publish/<slug>/', booksAdminPublishDetailsAPIView.as_view(), name='booksAdminBookDetailsAPIViewURL'),

]
