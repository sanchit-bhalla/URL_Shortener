from django.urls import path
from . import views
app_name='shortener'
urlpatterns = [
    path('',views.shorten_url,name='home'),
    path('<short_id>/',views.get_url,name='get_url'),
]
