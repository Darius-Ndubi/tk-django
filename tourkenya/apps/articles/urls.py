from django.urls import path

from .views import (
    CreateArticleAPIView, SpecificArticleView
)

urlpatterns = [
    path('create/', CreateArticleAPIView.as_view(), name="create_article"),
    path('<int:article_id>/', SpecificArticleView.as_view(), name='specific_article'),
    path('<int:article_id>/update', SpecificArticleView.as_view(), name='update_article'),
    path('<int:article_id>/delete', SpecificArticleView.as_view(), name='delete_article'),
]
