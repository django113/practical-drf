from pydoc import classname
from secrets import choice
from turtle import title
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll= models.PositiveBigIntegerField()
    city= models.CharField(max_length=100, blank=True)
    state= models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# drf relation with two models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,related_name='song')#signer parent model
    durations = models.IntegerField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



# nested serializers for models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def __str__(self):
        return self.question_text

    def choices(self):
        try:
            choice_queryset = self.Choice_question.all().values()
            print(choice_queryset)
            return choice_queryset
        except:
            return None






class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)#without realted name define using choice_set
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='Choice_question')#without realted name define using choice_set
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text