from django.db import models

class velocity(models.Model):
    title = models.CharField('Название', max_length=50)
    texts = models.CharField('Описание', max_length=250)
    price = models.CharField('Цена', max_length=10)

    def __str__(self):
        return self.title