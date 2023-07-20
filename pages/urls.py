from django.urls import path
from .views import Home, Sobrenosotros, Mision, InicioSesion, Mantenedor, agregar_producto, agregar_bodegas, agregar_autores, agregar_editoriales, modificar_producto

urlpatterns = [
    path("", Home, name="home"),
    path("sobrenosotros/", Sobrenosotros, name="sobrenosotros"),
    path("mision/", Mision, name="mision"),
    path("iniciosesion/", InicioSesion, name="iniciosesion"),
    path("mantenedor/", Mantenedor, name="mantenedor"),
    path("agregarproducto/", agregar_producto, name="agregarproducto"),
    path("agregarbodegas/", agregar_bodegas, name="agregarbodegas"),
    path("agregarautores/", agregar_autores, name="agregarautores"),
    path("agregareditoriales/", agregar_editoriales, name="agregareditoriales"),
    path("modificar-producto/<id>/", modificar_producto, name="modificar_producto")

]
