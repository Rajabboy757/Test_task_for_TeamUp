from django.urls import path
from .views import CreateTest, SetIQTestResult, SetEQTestResult, GetAllResults

urlpatterns = [
    path('create_test/', CreateTest.as_view(), name="create_test"),
    path('set_iq_test_result/', SetIQTestResult.as_view(), name="set_iq_test_result"),
    path('set_eq_test_result/', SetEQTestResult.as_view(), name="set_eq_test_result"),
    path('get_all_results/<str:login>/', GetAllResults.as_view(), name="get_all_results"),

]
