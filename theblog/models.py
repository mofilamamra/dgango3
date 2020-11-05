from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200 )
    authr = models.ForeignKey(User , on_delete = models.CASCADE)
    body  = models.TextField()


    def get_absolute_url(self):
        return f"/post/{self.id}"

    

    def __str__(self):

        return self.title + ' | ' + str(self.authr)
