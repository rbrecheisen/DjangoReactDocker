from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Item

class ItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Item.objects.values_list('name', flat=True)
        return Response({"items": list(items)})
