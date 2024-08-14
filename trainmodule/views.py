from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from trainmodule.models import TrainModel
from trainmodule.pagination import MyPagination
from trainmodule.permissions import IsAdmin
from trainmodule.serializers import TrainSerializer


class TrainModelAPIView(ListAPIView):
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class TrainModelDetailAPIView(RetrieveAPIView):
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]


class TrainModelCreateAPIView(CreateAPIView):
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class TrainModelUpdateAPIView(UpdateAPIView):
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class TrainModelDestroyAPIView(DestroyAPIView):
    queryset = TrainModel.objects.all()
    permission_classes = [IsAdmin]
