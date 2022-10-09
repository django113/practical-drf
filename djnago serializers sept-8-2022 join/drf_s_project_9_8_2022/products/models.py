from turtle import color
from django.db import models
from django.utils.text import slugify

from django.db.models.signals import pre_save
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_slug = models.SlugField(max_length=255,unique=True,blank=True)    

    def save(self,*args, **kwargs):
        self.category_slug=slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

# product variants 
"""
color
size
leater
kgs

"""

class Quantity(models.Model):
    variant_name = models.CharField(max_length=255)

    def __str__(self):
        return self.variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.color_name
class SizeVariant(models.Model):
    size_name = models.CharField(max_length=255)

    def __str__(self):
        return self.size_name

"""
    title = Required
    date_created = required
    unique_code = required

"""

class productsBrandModel(models.Model):
    title = models.CharField(max_length=255)
    unique_code = models.CharField(max_length=255)
    description = models.TextField()

    # every model in included below fields
    date_created = models.DateTimeField(auto_now_add=True)#inital create time 
    # date_created = models.DateTimeField(auto_now=True)# updated times
    slug= models.SlugField(max_length=255,unique=True,null=True,blank=True)#null database related and blank is validation related


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

pre_save.connect(slug_pre_save_reciver,sender=productsBrandModel)


        
class Product(models.Model):
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_slug = models.SlugField(max_length=255,unique=True,blank=True)
    product_image =models.ImageField(upload_to='products/',default='')#Upload a valid image. The file you uploaded was either not an image or a corrupted image.avif format not allowed
    product_price = models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    product_stock = models.IntegerField(default=10)


    def __str__(self):
        return self.product_name

    def save(self,*args, **kwargs):
        self.product_slug=slugify(self.product_name)
        super(Product,self).save(*args, **kwargs)

        







