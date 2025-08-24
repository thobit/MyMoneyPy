from django.db import models

# Create your models here.

class Budget(models.Model):
    name = models.CharField(max_length = 64,
                            default = 'Main Budget')
    current_balance = models.DecimalField(max_digits = 64,
                                          decimal_places = 6,
                                          default = 0)

