from django.db import models

# Create your models here.
class login_task(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    password = models.IntegerField()



    def __str__(self):
        return self.name