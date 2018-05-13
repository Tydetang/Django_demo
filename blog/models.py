from django.db import models

# Create your models here.

class ip_port(models.Model):
    ip = models.CharField(max_length=30)
    port = models.CharField(max_length=300)