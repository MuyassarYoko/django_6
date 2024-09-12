from django.db import models


# Create your models here.

class Author(models.Model):
    fio = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.fio


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    num_pages = models.IntegerField()

    def __str__(self):
        return self.name
