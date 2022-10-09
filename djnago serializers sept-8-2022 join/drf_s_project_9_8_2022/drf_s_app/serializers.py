from wsgiref.validate import validator
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from drf_s_app.models import *
#example 1
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



"""
{
    "name": [
        "value must be capitalized"
    ]
}

"""

def start_with(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('value must be capitalized')
    

#example 2
class StudentSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100,validators=[start_with])
    roll= serializers.IntegerField()
    city= serializers.CharField(max_length=100)
    state= serializers.CharField(max_length=100)



    def create(self,validata):
        return Student.objects.create(**validata)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        # instance.name = validated_data['name']
        print(instance.name,'instance name')
        instance.roll = validated_data['roll']
        instance.city = validated_data['city']
        instance.state = validated_data['state']
        instance.save()
        return instance

    # 20 bellow and above not working field level validationError 
    def validate_roll(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('Roll has to be between 1 and 10.')
        return value


    #object level validationError is raised
    def validate(self,data):

        """
            {
                "non_field_errors": [
                    "name is Mohan required"
                ]
            }
        """
        # if 'name' not in data:
        #     raise serializers.ValidationError('name is required')
        # if 'roll' not in data:
        #     raise serializers.ValidationError('roll is required')
        # if 'city' not in data:
        #     raise serializers.ValidationError('city is required')
        name=data.get('name',None)
        city=data.get('city',None)
        state=data.get('state',None)
        roll=data.get('roll',None)
        if name == 'Mohan': 
            raise serializers.ValidationError('name is Mohan required')
        return data




#  serializer realations for signer and song serializers

class SongSerializer(serializers.ModelSerializer):#child serializers
    class Meta:
        model = Song
        fields = '__all__'


# class SingerSerializer(serializers.ModelSerializer):#parent serializers

#     class Meta:
#         model = Singer
#         fields = '__all__'

# nested serializers for model serializers with two models:Song,signer
class SingerSerializer(serializers.ModelSerializer):#parent serializers
    # song = serializers.StringRelatedField(many=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='song-detail'
    # )
    # song=serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title',#child class field name
    #  )

    song = serializers.SerializerMethodField()

    class Meta:
        model = Singer
        fields = ['name', 'gender', 'song']


# nested serializers for ModelSerializer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question','choice_text','votes']

class QuestionSerializer(serializers.ModelSerializer):
    
    # 1.example way
    # choice = serializers.SerializerMethodField()
    # def get_choice(self,obj):
    #     try:
    #         print(obj)
    #         choice_quryset = Choice.objects.filter(question=obj)
    #         print(choice_quryset)
    #         serializer_data = ChoiceSerializer(choice_quryset,many=True)
    #         return serializer_data.data

    #     except:
    #         return {}
    # 2.example way
    Choice_question=ChoiceSerializer(many=True,read_only=True)
    # choice=ChoiceSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date','Choice_question']
        






        
    
    


