from rest_framework import serializers
from .models import Company, Industry
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["c_name", "c_founded", 'c_industry']


class IndustrySerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many = True)
    class Meta:
        model = Industry
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user