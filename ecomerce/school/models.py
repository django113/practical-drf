from django.db import models
#
# Create your models here.
# signals imports
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)
from django.contrib.auth import get_user_model
#
from school.signals import subject_unique_code_generator

#
User = get_user_model()
#
# from accounts.models import User
from ecomerce_core.uitil import slug_pre_save_receiver


# student-
# subject
# marks

# -fk student
# -fk --mark


# student
#
# class schoolStudentModel(models.Model):
#     owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name="schoolStudentModel_owner")
#     photo = models.FileField(upload_to='student_profile',default='')
#
#
# class schoolTeacherModel(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="schoolTeacherModel_owner")
#     designation = models.CharField(max_length=100)

# photo = models.FileField(upload_to='Teacher_profile', default='')

# class schoolCoursesModel(models.Model):
#     title = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     fees = models.IntegerField()
#     student = models.ManyToManyField(User, on_delete=models.CASCADE, related_name="schoolCoursesModel_student")
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schoolCoursesModel_teacher")

# student --fk--cousre

#
# class schoolSubjectModel(models.Model):
#     title = models.CharField(max_length=200)
#     discription = models.TextField()
#
#
# class schoolMarksModel(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schoolMarksModel_student")
#     subject = models.ForeignKey(schoolSubjectModel, on_delete=models.CASCADE, related_name="schoolMarksModel_subject")
#     marks = models.FloatField()
#
#
# class schoolMarksheetModel(models.Model):
#     student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="schoolMarksheetModel_student")
#     total_marks = models.FloatField()
#     grade = models.CharField(max_length=100)


# class schoolSubjectsModel(models.Model):
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
# pre_save.connect(subject_unique_code_generator, sender=schoolSubjectsModel)
# pre_save.connect(slug_pre_save_receiver, sender=schoolSubjectsModel)
#
#
# class schoolStudentsModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="signalsStudentsModel_user")
#     subjects = models.ManyToManyField(schoolSubjectsModel, related_name="signalsStudentsModel_subjects")
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
# pre_save.connect(slug_pre_save_receiver, sender=schoolStudentsModel)
