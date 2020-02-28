
from datetime import datetime
from django.db import models

# Create your models here.
from django.forms import CharField


class Alumni(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    session = models.CharField(max_length=10, default='', blank=True)
    current_position = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    contact_no = models.CharField(max_length=20, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ' - ' + self.session
