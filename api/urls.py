from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('create', views.apiCreateTree, name='createTree'),
    path('list', views.apiList, name='apiList'),
    path('lca', views.apiLowAncestor, name='apiLowAncestor'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
