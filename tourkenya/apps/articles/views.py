from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
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


"""
    View to retrieve specific article,
    update it and delete it
"""


class SpecificArticleView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, article_id):
        article = get_object_or_404(Articles.objects.all(), id=article_id)

        serializer = ViewArticlesSerializer(
            instance=article, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Method to edit user article. Takes in user token and article_id
    def put(self, request, article_id):
        # Try to retrieve the article or raise a 404 if article is not found
        article = get_object_or_404(Articles.objects.all(), id=article_id)

        # pick article data from the user
        article_update = request.data
        context = {'request': request}
        
        # Check if user is authorized
        ArticleSerializer.check_user_authorization(request.user, article_id)

        #  user serializer to update data in the db
        serializer = ArticleSerializer(
            instance=article, data=article_update, context=context
        )
        # Validate the data and save to the database
        if serializer.is_valid():
            serializer.save()
            response_message = {
                "message": "Article updated successfully",
                "article": serializer.data
            }
            # Return message to user upon successfull save
            return Response(response_message, status=status.HTTP_200_OK)
        # Return message 400 incase of wrong data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
