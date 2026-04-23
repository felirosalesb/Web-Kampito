from django.db import models

# Create your models here.

class Banner(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo de la promo")
    imagen = models.ImageField(upload_to='banners/')
    orden = models.IntegerField(default=0, help_text="Orden de aparicion")
    activo = models.BooleanField(default=True)
    link = models.URLField(blank=True, null=True, help_text="Opcional: link a una categoria o producto")

    def __claro__(self):
        return self.titulo
    
    class Meta:
        ordering = ['orden']
        



