from django.db import models
import uuid

# Create your models here.

class Transaction(models.Model):
    tx_id = models.UUIDField(primary_key = True,
                             default = uuid.uuid4,
                             editable = False)
    amount = models.DecimalField(max_digits = 24,
                                 decimal_places = 6)
    tx_budget = models.ForeignKey("budgets.Budget",
                                  on_delete = models.SET_NULL,
                                  null = True,
                                  blank = True)
    tx_account = models.ForeignKey("accounts.Account",
                                   on_delete = models.SET_NULL,
                                   null = True,
                                   blank = True)
