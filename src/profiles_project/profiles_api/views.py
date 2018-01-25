from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test API View. """

    def get(self, request, format=None):
        """ Returns a list of APIView features """

        an_apiview = [
        'Use HTTP Methods as function (get, post, put, patch, delete)'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
