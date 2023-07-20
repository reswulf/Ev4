from django.contrib import admin
from .models import Autores, Editoriales, Bodegas, Producto

# Register your models here.

admin.site.register(Autores)
admin.site.register(Editoriales)
admin.site.register(Bodegas)
admin.site.register(Producto)
