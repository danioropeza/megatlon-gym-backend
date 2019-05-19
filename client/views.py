from .models import ( Client )
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import ( ClientSerializers )

class ClientCreateAPI(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class ClientListAPI(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class ClientDetailAPI(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class ClientUpdateAPI(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class ClientDeleteAPI(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

