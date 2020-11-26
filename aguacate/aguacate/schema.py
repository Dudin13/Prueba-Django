import graphene
from graphene_django import DjangoObjectType
from .models import Usuario, Idea, Solicitud

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("id", "username","email","password")

class IdeaType(DjangoObjectType):
    class Meta:
        model = Idea
        fields = ("id", "private","texto", "visibility", "fecha")

class SolicitudType(DjangoObjectType):
    class Meta:
        model = Solicitud
        fields = ("id", "respuesta","usernamerequest", "usernameinvate", "status")

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.String())

    timeline = graphene.List(IdeaType)
    def resolve_timeline(root, info, **kwargs):
        return Idea.objects.all()

    followers = graphene.List(SolicitudType)
    def resolve_followers(root, info, **kwargs):
        return Idea.objects.all()
