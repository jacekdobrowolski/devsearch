
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.serializers import ProjectSerializer
from projects.models import Project, Review, Tag


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
        {'DELETE': '/api/remove-tag'}
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


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def project_vote(request, pk):
    project = Project.objects.get(project_id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project
    )

    review.value = data['value']
    review.save()
    project.count_votes()
    print(f'{data=} {user=}')
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_tag(request):
    tag_id = request.data['tag']
    project_id = request.data['project']
    project = Project.objects.get(project_id=project_id)
    tag = Tag.objects.get(tag_id=tag_id)

    project.tags.remove(tag)

    return Response('Tag was deleted')
