from django.urls import path
from .views import CreateTest

urlpatterns = [
    path('create_test/', CreateTest.as_view(), name="create_test"),
]
