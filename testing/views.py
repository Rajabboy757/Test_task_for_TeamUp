from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Test
from .serializers import IQTestSerializer


class CreateTest(generics.GenericAPIView):

    def get(self, request):
        test = Test.objects.create()
        test.set_login()
        test.save()
        res = {'login': test.login}
        return Response(res, status=status.HTTP_201_CREATED)


class SetIQTestResult(generics.GenericAPIView):
    serializer_class = IQTestSerializer

    def post(self, request):
        login = request.data.get('login')
        result = request.data.get('IQ_result')
        print(login,result)
        test = Test.objects.get(login=login)
        test.IQ_result = result
        test.set_time('IQ')
        test.save()
        return Response({'message': 'result has been set succesfully'}, status=status.HTTP_200_OK)
