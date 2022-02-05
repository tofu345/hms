from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    occupied = models.BooleanField(default=False)
    occupant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.occupant:
            return f"{self.name} uccupied by {self.occupant}"
        else:
            return f"{self.name} free"
