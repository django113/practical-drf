from products.models import productsBrandModel, productsProductMainModel, productsCartModel, productsUserCartModel
from .serilaizers import productsAdminBrandSerializer, productsAdminProductMainSerializer, productsAdminCartSerializer, \
    productsAdminUserSerializer, productsAdminProductMainCreateSerializer, \
    productsAdminUserCartSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, status, filters
# from django_filters import rest_framework as dj_filters


from django.contrib.auth import get_user_model

User = get_user_model()


class productsAdminBrandCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminBrandSerializer
    queryset = productsBrandModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        # s_name_brand = productsBrandModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAdminBrandDetailsAPIView(APIView):
    serializer_class = productsAdminBrandSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        serializer = productsAdminBrandSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        serializer = productsAdminBrandSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


"""
productsProductMainModel

"""


# <editor-fold desc="GET ALL PRODUCTS AND CREATE PRODUCTS">
class productsAdminProductMainCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminProductMainSerializer
    queryset = productsProductMainModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["brand", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminProductMainCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# </editor-fold>


class productsAdminProductMainDetailsAPIView(APIView):
    serializer_class = productsAdminProductMainSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        serializer = productsAdminProductMainSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        serializer = productsAdminProductMainSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


"""
productsCartModel

"""


class productsAdminCartCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminCartSerializer
    queryset = productsCartModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAdminCartDetailsAPIView(APIView):
    serializer_class = productsAdminCartSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsCartModel.objects.get(slug=slug)
        serializer = productsAdminCartSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsCartModel.objects.get(slug=slug)
        serializer = productsAdminCartSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsCartModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


"""
User

"""


class productsAdminUserCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminUserSerializer
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["email", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAdminUserDetailsAPIView(APIView):
    serializer_class = productsAdminUserSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsCartModel.objects.get(slug=slug)
        serializer = productsAdminUserSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = User.objects.get(slug=slug)
        serializer = productsAdminUserSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = User.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


"""
User Cart Model
"""


class productsAdminUserCartCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminUserCartSerializer
    queryset = productsUserCartModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminUserCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAdminUserCartDetailsAPIView(APIView):
    serializer_class = productsAdminUserCartSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsUserCartModel.objects.get(slug=slug)
        serializer = productsAdminUserCartSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsUserCartModel.objects.get(slug=slug)
        serializer = productsAdminUserCartSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsUserCartModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
