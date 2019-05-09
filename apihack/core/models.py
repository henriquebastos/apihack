from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()



class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    pages = models.IntegerField()
