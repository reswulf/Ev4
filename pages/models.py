from django.db import models

class Autores(models.Model):
    idautor= models.IntegerField(primary_key = True)
    autor = models.CharField(max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return self.autor

class Editoriales(models.Model):
    ideditorial = models.IntegerField(primary_key = True)
    editorial = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)


    def __str__(self):
        return self.editorial

class Bodegas(models.Model):
    idbodega = models.IntegerField(primary_key = True)
    espacio_de_bodega = models.IntegerField()
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.ciudad


# Se genera tabla intermedia entre idautor y libro, pero no es posible hacerla correr sin errores de PK
# Se deja comentada para posibles usos posteriores 

#class Autores_productos(models.Model):
    #idautor_producto = models.IntegerField(primary_key = True)
    #idautor = models.ForeignKey(Autores, on_delete=models.PROTECT)
    #idproducto = models.ForeignKey(Producto, on_delete=models.PROTECT)


class Producto(models.Model):
    idproducto = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.TextField()
    autor  = models.ForeignKey(Autores, on_delete=models.PROTECT)
    editorial = models.ForeignKey(Editoriales, on_delete=models.PROTECT)
    bodega = models.ForeignKey(Bodegas, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
