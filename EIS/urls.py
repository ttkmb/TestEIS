from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from .views import HouseViewSet, ApartmentViewSet, WaterMeterViewSet, RateViewSet, BillingRecordViewSet, \
    WaterMeterReadingViewSet

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Billing API",
        default_version='v1',
        description="API documentation for the billing system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router.register(r'houses', HouseViewSet, basename='houses')
router.register(r'apartments', ApartmentViewSet, basename='apartments')
router.register(r'water_meters', WaterMeterViewSet, basename='water_meters')
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'billing_records', BillingRecordViewSet, basename='billing_records')
router.register(r'water_meter_readings', WaterMeterReadingViewSet, basename='water_meter_readings')
urlpatterns = [
    path('houses/<int:pk>/calculate_billing/', HouseViewSet.as_view({'post': 'calculate_billing'})),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
