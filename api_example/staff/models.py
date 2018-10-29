from django.db import models

class Staff(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.surname
