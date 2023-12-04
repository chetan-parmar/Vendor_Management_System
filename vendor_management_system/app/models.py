from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name