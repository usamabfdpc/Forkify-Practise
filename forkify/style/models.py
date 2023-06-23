from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    PERSONAL_CHOICES =(
        ('p','play'),
        ('r','Read'),
        ('w','Walk')
    )

    title = models.CharField(max_length=100)
    choices = models.CharField(max_length=1,choices=PERSONAL_CHOICES,default=PERSONAL_CHOICES[0])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author')


