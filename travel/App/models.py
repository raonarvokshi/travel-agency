from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Registered_emails(models.Model):
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email


class Book(models.Model):
    destination = models.CharField(max_length=20)
    departure_date = models.DateField()
    return_date = models.DateField()
    travelers = models.IntegerField()
    approved = models.BooleanField(blank=True, null=True)
    not_approved = models.BooleanField(blank=True, null=True)
    pending = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-departure_date",)

    def __str__(self):
        return self.destination
