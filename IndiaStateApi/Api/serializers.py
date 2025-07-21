from rest_framework import serializers
from .models import State, ChfMinister


class StateSerializer(serializers.ModelSerializer):
    cm = serializers.SlugRelatedField(read_only = True, slug_field='name')
    class Meta:
        model = State
        fields = ['name', 'capital', 'population', 'cm']


class ChfMinisterSerializer(serializers.ModelSerializer):
    # state_id = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')
    class Meta:
        model = ChfMinister
        fields = ['name', 'dob', 'gender', 'state_id']