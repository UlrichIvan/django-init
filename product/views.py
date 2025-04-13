from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ProductSerializer


@api_view(["GET"])
def index(_) -> Response:
    return Response("Hello world!")


@csrf_exempt
@api_view(["POST"])
def create(request):
    Done = False
    try:
        serializer: ProductSerializer = ProductSerializer(data=request.data)
        Done = True if serializer.is_valid() else False
        if Done:
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response("invalide data", status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(
            [request.data, Done],
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
