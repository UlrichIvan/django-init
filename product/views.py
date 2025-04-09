from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
from .serializer import ProductSerializer
from rest_framework.views import APIView


@require_http_methods(["GET"])
def index(request) -> HttpResponse:
    return HttpResponse("Hello world!")


@csrf_exempt
@require_http_methods(["POST"])
class Create(APIView):
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        try:
            body = ProductSerializer(data=request.body)
            if body.is_valid():
                p = Product(request.body)
                p.save()
                return HttpResponse("product save successfully!")
            else:
                return HttpResponse("invald product data")
        except BaseException as e:
            raise e
