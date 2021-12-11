from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
# views import
from .views import HomePageView, WeatherForecastView
from utils.views import get_city_data
# urls import
from .rosetta_urls import ROSETTA_URLS

THIRD_PARTY_URLS = [
    # Django Select2
    path("select2/", include("django_select2.urls")),
    # Django Allauth URLs
    path('accounts/', include('allauth.urls')),
]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path('i18n/', include('django.conf.urls.i18n')),
    path("get-city-data/", get_city_data, name="city_data"),
    path("get-weather-forecast/", WeatherForecastView.as_view(), name="weather_forecast"),
    prefix_default_language=False
) + THIRD_PARTY_URLS

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += ROSETTA_URLS

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
