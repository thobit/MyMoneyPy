from django.db import models
import uuid

# Create your models here.

class Budget(models.Model):
    name = models.CharField(max_length = 64,
                            default = 'Main Budget')
    current_balance = models.DecimalField(max_digits = 24,
                                          decimal_places = 6,
                                          default = 0)
    target_balance = models.DecimalField(max_digits = 24,
                                         decimal_places = 6,
                                         null = True)


class BudgetTransaction(models.Model):
    tx_id = models.UUIDField(primary_key = True,
                             default = uuid.uuid4,
                             editable = False)
    amount = models.DecimalField(max_digits = 24,
                                 decimal_places = 6,
                                 default = 0)
    occured_at = models.DateTimeField(auto_now_add = True,
                                      db_index = True)
    description = models.CharField(max_length = 128,
                                   default = "money goes brrrr")

