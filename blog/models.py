
#importaciones las cuales utilizamos para agregar contenido de otro archivo
from django.db import models
from django.utils import timezone

#esta línea define nuestro modelo (es un objeto)
class Post(models.Model): #significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #Metodo/funcion 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #cuando llamemos a __str__() obtendremos un texto (string) con un título de Post.