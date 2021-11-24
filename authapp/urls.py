from django.urls import path
from authapp.views import login, registr

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('registr/', registr, name='registr'),
]

