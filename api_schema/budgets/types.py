import graphene
from graphene_django import DjangoObjectType
from budgets.models import Budget

class BudgetType(DjangoObjectType):
    class Meta:
        model = Budget
        fields = ("id", "name", "current_balance")
