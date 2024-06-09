from datetime import timedelta, datetime
from decimal import Decimal

from celery import shared_task

from EIS.models import House, BillingRecord, Rate, WaterMeterReading


@shared_task(bind=True)
def calculate_billing(self, house_id, year, month):
    try:
        house = House.objects.get(id=house_id)
        water_tariff = Rate.objects.get(name="Water")
        maintenance_tariff = Rate.objects.get(name="Maintenance")

        for apartment in house.apartments.all():
            water_charge = Decimal(0)
            for meter in apartment.water_meter.all():
                current_reading = WaterMeterReading.objects.filter(water_meter=meter, date__year=year,
                                                                   date__month=month).first()
                if current_reading:
                    previous_reading_date = current_reading.date - timedelta(days=30)
                    previous_reading = WaterMeterReading.objects.filter(water_meter=meter,
                                                                        date=previous_reading_date).first()
                    if previous_reading:
                        consumption = current_reading.reading - previous_reading.reading
                        water_charge += consumption * water_tariff.price

            maintenance_charge = apartment.area * maintenance_tariff.price
            total_charge = water_charge + maintenance_charge

            billing_record = BillingRecord(
                apartment=apartment,
                month=datetime(year, month, 1),
                water_charge=water_charge,
                maintenance_charge=maintenance_charge,
                total_charge=total_charge
            )
            billing_record.save()
        return 'Billing calculation completed'
    except Exception as exc:
        self.retry(exc=exc, countdown=60)
