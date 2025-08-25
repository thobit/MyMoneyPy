from django.db import models
import uuid

# Create your models here.

class Account(models.Model):
    acc_id = models.UUIDField(primary_key = True,
                              default = uuid.uuid4,
                              editable = False)
    iban = models.CharField(max_length = 32,
                            default = "DE00 0000 0000 0000 0000 00")
    balance = models.DecimalField(max_digits = 24,
                                  decimal_places = 6,
                                  default = 0)
