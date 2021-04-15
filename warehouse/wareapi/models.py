from django.db import models

class warehouse(models.Model):
    title = models.CharField(max_length=10)
    forename = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    postcode = models.CharField(max_length=10)
    items = models.CharField(max_length=5)
    con_number = models.CharField(max_length=30)
    deliverycompany = models.CharField(max_length=60)

    def __str__(self):
        return self.surname
