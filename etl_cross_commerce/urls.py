from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', NumbersView.as_view(), name='numbers_rest_view'),
]