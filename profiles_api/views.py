from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView (APIView):

    def get(self, request, format=None):
        an_apiview=[
            "uses http methods",
            "Is similar to a trad django view",
            'gives u most control to app logic',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

