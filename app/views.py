from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
class RootView(APIView):
    def get(self, request: Request):
        return Response({"message": "Hello from the backend!"})

    def post(self, request: Request):
        return Response({"message": "Hello, POST!"})
