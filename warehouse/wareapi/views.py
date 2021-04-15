from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WarehouseSerializer
from .models import warehouse

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = warehouse.objects.all().order_by('surname')
    serializer_class = WarehouseSerializer
