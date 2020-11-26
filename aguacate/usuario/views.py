from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Idea, Solicitud
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from django.core.exceptions import ObjectDoesNotExist

#@permission_classes([IsAuthenticated])
@api_view(["POST"])
@csrf_exempt
def register(request):
    try:
        data = request.data
        new_user = Usuario(
            email=data['email'],
            username=data['username'],
            password=data['password']
        )
        new_user.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def createidea(request):
    try:
        data = request.data
        new_idea = Idea(
        private=data['private'],
        texto=data['texto'],
        visibility=['visibility'],
        fecha=['fecha']
        )
        new_idea.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def updateidea(request, idea_id):
    user = request.user.id
    try:
        idea = Idea.objects.filter(added_by=user, id=idea_id)
        data = request.data
        new_idea = Idea(
        private=data['private'],
        texto=data['texto'],
        visibility=['visibility'],
        fecha=['fecha']
        )
        new_idea.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def listorderidea(request):
    user = request.user.id
    ideas = Idea.objects.filter(added_by=user)
    serializer = IdeasSerializer(ideas, many=True)
    return JsonResponse({'ideas': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def deleteidea(request, idea_id):
    user = request.user.id
    try:
        idea = idea.objects.get(added_by=user, id=idea_id)
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
def invitation(request):
    try:
        data = request.data
        new_invitation = Usuario(
            respuesta=data['email'],
            usernamerequest=data['username'],
            usernameinvate=data['password'],
            )
        new_invitation.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def listinvitation(request):
    user = request.user.id
    solicitud = Solicitud.objects.filter(added_by=user)
    serializer = SolicitudSerializer(solicitud, many=True)
    return JsonResponse({'Solicitudes': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def updateinvitation(request, invitation_id):
    user = request.user.id
    try:
        invitation = Solicitud.objects.filter(added_by=user, id=invitation_id)
        invitation.update(**request.data)
        return HttpResponse(safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def listfollowers(request):
    user = request.user.id
    my_user = Usuario.objects.get(id=user)
    solicitud = Solicitud.objects.filter(usernameinvate=my_user.username).filter(status=1)
    serializer = SolicitudSerializer(solicitud, many=True)
    return JsonResponse({'Followers': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def listfollowing(request):
    user = request.user.id
    solicitud = Solicitud.objects.filter(added_by=user).filter(status=1)
    serializer = SolicitudSerializer(solicitud, many=True)
    return JsonResponse({'Following': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def deleteinvitation(request, invitation_id):
    user = request.user.id
    try:
        invitation = Solicitud.objects.get(added_by=user, id=invitation_id)
        invitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
