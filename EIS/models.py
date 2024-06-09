from django.db import models
from django.utils import timezone


class House(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='apartments')
    number = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.house} {self.number} - {self.area}'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Rate(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='water_meter')
    date = models.DateField(default=timezone.now)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.apartment} - {self.date} - {self.value}'

    class Meta:
        verbose_name = 'Показания воды'
        verbose_name_plural = 'Показания воды'


class WaterMeterReading(models.Model):
    water_meter = models.ForeignKey(WaterMeter, related_name='readings', on_delete=models.CASCADE)
    reading = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class BillingRecord(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='billing_records', on_delete=models.CASCADE)
    month = models.DateField()
    water_charge = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2)
