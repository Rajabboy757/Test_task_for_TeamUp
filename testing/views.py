from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Test


class CreateTest(generics.GenericAPIView):

    def get(self, request):
        test = Test.objects.create()
        test.set_login()
        res = {'login': test.login}
        return Response(res, status=status.HTTP_201_CREATED)
