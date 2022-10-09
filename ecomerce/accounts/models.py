from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from ecomerce_core.uitil import slug_pre_save_receiver


# from products.models import *


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, phone, dob=None, password=None):
        """
        Create and save a User with the given email and password.
        """
        if phone == None:
            raise ValueError(_('The phone must be set'))
        else:
            user = self.model(phone=phone, dob=dob)

        user.is_active = True
        email = self.normalize_email(email)
        user.email = email
        user.set_password(password)
        user.save()
        return user

    def create_staff(self, email, phone, dob=None, password=None):
        """
        Create and save a User with the given email and password.
        """
        user = self.create_user(email=email, phone=phone, dob=dob, password=password)

        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, dob=None, password=None):
        """
        Create and save a User with the given email and password.
        """
        user = self.create_user(email=email, phone=phone, dob=dob, password=password)

        user.is_staff = True
        user.is_admin = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.BigIntegerField(_('phone number'), unique=True)
    email = models.EmailField(_('Email address'), unique=True)
    dob = models.DateField(_('date of birth'), null=True,
                           blank=True)  # null is database related,blank is validation related use

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_superuser= models.BooleanField( default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    # this methods must be Required for AbstractBaseUser Model  .
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


pre_save.connect(slug_pre_save_receiver, sender=User)


class accountUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accountsUserProfile_user')
    country = models.CharField(blank=True, max_length=250)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.user)


pre_save.connect(slug_pre_save_receiver, sender=accountUserProfile)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        accountUserProfile.objects.create(
            user=instance
        )
