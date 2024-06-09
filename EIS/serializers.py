from rest_framework import serializers
from .models import House, Apartment, WaterMeter, Rate, WaterMeterReading, BillingRecord


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class WaterMeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeterReading
        fields = '__all__'


class WaterMeterSerializer(serializers.ModelSerializer):
    readings = WaterMeterReadingSerializer(many=True, read_only=True)
    tariff = RateSerializer(read_only=True)

    class Meta:
        model = WaterMeter
        fields = '__all__'


class BillingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingRecord
        fields = ['apartment', 'month', 'water_charge', 'maintenance_charge', 'total_charge']


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, read_only=True)
    billing_records = BillingRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
