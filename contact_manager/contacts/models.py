from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name