# from django.db import models
#
# # Create your models here.
# from django.db import models
# from django.utils import timezone
# from django.utils.text import slugify
#
# # signals imports
# from django.dispatch import receiver
# from django.db.models.signals import (
#     pre_save,
#     post_save,
#     # pre_delete,
#     # post_delete,
#     # m2m_changed,
# )
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# from accounts.models import User
# from ecomerce_core.uitil import slug_pre_save_receiver
#
#
# class signalsSubjectsModel(models.Model):
#     title = models.CharField(max_length=100)
#     date_created = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)
#
#     class Meta:
#         ordering = ['title']
#
#     def __str__(self):
#         return self.title
#
#
# pre_save.connect(slug_pre_save_receiver, sender=signalsSubjectsModel)
#
#
# class signalsStudentsModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="signalsStudentsModel_user")
#     subjects = models.ManyToManyField(signalsSubjectsModel, related_name="signalsStudentsModel_subjects")
#     date_created = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)
#
#     class Meta:
#         ordering = ['user']
#
#     def __str__(self):
#         return self.user
#
#
# pre_save.connect(slug_pre_save_receiver, sender=signalsStudentsModel)
#
# # from datetime import date
# #
# #
# # class Blog(models.Model):
# #     name = models.CharField(max_length=100)
# #     tagline = models.TextField()
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Author(models.Model):
# #     name = models.CharField(max_length=200)
# #     email = models.EmailField()
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Entry(models.Model):
# #     blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="Entry_blog")
# #     headline = models.CharField(max_length=255)
# #     body_text = models.TextField()
# #     pub_date = models.DateField()
# #     mod_date = models.DateField(default=date.today)
# #     authors = models.ManyToManyField(Author,related_name="Entry_authors")
# #     number_of_comments = models.IntegerField(default=0)
# #     number_of_pingbacks = models.IntegerField(default=0)
# #     rating = models.IntegerField(default=5)
# #
# #     def __str__(self):
# #         return self.headline
# #
# #
#
#
# # @receiver(pre_save, sender=User)
# # def user_pre_save_receiver(sender, instance, *args, **kwargs):
# #     """
# #     before saved in the database
# #     """
# #     print('pre save----update1--------',instance.phone, instance.id) # None
# #     # trigger pre_save
# #     # DONT DO THIS -> instance.save()
# #     # trigger post_save
# #
# # # pre_save.connect(user_created_handler, sender=User)
# #
# #
# # @receiver(post_save, sender=User)
# # def user_post_save_receiver(sender, instance, created, *args, **kwargs):
# #     """
# #     after saved in the database
# #     """
# #     if created:
# #         print("post save user phone---------new created----------> ", instance.phone)
# #         # trigger pre_save
# #         instance.save()
# #         # trigger post_save
# #     else:
# #         print('post save------updated2------->',instance.phone, "was just saved")
# #
# # # post_save.connect(user_created_handler, sender=User)
# #
# #
# #
# #
