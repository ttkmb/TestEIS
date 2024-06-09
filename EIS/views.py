from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import House, Apartment, WaterMeter, Rate, BillingRecord, WaterMeterReading
from .serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, RateSerializer, \
    BillingRecordSerializer, WaterMeterReadingSerializer
from .utils import calculate_billing


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    @action(detail=True, methods=['post'])
    def calculate_billing(self, request, pk=None):
        house = self.get_object()
        year = int(request.data.get('year'))
        month = int(request.data.get('month'))
        task = calculate_billing.delay(house.id, year, month)
        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def get_billing(self, request, pk=None):
        house = self.get_object()
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            return Response({'error': 'Year and month are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return Response({'error': 'Year and month must be integers'}, status=status.HTTP_400_BAD_REQUEST)

        billings = BillingRecord.objects.filter(apartment__house=house, month__year=year, month__month=month)
        serializer = BillingRecordSerializer(billings, many=True)
        return Response(serializer.data)


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class BillingRecordViewSet(viewsets.ModelViewSet):
    queryset = BillingRecord.objects.all()
    serializer_class = BillingRecordSerializer


class WaterMeterReadingViewSet(viewsets.ModelViewSet):
    queryset = WaterMeterReading.objects.all()
    serializer_class = WaterMeterReadingSerializer
