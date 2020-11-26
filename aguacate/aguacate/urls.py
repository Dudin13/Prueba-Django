"""aguacate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('register/', views.register),
    path('createidea/', views.createidea),
    path('updateidea/<int:idea_id>', views.updateidea),
    path('listorderidea/', views.listorderidea),
    path('deleteidea/<int:idea_id>', views.deleteidea),
    path('solicitud/<int:idea_id>', views.invitation),
    path('listinvitation/', views.listinvitation),    
    path('updateinvitation/<int:invitation_id>', .views.updateinvitation),
    path('listfollowers/', views.listfollowers),
    path('listfollowing/', views.listfollowing),
    path('deleteinvitation/', views.deleteinvitation),
]|
