from django.contrib import admin
from django.urls import path
from permisos_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verificar_permiso/', views.verificar_permiso, name='verificar_permiso'),
]
