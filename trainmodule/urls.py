from django.urls import path

from .apps import TrainmoduleConfig
from .views import (
    TrainModelAPIView,
    TrainModelDetailAPIView,
    TrainModelCreateAPIView,
    TrainModelUpdateAPIView,
    TrainModelDestroyAPIView,
)

app_name = TrainmoduleConfig.name

urlpatterns = [
    path("models/", TrainModelAPIView.as_view(), name="models"),
    path("models/<int:pk>/", TrainModelDetailAPIView.as_view(), name="model"),
    path("models/create/", TrainModelCreateAPIView.as_view(), name="create"),
    path("models/delete/<int:pk>/", TrainModelDestroyAPIView.as_view(), name="delete"),
    path("models/update/<int:pk>/", TrainModelUpdateAPIView.as_view(), name="update"),
]
