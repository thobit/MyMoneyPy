import graphene
from decimal import Decimal
from budgets.models import Budget
from .types import BudgetType

class UpdateBudgetBalance(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required = True)
        current_balance = graphene.Decimal(required = True)

    budget = graphene.Field(BudgetType)

    @staticmethod
    def mutate(root, info, id, current_balance):
        b = Budget.objects.get(pk = id)
        b.current_balance = Decimal(current_balance)
        b.save(update_fields=["current_balance"])
        return UpdateBudgetBalance(budget = b)

class Mutation(graphene.ObjectType):
    update_budget_balance = UpdateBudgetBalance.Field()

class CreateBudget(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
        current_balance = graphene.Decimal(required = False,
                                           default_value = "0")

    budget = graphene.Field(BudgetType)

    @staticmethod
    def mutate(root, info, name, current_balance = "0"):
        b = Budget.objects.create(name = name,
                                  current_balance = Decimal(current_balance))
        return CreateBudget(budget = b)

class Mutation(graphene.ObjectType):
    update_budget_balance = UpdateBudgetBalance.Field()
    create_budget = CreateBudget.Field()

