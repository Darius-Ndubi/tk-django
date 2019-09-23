from rest_framework import serializers

from .models import Articles

"""
    Class to define Article creation serializer
    takes in the author_id since an article is associated to a user
    title, body, draft (specifies if user is just storing the article
    to edit later), post (specifies if an article is finished on editing
    or is ready to be published )

"""


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField()
    body = serializers.CharField()
    draft = serializers.BooleanField()
    posted = serializers.BooleanField()

    # Defines fields fron the  article that are to be saved
    class Meta:
        model = Articles
        fields = ["author", "title", "body", "draft", "posted"]

    # Method to save article data to the data base.
    def create(self, valid_data):
        article = Articles(**valid_data)
        article.save()
        return article
