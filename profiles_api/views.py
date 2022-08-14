from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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




class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset"""

    def list(self, request):
        a_viewset=["uses actions 7agat kteer",
        "auto maps to urls" ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name',"email")