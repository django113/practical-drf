from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from rest_framework import permissions
from drf_s_app.serializers import UserSerializer, GroupSerializer
from drf_s_app.models import *
from drf_s_app.serializers import *
from rest_framework.renderers import JSONRenderer

#example 1
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


# hyperlinked related return ?
def user_detail(request):
    stu=User.objects.all()
    # stu=Student.objects.get(id=1)
    # sr=StudentSerializer(stu)#serializer
    sr=UserSerializer()#serializer
    """
    UserSerializer():
    url = HyperlinkedIdentityField(view_name='user-detail')
    username = CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[<django.contrib.auth.validators.UnicodeUsernameValidator object>, <UniqueValidator(queryset=User.objects.all())>])
    email = EmailField(allow_blank=True, label='Email address', max_length=254, required=False)
    groups = HyperlinkedRelatedField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', many=True, queryset=Group.objects.all(), required=False, view_name='group-detail')  -----------what output

    """
    print(repr(sr), " -----------what output" )
    # print('student serializer-------',sr)
    # print('student serializer data---',sr.data)

    # json = JSONRenderer().render(sr.data)
    # print('json data using json render-----------',json)
    # return HttpResponse(json,content_type="application/json")

    return JsonResponse(sr.data,safe=False)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


#example 2
# https://www.django-rest-framework.org/tutorial/1-serialization/
# serialization and deserialization are implemented example

def student_detail(request):
    stu=Student.objects.all()
    # stu=Student.objects.get(id=1)
    # sr=StudentSerializer(stu)#serializer
    sr=StudentSerializer(stu,many=True)#serializer
    # print('student serializer-------',sr)
    # print('student serializer data---',sr.data)

    # json = JSONRenderer().render(sr.data)
    # print('json data using json render-----------',json)
    # return HttpResponse(json,content_type="application/json")

    return JsonResponse(sr.data,safe=False)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class =StudentSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('-id')
    serializer_class =SongSerializer

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all().order_by('-id')
    serializer_class =SingerSerializer



# nested serializers for views

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-id')
    serializer_class =QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by('-id')
    serializer_class =ChoiceSerializer