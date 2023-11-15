
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets, status
from .models import Ad
from .serializers import AdSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

def parse_data():
    url = 'https://127.0.0.1.:800/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')


        title = 'Название объявления'
        description = 'Описание объявления'
        price = 100.00
        new_ad = Ad(title=title, description=description, price=price)
        new_ad.save()
        return True
    else:
        return False

@api_view(['POST'])
def create_ad_api(request):
    if request.method == 'POST':
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse

def ad_detail(ad_id):
    return HttpResponse(f'Детали объявления с ID {ad_id}')

from rest_framework import generics
from .models import ApartmentRent
from .serializers import ApartmentRentSerializer

class ApartmentRentListCreate(generics.ListCreateAPIView):
    queryset = ApartmentRent.objects.all()
    serializer_class = ApartmentRentSerializer

from rest_framework import generics
from .models import ApartmentSale
from .serializers import ApartmentSaleSerializer

class ApartmentSaleListCreate(generics.ListCreateAPIView):
    queryset = ApartmentSale.objects.all()
    serializer_class = ApartmentSaleSerializer

