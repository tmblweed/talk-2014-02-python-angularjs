from rest_framework import viewsets
from doge.models import DogeConversion

class DogeConversionViewSet(viewsets.ModelViewSet):
    model = DogeConversion
