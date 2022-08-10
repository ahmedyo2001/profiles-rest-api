from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers



class HelloApiView (APIView):
    serializers_class = serializers.HelloSerializers
    def get(self, request, format=None):
        an_apiview=[
            "uses http methods",
            "Is similar to a trad django view",
            'gives u most control to app logic',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        serializer =self.serializers_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors , status=400)

    def patch(self, request):
        serializer =self.serializers_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors , status=400)



class BadBad (APIView):

    def get(self, request, format=None):
        an_apiview=[
            "uses http methods",
            "Is similar to a trad django view",
            'gives u most control to app logic',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

