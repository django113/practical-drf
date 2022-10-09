from django.shortcuts import render

# Create your views here.
from SIGNALS.models import signalsStudentsModel,signalsSubjectsModel
from SIGNALS.api_v1_admin.serializers import siganlsAdminStudentSerializer,signalsAdminSubjectsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,BasePermission
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics,status,filters
# from django_filters import rest_framework as dj_filters

class siganlsAdminSubjectCreateGenericsView(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = signalsAdminSubjectsSerializer
    queryset = signalsSubjectsModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title",]
    filter_backends = (filters.SearchFilter,)

    def list(self,request,*args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())),many=True,context={"request":request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = signalsAdminSubjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class siganlsAdminSubjectDetailsAPIView(APIView):
    serializer_class = signalsAdminSubjectsSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = signalsSubjectsModel.objects.get(slug=slug)
        serializer = signalsAdminSubjectsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = signalsSubjectsModel.objects.get(slug=slug)
        serializer = signalsAdminSubjectsSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, slug):
        data = signalsSubjectsModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
