import graphene 
from Products import schema as product_schema
from Users import schema as user_schema

class Query(product_schema.Query, user_schema.Query, graphene.ObjectType):
    pass

class Mutation(user_schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)