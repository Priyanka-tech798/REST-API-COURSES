from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers,models,permissions

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'uses HTTp methods as function (get,post,patch,put,delete)',
            'Is similar to traditional Django ',
            'Gives you the most control over your application logic',
            'Is mapped manually to the URLS'
        ]
        return Response({'message':"Hello!",'an_apiview':an_apiview})

    def post(self,request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(Self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class =serializers.HelloSerializer
    def list(self,request):

        a_viewset=[
            'Uses action (list,create,retrive,update,partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        serializer =self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk = None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk =None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
