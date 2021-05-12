from django.db import models

# Create your models here.

class Project(models.Model):
    title  = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edicion") 
    
    #esta clase sirve para pasar el nombre del Preject a español, es una clase de metadatos 
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #para oredenar los proyectos creados en fecha de creacion 
        ordering = ["-created"]
    def __str__(self):
        return self.title
