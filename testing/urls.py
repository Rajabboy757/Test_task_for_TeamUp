from django.urls import path
from .views import CreateTest, SetIQTestResult

urlpatterns = [
    path('create_test/', CreateTest.as_view(), name="create_test"),
    path('set_iq_test_result/', SetIQTestResult.as_view(), name="set_iq_test_result"),
]
