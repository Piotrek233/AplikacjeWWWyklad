from rest_framework import serializers
from .models import Equipment
from .models import Rating
from django.contrib.auth.models import User

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Mate:
        model = User
        fields = ['id','last_login','is_superuser','username','email','data_joined']