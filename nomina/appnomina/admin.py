from django.contrib import admin
from .models import Cargo, Empleado, Departamento
# Añadimos los modelos (manteminientos o formularios) al administrador.
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)

