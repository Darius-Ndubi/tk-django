from django.urls import path

from .views import SignUpAPIView, SignInAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name="sign_up"),
    path('signin/', SignInAPIView.as_view(), name="sign_in"),
]
