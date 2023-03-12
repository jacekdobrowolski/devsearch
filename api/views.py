from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def get_routes(response):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(project_id=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)
