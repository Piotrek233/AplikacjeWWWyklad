from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Equipment,Rating
from .serializers import EquipmentSerializer,RatingSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    name = 'equipments'
    filterset_fields = ['name','type','destiny']
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['type','destiny']


class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    name = 'rating'
    filterset_fields = ['subject', 'value']
    permission_classes = [IsAuthenticated]
    search_fields = ['subject']
    ordering_fields = ['subject', 'value']


class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    name = 'equipment'
    permission_classes = [IsAuthenticated]

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    name = 'rating'
    permission_classes = [IsAuthenticated]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users'
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user'
    permission_classes = [IsAuthenticated]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'equimpment': reverse(EquipmentList.name, request=request),
                         'rating': reverse(RatingList.name, request=request),
                         'users': reverse(UserList.name, request=request)
})