from django.db import models
from Books.signals import isbn_unique_code_generator
from ecomerce_core.uitil import slug_pre_save_receiver
from django.db.models.signals import pre_save

"""

title = required
date_created = required
slug = required
"""


# publish the books
class bookPublicationModel(models.Model):
    title = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver, sender=bookPublicationModel)
"""
email = required
date_created = required
slug = required


"""


# Create your models here.
class booksAuthorModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


pre_save.connect(slug_pre_save_receiver, sender=booksAuthorModel)

"""
title = required
price = required
pages = required

isbn = required
author = required
slug= required
date_created = required

"""


class booksBookModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    pages = models.IntegerField()
    pub_date = models.DateField()
    author = models.ForeignKey(booksAuthorModel, on_delete=models.CASCADE, related_name='booksBookModel_author')
    # author = models.ForeignKey(booksAuthorModel, on_delete=models.CASCADE, related_name='booksBookModel_author')
    summary = models.TextField(max_length=1000, null=True,
                               blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, null=True, blank=True)
    publications = models.ManyToManyField(bookPublicationModel, related_name='booksBookModel_publications')

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


pre_save.connect(slug_pre_save_receiver, sender=booksBookModel)
pre_save.connect(isbn_unique_code_generator, sender=booksBookModel)
