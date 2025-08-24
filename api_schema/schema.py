import graphene
from graphene_django import DjangoObjectType
from api_schema.budgets.queries import Query as BudgetsQuery
from api_schema.budgets.mutation import Mutation as BudgetsMutation

class Query(BudgetsQuery, graphene.ObjectType):
    pass

class Mutation(BudgetsMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
