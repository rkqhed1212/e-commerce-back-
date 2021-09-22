
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from config.schema import schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('Orders.urls')),
    path('cart/', include('Carts.urls')),
    path('FAQ/', include('FAQs.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema = schema))),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)