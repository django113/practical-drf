from django.db import models, transaction
from django.db.models import Q
from django.dispatch import receiver
from django.utils.text import slugify

from ecomerce_core.uitil import slug_pre_save_receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed

from products.signals import brand_unique_code_generator

from django.contrib.auth import get_user_model

User = get_user_model()

"""

unique_code = required

title = required

date_created = required

slug = required




"""


# Create your models here.
class productsBrandModel(models.Model):
    unique_code = models.CharField(max_length=250, null=True, unique=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver, sender=productsBrandModel)
pre_save.connect(brand_unique_code_generator, sender=productsBrandModel)


class productsProductMainModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(productsBrandModel, on_delete=models.CASCADE,
                              related_name='productsProductMainModel_brand')
    price = models.FloatField()

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_productbrand(self, obj):
        try:
            brand = obj.brand.title
        except:
            brand = ""
        return brand


pre_save.connect(slug_pre_save_receiver, sender=productsProductMainModel)

"""
product = required
quantity =required
initalprice = required
finalprice = required
date_created = required
slug = required

"""


class productsCartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productsCartModel_user')
    product = models.ForeignKey(productsProductMainModel, on_delete=models.CASCADE,
                                related_name='productsCartModel_product')
    quantity = models.IntegerField(default=1)
    initial_price = models.FloatField(null=True, blank=True)  # initial price is product price
    final_price = models.FloatField(null=True, blank=True)  # quantity * initial price
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        self.initial_price = self.product.price
        self.final_price = self.product.price * self.quantity
        super(productsCartModel, self).save(*args, **kwargs)
        try:
            self.user.productsUserCartModel_user.save()
        except Exception as e:
            pass

@receiver(pre_delete, sender=productsCartModel)
def cart_pre_delete(sender, instance, *args, **kwargs):
    if instance:
        #   product user cart model price update
        product_price = productsCartModel.objects.all().filter(user_id=instance.user).values_list('final_price',
                                                                                                  flat=True)
        print('update pre delete product cart----------1', product_price)
        print('pre_delete--------->3', product_price)
        price = sum(product_price)
    if instance.user != None:
        price_update = productsUserCartModel.objects.filter(user=instance.user).update(price=price)
        print("pre delete on update price", price_update)


@receiver(post_delete, sender=productsCartModel)
def cart_post_delete(sender, instance, *args, **kwargs):
    #   product user cart model price update
    product_price = productsCartModel.objects.all().filter(user_id=instance.user).values_list('final_price', flat=True)
    print('update post_delete product cart----------2', product_price)

    print('post_delete--------->3', product_price)
    price = sum(product_price)
    if instance.user != None:
        price_update = productsUserCartModel.objects.filter(user=instance.user).update(price=price)
        print("post_delete on update price", price_update)

pre_save.connect(slug_pre_save_receiver, sender=productsCartModel)


class productsUserCartModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='productsUserCartModel_user')
    cart_line = models.ManyToManyField(productsCartModel, blank=True, related_name='productsUserCartModel_cart_line')
    price = models.FloatField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.cart_line)
        # return str(self.cart_line) + " " + str(self.user)

    def save(self, *args, **kwargs):
        super(productsUserCartModel, self).save(*args, **kwargs)
        with transaction.atomic():
            transaction.on_commit(self.price_update)

    def price_update(self):
        total_final_price = 0
        for item in self.cart_line.all():
            print(item.final_price)
            total_final_price += item.final_price
        self.price = total_final_price
        super(productsUserCartModel, self).save()

        # data = self.cart_line.all().aggregate(Sum('final_price'))
        # self.price = data.get('final_price__sum')
        # super(productsUserCartModel, self).save()

    def get_products(self):
        return ",".join([str(p) for p in self.cart_line.all()])


pre_save.connect(slug_pre_save_receiver, sender=productsUserCartModel)


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        print("post save user phone---------new created----------> ", instance.phone)
        # trigger pre_save
        if instance:
            product_user_cart = productsUserCartModel.objects.create(user=instance)
            print(product_user_cart, 'user cart is created')
            instance.save()
        # trigger post_save
    else:
        print('post save------updated2------->', instance.phone, "was just saved")
