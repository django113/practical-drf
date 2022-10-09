from django.contrib import admin

# Register your models here.
from Books.models import booksAuthorModel, booksBookModel, bookPublicationModel

admin.site.register(booksBookModel)
admin.site.register(booksAuthorModel)
admin.site.register(bookPublicationModel)
