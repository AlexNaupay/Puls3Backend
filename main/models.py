from django.db import models


# Create your models here

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)

    def __unicode__(self):
        return self.nombre  # Para que muestre === toString()

    # char=models.CharField(help_text="Char",max_length=100)
    # biginteger=models.BigIntegerField()
    # integer=models.IntegerField()
    # boolean=models.BooleanField()
    # nullbooolean=models.NullBooleanField()
    # # comainteger=models.CommaSeparateIntegerField()
    # date=models.DateField()
    # #date=models.DateField(auto_now=True) #Con true ya no aparece
    # datetime=models.DateTimeField()
    # decimal=models.DecimalField(max_digits=5,decimal_places=2)
    # slug=models.SlugField()
    # text=models.TextField()
    # url=models.URLField()
    # floatf=models.FloatField()
    # filef=models.FileField(upload_to='carga')
    # filepath=models.FilePathField()
    # image=models.ImageField(upload_to='carga')


class Post(models.Model):
    titulo = models.CharField(max_length=140)
    enlace = models.URLField()
    categoria = models.ForeignKey(Categoria)
    autor = models.CharField(max_length=30)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
        return self.titulo

    def votos_en_imagen(self):
        return 'http://placehold.it/200x35/22BDE0/FFFFFF/&text=%s votos' % self.votos
