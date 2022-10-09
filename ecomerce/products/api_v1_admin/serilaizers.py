from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Sum

from products.models import productsBrandModel, productsProductMainModel, productsCartModel, productsUserCartModel
from rest_framework import serializers, status

from django.contrib.auth import get_user_model

User = get_user_model()

"""
user serializers
"""


class productsAdminUserSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=True)

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_email

    class Meta:
        model = User
        fields = ['phone', 'email', 'dob', 'slug']
        # exclude = ['password', 'last_login', 'is_admin', 'is_active', 'is_staff']

        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data
                                        )

        # user.set_password(make_password(validated_data['password']))
        # user.save()
        return user


class productsAdminBrandSerializer(serializers.ModelSerializer):

    def validate(self, data):
        title = data.get("title", None)
        brand = productsBrandModel.objects.filter(title__iexact=title)
        if brand.exists():
            raise serializers.ValidationError(
                {"errors": "This brand already exists", 'status': status.HTTP_400_BAD_REQUEST})
        else:
            return data

    class Meta:
        model = productsBrandModel
        fields = "__all__"


"""
product main model serializers
"""


class productsAdminProductMainCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = productsProductMainModel
        fields = "__all__"


"""
product main model serializers get brand name with put,delete
"""


class productsAdminProductMainSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        brand = obj.get_productbrand(obj)
        return brand

    #
    # productsProductMainModel_brand=productsAdminBrandSerializer()
    class Meta:
        model = productsProductMainModel
        fields = ['name', 'brand', 'price', 'date_created', 'slug']


class productsAdminCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = productsCartModel
        # fields = "__all__"
        fields = ['user', 'product', 'quantity', 'initial_price', 'final_price', 'date_created', 'slug', ]


# <editor-fold desc="user_slug and product slug post ">
class productsAdminUserCartSerializer(serializers.Serializer):
    user_slug = serializers.CharField(max_length=100, required=True)
    product_slug = serializers.CharField(max_length=100, required=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        user_slug = validated_data['user_slug']
        # user=self.context['request'].user
        product_slug = validated_data['product_slug']

        try:
            product = productsProductMainModel.objects.filter(slug=product_slug).last()
        except Exception as e:

            raise serializers.ValidationError("Not Available product")

        user_main = User.objects.filter(slug=user_slug).last()
        user_cart = productsUserCartModel.objects.filter(user=user_main).last()

        if user_cart == None:
            cart_main = productsUserCartModel.objects.create(user=user_main)
        else:
            cart_main = user_cart

        product_user = productsCartModel.objects.filter(user=user_main, product=product)

        if len(product_user) == 0:
            product_cart = productsCartModel.objects.create(user=user_main, product=product)
        elif len(product_user) != 0:
            product_cart = product_user.last()
            print(product_cart)
        else:
            product_cart = product_user.last()

        cart_main.cart_line.add(product_cart)

        # cart_main.price = user_cart.cart_line.all().aggregate(Sum('final_price')).get('final_price__sum')
        # cart_main.price = user_cart.price
        cart_main.save()
        return validated_data
