from django.views import View
from django.db import transaction
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserDetails, Card, Column
from .serializers import UserDetailsSerializer, ColumnSerializer, ColumnDataSerialzer

# Create your views here.

class SignUp(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
        

class Authenticate(generics.ListCreateAPIView):
    def get(self, request):
        if request.user.is_authenticated:  
            return redirect('/schedule')
        return redirect('/signup')

    
class Schedule(APIView):
    def get(self, request, format=None):
        userid = request.query_params.get('userid', None)
        cards = Card.objects.filter(userid=userid)
        serializer = ColumnSerializer(cards, many=True)
        return Response(serializer.data)


class ScheduleAll(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = ColumnSerializer

# Edit Card Details
class EditCard(generics.RetrieveUpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = ColumnSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Custom logic to change the primary key based on the column value
        new_column_value = serializer.validated_data.get('column')
        if new_column_value != instance.column:
            with transaction.atomic():
                # Create a new object with a new primary key
                new_instance = Card.objects.create(
                    title=instance.title,
                    column=new_column_value,
                    userid = instance.userid
                    # Add other fields as necessary
                )
                # Delete the old object
                instance.delete()
                return Response(self.get_serializer(new_instance).data)
        # If the column value hasn't changed, proceed with the normal update
        self.perform_update(serializer)
        return Response(serializer.data)
    

# Add new columns
class Columns(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnDataSerialzer