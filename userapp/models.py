from django.db import models

# Create your models here.
class userform(models.Model):
    email = models.EmailField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.email
    