from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'statastic/', views.statastic, name='statastic'),
    url(r'histogram_heat_map/', views.HistoHeat, name='histogram and heat map'),
    url(r'prediction/',views.prediction,name="prediction"),
    url(r'index/', views.index,name='index'),
    url(r'dataset/', views.dataset, name='dataset'),
    url(r'^admin/', include(admin.site.urls)),
]
