from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from .models import QRInfo
from .serializers import Serializer

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class QRInfoViewSet(ModelViewSet):
    queryset = QRInfo.objects.all()
    serializer_class = Serializer
