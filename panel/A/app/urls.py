from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'app'

urlpatterns = [
    url('ransomwares/', views.ransomwares, name='ransomwares'),
    url('fishing/', views.fishing, name='fishing'),
    url('q/Devices/', views.Devices_q, name='Devices_q'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('settings/', views.settings, name='settings'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)