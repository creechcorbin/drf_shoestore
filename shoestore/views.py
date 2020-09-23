from django.shortcuts import render

from rest_framework import viewsets
from shoestore.serializers import ShoeSerializer
from shoestore.models import Shoe

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer