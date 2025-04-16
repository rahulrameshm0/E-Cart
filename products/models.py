from django.db import models

# Models for products
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'), (DELETE,'Delete'))
    title = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    priority = models.IntegerField(default=0)
    delete_staus = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title   