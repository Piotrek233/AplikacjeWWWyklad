from rest_framework import serializers
from .models import Equipment
from .models import Rating
from django.contrib.auth.models import User

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name','type','destiny','user']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','last_login','is_superuser','username','email','date_joined','password']
        extra_kwargs = {'last_login':{'read_only':True},'date_joined':{'read_only':True}}