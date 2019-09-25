from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response

from .serializers import (
    ArticleSerializer, ViewArticlesSerializer
)
from .models import Articles


"""
    View to create an article from the user
    Takes in title and body from request
    and user token from the context setting.
    This is using the header
"""


class CreateArticleAPIView(CreateAPIView):
    #  Set the view to only allow authorized users
    permission_classes = (IsAuthenticated, )
    # set the serializer class
    serializer_class = ArticleSerializer

    #  Since its creation the method should be post
    def post(self, request):

        # Pass the context and data to the serializer class
        serializer = ArticleSerializer(
            data=request.data,
            context={'request': request}
        )

        """
            Check if the data is valid and save the article
            giving the user back a message on success.
            Else raise exception error
        """
        if serializer.is_valid():
            serializer.save()

            response_message = {
                "message": "Article has been successfully Posted"
            }

            return Response(response_message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    View to show all created articles to both autorized and non
    authorized users
"""


class ViewAllArticles(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = ViewArticlesSerializer
    queryset = Articles.objects.all()
