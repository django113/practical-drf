from Books.models import booksAuthorModel, booksBookModel, bookPublicationModel
from .serilaizers import booksAdminAuthorSerializer, booksAdminBookSerializer, booksSerializer, \
    booksAdminPublishSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, status, filters

# from django_filters import rest_framework as dj_filters


"""
LIST AND CREATE PURPOSE WE CAN USE GENERIC API VIEWS USING 
"""


class booksAdminAuthorGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = booksAdminAuthorSerializer
    queryset = booksAuthorModel.objects.all()
    permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["email"]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        """
        IF FILTER  value query set in not using list method will using and filter or etc.
        or get_queryset method ofter will filter or etc.
        """
        # s_name_brand = productsBrandModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = booksAdminAuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class booksAdminAuthorDetailsAPIView(APIView):
    serializer_class = booksAdminAuthorSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = booksAuthorModel.objects.get(slug=slug)
        serializer = booksAdminAuthorSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = booksAuthorModel.objects.get(slug=slug)
        serializer = booksAdminAuthorSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = booksAuthorModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


"""
LIST AND CREATE PURPOSE WE CAN USE GENERIC API VIEWS USING 
"""


class booksAdminBookGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = booksAdminBookSerializer
    queryset = booksBookModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):

        """
        IF FILTER  value query set in not using list method will using and filter or etc.
        or get_queryset method ofter will filter or etc.
        """
        # s_name_brand = productsBrandModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = booksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class booksAdminBookDetailsAPIView(APIView):
    serializer_class = booksAdminBookSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = booksBookModel.objects.get(slug=slug)
        serializer = booksAdminBookSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = booksBookModel.objects.get(slug=slug)
        serializer = booksAdminBookSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = booksBookModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


# --------------------------------------------publish---------------------------------------


"""
LIST AND CREATE PURPOSE WE CAN USE GENERIC API VIEWS USING 
"""


class booksAdminPublishGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = booksAdminPublishSerializer
    queryset = bookPublicationModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):

        """
        IF FILTER  value query set in not using list method will using and filter or etc.
        or get_queryset method ofter will filter or etc.
        """
        # s_name_brand = productsBrandModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = booksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class booksAdminPublishDetailsAPIView(APIView):
    serializer_class = booksAdminPublishSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = bookPublicationModel.objects.get(slug=slug)
        serializer = booksAdminPublishSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = bookPublicationModel.objects.get(slug=slug)
        serializer = booksAdminPublishSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = bookPublicationModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
