import graphene
from budgets.models import Budget
from .types import BudgetType

class Query(graphene.ObjectType):
    budgets = graphene.List(BudgetType)
    budget = graphene.Field(BudgetType, id=graphene.ID(required=True))

    def resolve_budgets(root, info):
        return Budget.objects.all()

    def resolve_budget(root, info, id):
        return Budget.objects.get(pk=id)
