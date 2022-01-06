from django.db import models

# Create your models here.
class valores(models.Model):
    id = models.AutoField(primary_key=True)
    parametros=models.CharField(max_length=100, verbose_name='parametros')
    valor=models.IntegerField(blank=False, verbose_name='valor')
    descripcion=models.TextField(verbose_name='descrpcion')


    def __str__(self):
        fila=self.parametros + str(self.valor)
        return fila 


