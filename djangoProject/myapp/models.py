from django.db import models

# Create your models here.
class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.iso} {self.long_name}'

