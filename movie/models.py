from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    year = models.DateField( )
    created_date = models.DateTimeField(auto_now_add=True)
    update_at_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)
    janr = models.ForeignKey('janr', on_delete=models.SET_NULL,
                               null=True)
    class Meta:
        ordering = ['-id']




    def __str__(self):
        return self.name

class Janr(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

