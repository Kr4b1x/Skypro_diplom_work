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
    """
    List all training models, or create a new training model.
    """
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class TrainModelDetailAPIView(RetrieveAPIView):
    """
    Retrieve, update or delete a training model.
    """
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]


class TrainModelCreateAPIView(CreateAPIView):
    """
    Create a new training model.
    """
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class TrainModelUpdateAPIView(UpdateAPIView):
    """
    Update an existing training model.
    """
    queryset = TrainModel.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class TrainModelDestroyAPIView(DestroyAPIView):
    """
    Delete a training model.
    """
    queryset = TrainModel.objects.all()
    permission_classes = [IsAdmin]
