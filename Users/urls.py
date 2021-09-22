from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

appname = "Users"

urlpatterns = [
    path(r'graphql/', csrf_exempt(GraphQLView.as_view()))
]
