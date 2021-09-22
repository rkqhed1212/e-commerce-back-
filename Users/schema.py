import graphene
from graphene_django import DjangoObjectType,DjangoListField
from Users.models import User

class User_list(DjangoObjectType):

    class Meta:
        model = User
        fields = ('nick_name', 'number','gender',)

class Query(graphene.ObjectType):
    
    all_user = graphene.List(User_list)

    def resolve_all_user(root,info):
        return User.objects.all()


class ResisterMutation(graphene.Mutation):

    class Arguments:
        nick_name = graphene.String()
        number = graphene.Int()
        username = graphene.String()

    user = graphene.Field(User_list)

    def mutate(self, info, username, nick_name, number):
        user = User(username=username, nick_name=nick_name, number=number)
        user.save()
        return ResisterMutation(user=user)

class Mutation(graphene.ObjectType):

    update_user = ResisterMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)