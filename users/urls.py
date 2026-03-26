from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payment_list"),
] + router.urls
