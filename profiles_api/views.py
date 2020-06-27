from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview=[
            'uses HTTp methods as function (get,post,patch,put,delete)',
            'Is similar to traditional Django ',
            'Gives you the most control over your application logic',
            'Is mapped manually to the URLS'
        ]
        return Response({'message':"Hello!",'an_apiview':an_apiview})
