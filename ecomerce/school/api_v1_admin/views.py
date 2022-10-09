# from django.shortcuts import render
#
# # Create your views here.
# from school.models import schoolSubjectsModel,schoolStudentsModel
# from .serializers import schoolAdminStudentSerializer,schoolAdminSubjectsSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated,AllowAny,BasePermission
# from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework import generics,status,filters
# # from django_filters import rest_framework as dj_filters
#
# # <editor-fold desc="subject create">
# class schoolAdminSubjectCreateGenericsView(generics.ListAPIView,generics.CreateAPIView):
#     serializer_class = schoolAdminSubjectsSerializer
#     queryset = schoolSubjectsModel.objects.all()
#     # permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     # pagination_class = LimitOffsetPagination
#     search_fields = ["title",]
#     filter_backends = (filters.SearchFilter,)
#
#     def list(self,request,*args, **kwargs):
#         serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())),many=True,context={"request":request})
#         return self.get_paginated_response(serializer.data)
#
#     def post(self, request):
#         serializer = schoolAdminSubjectsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # </editor-fold>
#
#
# # <editor-fold desc="subject details">
# class schoolAdminSubjectDetailsAPIView(APIView):
#     serializer_class = schoolAdminSubjectsSerializer
#     # permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     pagination_class = None
#
#     def get(self, request, slug):
#         data = schoolSubjectsModel.objects.get(slug=slug)
#         serializer = schoolAdminSubjectsSerializer(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, slug):
#         data = schoolSubjectsModel.objects.get(slug=slug)
#         serializer = schoolAdminSubjectsSerializer(data=request.data, instance=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request, slug):
#         data = schoolSubjectsModel.objects.get(slug=slug)
#         data.delete()
#         return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# # </editor-fold>
#
#
# # <editor-fold desc="student create">
# class schoolAdminStudentCreateGenericsView(generics.ListAPIView,generics.CreateAPIView):
#     serializer_class = schoolAdminStudentSerializer
#     queryset = schoolStudentsModel.objects.all()
#     # permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     # pagination_class = LimitOffsetPagination
#     search_fields = ["title",]
#     filter_backends = (filters.SearchFilter,)
#
#     def list(self,request,*args, **kwargs):
#         serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())),many=True,context={"request":request})
#         return self.get_paginated_response(serializer.data)
#
#     def post(self, request):
#         serializer = schoolAdminStudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # </editor-fold>
#
#
# # <editor-fold desc="student details">
# class schoolAdminStudentDetailsAPIView(APIView):
#     serializer_class = schoolAdminStudentSerializer
#     # permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     pagination_class = None
#
#     def get(self, request, slug):
#         data = schoolStudentsModel.objects.get(slug=slug)
#         serializer = schoolAdminStudentSerializer(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, slug):
#         data = schoolStudentsModel.objects.get(slug=slug)
#         serializer = schoolAdminStudentSerializer(data=request.data, instance=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request, slug):
#         data = schoolStudentsModel.objects.get(slug=slug)
#         data.delete()
#         return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# # </editor-fold>
