from django.db import models

class Advert(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
