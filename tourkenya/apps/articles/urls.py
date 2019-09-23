from django.urls import path

from .views import CreateArticleAPIView

urlpatterns = [
    path('create/', CreateArticleAPIView.as_view(), name="create_article"),
]
