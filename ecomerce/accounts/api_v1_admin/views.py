from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics, status, filters
# from django_filters import rest_framework as dj_filters


from django.contrib.auth import get_user_model

from accounts.api_v1_admin.serializers import accountsAdminUserProfileSerializer
from accounts.models import accountUserProfile

User = get_user_model()


class productsAdminUserProfileCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = accountsAdminUserProfileSerializer
    queryset = accountUserProfile.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["user", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = accountsAdminUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productsAdminUserProfileDetailsAPIView(APIView):
    serializer_class = accountsAdminUserProfileSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = accountUserProfile.objects.get(slug=slug)
        serializer = accountsAdminUserProfileSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = accountUserProfile.objects.get(slug=slug)
        serializer = accountsAdminUserProfileSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = accountUserProfile.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
