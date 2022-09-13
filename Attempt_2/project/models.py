from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100) #заголовок
    description = models.TextField() #описание
    coordinates = models.CharField(max_length=50) #координаты местонахождения
    image = models.FileField(upload_to='img/') #прикрепляем картинку