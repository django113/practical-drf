from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from Books.models import booksAuthorModel, booksBookModel, bookPublicationModel


class booksAdminPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookPublicationModel
        fields = ["title"]


class booksAdminBookSerializer(serializers.ModelSerializer):
    publications = serializers.SerializerMethodField()

    def get_publications(self, obj):
        try:
            serializer_data = booksAdminPublishSerializer(obj.publications, many=True).data
        except Exception as e:
            print(e)
            serializer_data = []
        return serializer_data

    class Meta:
        model = booksBookModel
        fields = "__all__"
        # depth=1
        # fields = ['title','price','pages','pub_date','author','summary','isbn','publications','date_created','slug',]

    # def create(self, validated_data):
    #     publications1 = validated_data.pop('publications', ())
    #     book = booksBookModel.objects.create(
    #         **validated_data
    #     )
    #     # add groups to the user ↓
    #     book.publications.add(*publications1)
    #     book.save()
    #     return book


class booksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    pages = serializers.IntegerField()
    pub_date = serializers.DateField()
    author = serializers.IntegerField(required=True)
    summery = serializers.CharField(max_length=500)
    publications = booksAdminPublishSerializer(many=True, required=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        data = validated_data['publications']
        publications_all = []
        for i in data:
            data1 = i['title']

            publish = bookPublicationModel.objects.create(title=data1)
            publications_all.append(publish)
        author = booksAuthorModel.objects.filter(id=validated_data["author"]).last()
        try:
            publish = booksAuthorModel.objects.get(pk=author.id)
        except booksAuthorModel.DoesNotExist:
            publish = None

        books = booksBookModel.objects.create(title=validated_data["title"],
                    price=validated_data["price"],
                    pages=validated_data["pages"],
                    pub_date=validated_data["pub_date"],
                    author=author)
        books.publications.set(publications_all)
        return validated_data


class booksAdminAuthorSerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     email = data.get("email", None)
    #     author = booksAuthorModel.objects.filter(email__iexact=email)
    #     if author.exists():
    #         raise serializers.ValidationError(
    #             {"errors": "This Author already exists", 'status': status.HTTP_400_BAD_REQUEST})
    #     else:
    #         return data

    booksBookModel_author = booksAdminBookSerializer(many=True, read_only=True)

    class Meta:
        model = booksAuthorModel
        # fields = "__all__"
        fields = ['id', 'first_name', 'last_name', 'email', 'date_of_birth', 'date_of_death', 'date_created', 'slug',
                  'booksBookModel_author', ]
