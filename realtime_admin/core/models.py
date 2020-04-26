from django.db import models


class Order(models.Model):
    product = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return self.product
