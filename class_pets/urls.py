from django.contrib import admin
from django.urls import path
from django.urls import include
from pets_for_students import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pets_for_students/', include('pets_for_students.urls')),
    path('admin/', admin.site.urls),
]


