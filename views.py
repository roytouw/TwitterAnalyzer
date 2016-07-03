# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestViewSet(APIView):
    def get(self, request, *args):
        result = "hello"
        print('came here')
        response = Response(result, status=status.HTTP_200_OK)
        return response
