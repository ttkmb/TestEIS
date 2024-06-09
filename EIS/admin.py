from django.contrib import admin

from EIS.models import House, Apartment, WaterMeter, Rate, WaterMeterReading, BillingRecord


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    search_fields = ('address',)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'area', 'house')
    search_fields = ('number', 'house__address')
    list_filter = ('house',)


@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment', 'date', 'value')
    search_fields = ('apartment__number', 'apartment__house__address')
    list_filter = ('apartment',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


@admin.register(WaterMeterReading)
class WaterMeterReadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'water_meter', 'reading', 'date')
    search_fields = ('water_meter__apartment__number', 'water_meter__apartment__house__address')
    list_filter = ('water_meter',)


@admin.register(BillingRecord)
class BillingRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment', 'month', 'water_charge', 'maintenance_charge', 'total_charge')
    search_fields = ('apartment__number', 'apartment__house__address')
    list_filter = ('apartment', 'month')
