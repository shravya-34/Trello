from rest_framework import serializers
from .models import Card, Column, UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ["id", "name", "email", "password"]

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "title", "column", "userid"]

class ColumnDataSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ["id", "name"]

