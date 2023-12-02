from django.http import JsonResponse
from django.shortcuts import render
#from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from .models import Teacher
from .serializers import TeacherSerializer, CourseSerializer
from . import models


# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def teacher_login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,'email')
        teacherData = Teacher.objects.filter(email=email, password=password).first()
        if teacherData:
            return JsonResponse({'bool': True})
        else:
            return JsonResponse({'bool': False})
    else:
        return JsonResponse({'bool': 'False'})


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

