from django.db import models
# Models of coustamer.
from django.contrib.auth.models import User

class Coustamer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    delete_staus = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name